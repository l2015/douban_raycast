import { List, ActionPanel } from "@raycast/api";
import { useState, useEffect } from "react";
import axios from "axios";
import cheerio from "cheerio";

type Movie = {
  title: string;
  year: string;
  rating: string;
  actors: string[];
};

type SearchResults = Movie[];

export default function DoubanSearch() {
  const [search, setSearch] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [results, setResults] = useState<SearchResults>([]);

  useEffect(() => {
    async function searchMovies(query: string) {
      try {
        setLoading(true);
        const response = await axios.get(
          `https://www.douban.com/search?q=${query}&cat=1002`,
          {
            headers: {
              "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            },
          }
        );
        const html = response.data;
        const $ = cheerio.load(html);
        const items = $("div.result");
        const movies: SearchResults = [];

        items.each((index, item) => {
          if (index >= 5) {
            return;
          }

          const titleEl = $(item).find("div.title a");
          const ratingEl = $(item).find("span.rating_nums");
          const yearEl = $(item).find("span.subject-cast:last-child");
          const actorsEl = $(item).find("span.subject-cast:last-child");
          console.log(actorsEl);
          const title = titleEl?.text()?.trim() || "Unknown Title";
          const rating = ratingEl?.text()?.trim() || "N/A";
          const year = yearEl
            ?.text()
            ?.trim()
            .split("/")
            .pop() || "Unknown Year";
          const actors = actorsEl
            ?.text()
            ?.trim()
            .split("/")
            .slice(0, -1)
            .map((actor) => actor.trim()) || ["Unknown Actor"];

          const movie: Movie = {
            title,
            rating,
            year,
            actors,
          };

          movies.push(movie);
        });

        setResults(movies);
        setLoading(false);
      } catch (error) {
        console.error("Failed to search movies from Douban:", error);
        setLoading(false);
      }
    }

    if (search.trim().length > 0) {
      searchMovies(search);
    }
  }, [search]);

  const handleSearchTextChange = (searchText: string) => {
    setSearch(searchText);
  };

  const handleSelectMovie = (movie: Movie) => {
    console.log(`Selected movie: ${movie.title}`);
  };


  return (
    <List isLoading={loading} searchBarPlaceholder="Search movies on Douban" onSearchTextChange={handleSearchTextChange}>
      {results.map((movie) => (
        <List.Item
          key={movie.title}
          title={movie.title}
          subtitle={`年代: ${movie.year} | 评分: ${movie.rating} |  ${movie.actors.join(", ")}`}
          actions={
            <ActionPanel>
              <ActionPanel.Item title="Select" onAction={() => handleSelectMovie(movie)} />
            </ActionPanel>
          }
        />
      ))}
    </List>
  );
}

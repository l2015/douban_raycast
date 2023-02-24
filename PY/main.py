import requests
from bs4 import BeautifulSoup


def search_douban(query):
    url = f"https://www.douban.com/search?q={query}&cat=1002"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("div", class_="result")
    # print(results)
    for i, result in enumerate(results[:5]):
        # title = result.find("a", class_="subject-cast").get_text().strip()
        title = result.find("div", class_="title").find("a").get_text().strip()
        rating_span = result.find("span", class_="rating_nums")
        if rating_span:
            rating = rating_span.get_text().strip()
        else:
            rating = "N/A"
        rating = result.find("span", class_="rating_nums").get_text().strip()
        year = result.find("span", class_="subject-cast").get_text().strip().split("/")[-1]
        actors = result.find("span", class_="subject-cast").get_text().strip().split("/")[:-1]
        print(f"{i + 1}. {title}\n评分：{rating}\n年代：{year}\n主演：{', '.join(actors)}\n")


if __name__ == '__main__':
    query = input("请输入要搜索的影视名称：")
    search_douban(query)

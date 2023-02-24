# Douban for Raycast

This is a [Raycast](https://raycast.com/) script that allows you to search for movies on Douban, a popular Chinese movie review and rating platform. The script displays the top 5 search results along with their titles, ratings, years, and actors.

## Requirements

- [Raycast](https://raycast.com/)
- [Python 3](https://www.python.org/downloads/)
- [BeautifulSoup 4](https://pypi.org/project/beautifulsoup4/)
- [requests](https://pypi.org/project/requests/)

## Installation

1. Install [Raycast](https://raycast.com/).
2. Install Python 3, if you haven't already, by following the instructions on the official [Python website](https://www.python.org/downloads/).
3. Install the required Python packages by running the following command in the terminal:

```
pip3 install beautifulsoup4 requests
```

1. In the Raycast app, click the gear icon to open **Preferences**, then click **Extensions**.
2. Click the **+** button and select **Add Script Directory**.
3. Navigate to the directory where the `douban.py` script is located and select it.

## Usage

To search for a movie on Douban, open Raycast and type `db` followed by the Enter key to activate the script. Then, enter the name of the movie you want to search for and press Enter again. For example, to search for "The Godfather", you would do the following:

1. Type `db` and press Enter to activate the script.
2. Type `The Godfather` and press Enter to run the script.

The script will display the top 5 search results, which include the movie title, rating, year, and actors. You can then click on a result to open its page on Douban.

## Example

Here's an example of how to use the script:

```
1. 流浪地球2 年代： 2023 评分：8.3 主演：原名:流浪地球2 ,  郭帆 ,  吴京 
2. 流浪地球 年代： 2019 评分：7.9 主演：原名:流浪地球 ,  郭帆 ,  吴京 
3. 流浪地球3 年代： 2027 评分：N/A 主演：原名:流浪地球3 ,  郭帆 ,  吴京 
4. 流浪地球2——纪录片 年代： 2023 评分：N/A 主演：原名:流浪地球2——纪录片 ,  郭帆 
5. 流星撞地球 年代： 1998 评分：3.3 主演：原名:Meteorites! ,  罗珊妮·哈特 
```

## Credits

This script was created by [LongYu](https://github.com/l2015).
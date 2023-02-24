#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title db
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Placeholder" }
# @raycast.packageName DoubanForRayCast

# Documentation:
# @raycast.author LongYu
# @raycast.authorURL https://github.com/l2015

import sys
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
	for i, result in enumerate(results[:5]):
		title = result.find("div", class_="title").find("a").get_text().strip()
		rating_span = result.find("span", class_="rating_nums")
		if rating_span:
			rating = rating_span.get_text().strip()
		else:
			rating = "N/A"
		year = result.find("span", class_="subject-cast").get_text().strip().split("/")[-1]
		actors = result.find("span", class_="subject-cast").get_text().strip().split("/")[:-1]
		print(f"{i + 1}. \033[1m{title}\033[0m 年代：{year} 评分：\033[1m{rating}\033[0m 主演：{', '.join(actors)}")
		if i == 4:
			break
		
		
if __name__ == '__main__':
	query = sys.argv[1]
	search_douban(query)
	

	
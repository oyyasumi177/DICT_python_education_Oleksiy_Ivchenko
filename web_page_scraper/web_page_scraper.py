import os
import requests
from bs4 import BeautifulSoup

pages_input = input().strip()
if pages_input.isdigit():
    pages = int(pages_input)
else:
    pages = 1

article_type = input().strip()

headers = {"Accept-Language": "en-US,en;q=0.5"}

for page in range(1, pages + 1):
    dir_name = "Page_" + str(page)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page=" + str(page)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article")

        for article in articles:
            type_tag = article.find("span", {"data-test": "article.type"})

            if type_tag and type_tag.text.strip() == article_type:
                link_tag = article.find("a", {"data-track-action": "view article"})

                if link_tag:
                    title = link_tag.text.strip()

                    clean_title = ""
                    for char in title:
                        if char.isalnum() or char == " ":
                            clean_title = clean_title + char
                    clean_title = clean_title.replace(" ", "_")

                    article_url = "https://www.nature.com" + link_tag.get("href")
                    art_response = requests.get(article_url, headers=headers)

                    if art_response.status_code == 200:
                        art_soup = BeautifulSoup(art_response.text, "html.parser")

                        body = art_soup.find("div", class_="c-article-body")
                        if not body:
                            body = art_soup.find("div", class_="article__body")
                        if not body:
                            body = art_soup.find("div", class_="article-item__body")
                        if not body:
                            body = art_soup.find("article")

                        if body:
                            text = body.get_text(separator="\n").strip()
                            file_path = os.path.join(dir_name, clean_title + ".txt")

                            with open(file_path, "w", encoding="utf-8") as file:
                                file.write(text)

print("Processing elapsed.")
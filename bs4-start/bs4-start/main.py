from bs4 import BeautifulSoup

import requests

responses = requests.get("https://news.ycombinator.com/")
yc_web_page =responses.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
articles_texts = []
articles_links = []
for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)
articles_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

largest_number = max(articles_upvotes)
largest_index = articles_upvotes.index(largest_number)
print(articles_texts[largest_index])
print(articles_links[largest_index])
# print(articles_texts)
# print(articles_links)
print(int(articles_upvotes[0].split()[0]))


















# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title.string)
# print(soup.title.name)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.name)

# class_is_heading = soup.find_all(class_="heading")
# print(class_is_heading)

# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)


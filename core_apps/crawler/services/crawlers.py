import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from django.template.defaultfilters import slugify


def url_maker(url):
    splited = url.split("/")
    return f"{splited[0]}//{splited[2]}/{splited[-2]}"


def crawl_categories(url):
    df = pd.read_xml(url)
    print(f"crawled {len(df)} catogies")
    df = df["loc"]
    categories = df.apply(url_maker, 1)
    categories = set(categories)
    print(f"we have {len(categories)} unique categories")
    return categories


def get_links_from_category(categories):
    data = {}

    for i, category_url in enumerate(categories, start=1):
        category_name = category_url.split("/")[-1]
        print(f"start crawling {category_name} {i}/{len(categories)}")
        req = requests.get(category_url)
        soup = bs(req.content, features="lxml")

        cards = soup.select("div.custom-income-card")
        links = []

        print(f"There are {len(cards)} cards in this category")

        for card in cards:
            link = card.select_one("a.custom-card-link-wrapper").get("href")
            name = card.select_one("h4.card-title").get_text(strip=True)
            links.append(
                {
                    "name": name,
                    "link": link,
                    "category": category_name,
                }
            )
        data[category_name] = links

        print("crawld all cards info")
    return data


def crawl_level(url):
    name = url.split("/")[-2]
    table = pd.read_html(url)[0]
    mask = table[table["Hourly Income"] != "-"]
    mask.drop(["Payback (hours/days)"], axis=1, inplace=True)
    mask = mask.astype({"Upgrade Cost": "int", "Hourly Income": "int"})
    listed = [row.tolist() + [slugify(name)] for index, row in mask.iterrows()]

    return listed

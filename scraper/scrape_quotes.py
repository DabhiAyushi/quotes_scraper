import requests
from bs4 import BeautifulSoup
import os
import sys

sys.path.append(os.path.dirname(__file__))

from utils import save_to_csv
from database import init_db, insert_quotes

BASE_URL = "https://quotes.toscrape.com"


def scrape_quotes(pages=10):
    all_quotes = []

    for page in range(1, pages + 1):
        url = f"{BASE_URL}/page/{page}/"
        print(f"Scraping page {page}: {url}")

        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch page {page}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        for q in quotes:
            quote_text = q.find("span", class_="text").get_text(strip=True)
            author = q.find("small", class_="author").get_text(strip=True)

            tags = [tag.get_text(strip=True) for tag in q.find_all("a", class_="tag")]
            tags_str = ", ".join(tags)

            author_relative_url = q.find("a")["href"]
            author_profile = BASE_URL + author_relative_url

            all_quotes.append({
                "quote": quote_text,
                "author": author,
                "tags": tags_str,
                "author_profile": author_profile
            })

    return all_quotes


if __name__ == "__main__":
    quotes = scrape_quotes(pages=10)

    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "..", "data", "quotes.csv")
    db_path = os.path.join(base_dir, "..", "data", "quotes.db")

    save_to_csv(quotes, csv_path)

    conn = init_db(db_path)
    insert_quotes(conn, quotes)
    conn.close()

    print(f"\nSaved {len(quotes)} quotes to CSV and SQLite database")

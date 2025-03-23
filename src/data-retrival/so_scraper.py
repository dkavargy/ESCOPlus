# so_scraper.py

import requests
import time
import pandas as pd

STACK_OVERFLOW_API_URL = "https://api.stackexchange.com/2.3/tags"
SITE = "stackoverflow"
PAGE_SIZE = 100  # Max allowed
MAX_PAGES = 5    # Adjust based on desired volume

def fetch_tags(pages=MAX_PAGES):
    """
    Fetches Stack Overflow tags using the Stack Exchange API.
    """
    all_tags = []

    for page in range(1, pages + 1):
        print(f"Fetching page {page}...")
        response = requests.get(
            STACK_OVERFLOW_API_URL,
            params={
                "page": page,
                "pagesize": PAGE_SIZE,
                "order": "desc",
                "sort": "popular",
                "site": SITE
            }
        )
        if response.status_code != 200:
            print(f"Failed to fetch page {page}")
            break

        data = response.json()
        tags = data.get("items", [])
        all_tags.extend(tags)

        if not data.get("has_more", False):
            break

        time.sleep(1)  # Respect API rate limit

    return all_tags


def tags_to_dataframe(tags):
    """
    Converts API tag results to a pandas DataFrame.
    """
    df = pd.DataFrame(tags)
    df = df[["name", "count"]]
    df.columns = ["tag", "count"]
    df = df.sort_values(by="count", ascending=False)
    return df


def save_tags_to_csv(filename="data/raw/stackoverflow_tags.csv", pages=MAX_PAGES):
    tags = fetch_tags(pages)
    df = tags_to_dataframe(tags)
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} tags to {filename}")


if __name__ == "__main__":
    save_tags_to_csv()

from collections import defaultdict
from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException


def get_urls_list(filename: str = "urls.txt"):
    try:
        with open(filename, "r") as files:
            urls = files.read().strip().split("\n")
            return urls
    except FileNotFoundError:
        raise SystemExit(f'URLs list "{filename}" does not exist')
    except PermissionError:
        raise SystemExit(f'Permission denied for file "{filename}"')


def get_url(url: str):
    try:
        req = requests.get(url)
        req.raise_for_status()
        return req.text
    except RequestException as rx:
        print(f"Failed to get URL {url} with error {rx}")


def get_prices(html: str):
    results = defaultdict()
    fields = [
        "used_price",
        "complete_price",
        "new_price",
        "graded_price",
        "box_only_price",
        "manual_only_price",
    ]

    soup = BeautifulSoup(html, features="html.parser")
    for field in fields:
        if val := soup.find(id=field):
            results[field] = val

    return results


def main():
    urls = get_urls_list()
    print("\n".join(urls))

    for url in urls[:1]:
        html = get_url(url)
        # print(soup.prettify())
        prices = get_prices(html)
        print(prices)


if __name__ == "__main__":
    main()

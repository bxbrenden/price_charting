from datetime import datetime
from typing import Dict

from bs4 import BeautifulSoup
import pandas as pd
import requests
from requests.exceptions import RequestException
import yaml


def get_url_data(filename: str = "urls.yaml"):
    try:
        with open(filename, "r") as files:
            url_data = yaml.safe_load(files)
            return url_data
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
    results = dict()
    fields = {
        "used_price": "Ungraded",
        "complete_price": "Grade 7",
        "new_price": "Grade 8",
        "graded_price": "Grade 9",
        "box_only_price": "Grade 9.5",
        "manual_only_price": "Grade 10",
    }

    soup = BeautifulSoup(html, features="html.parser")
    for field, grade_level in fields.items():
        if val := soup.find("td", {"id": field}):
            children = val.findChildren("span", {"class": "price"}, recursive=False)
            if not children:
                raise SystemExit("No child elements found")
            else:
                for child in children:
                    price_str = child.text.strip().replace("$", "").replace(" ", "")
                    try:
                        price = float(price_str)
                    except ValueError:
                        raise SystemExit(f'Could not turn value "{price_str}"')
                    results[grade_level] = price

    return results


def results_to_dataframe(results: Dict[str, Dict[str, float]]) -> pd.DataFrame:
    all_series = []
    for pokemon in results.keys():
        index = results[pokemon].keys()
        values = results[pokemon].values()
        s = pd.Series(data=values, index=index, name=pokemon, dtype="float64")
        all_series.append(s)

    df = pd.DataFrame(data=all_series)
    return df


def pokemon_prices_to_excel(pokemon_prices: pd.DataFrame):
    date_time_stamp = datetime.today().isoformat(sep="-", timespec="seconds")
    pokemon_prices.to_excel(
        f"Pokemon-Prices-{date_time_stamp}.xlsx", sheet_name="Prices"
    )


def main():
    url_data = get_url_data()
    prices = dict()

    for pokemon in url_data.keys():
        url = url_data[pokemon]
        html = get_url(url)
        price = get_prices(html)
        prices[pokemon] = price

    pokemon_prices = results_to_dataframe(prices)
    print(pokemon_prices)
    pokemon_prices_to_excel(pokemon_prices)


if __name__ == "__main__":
    main()

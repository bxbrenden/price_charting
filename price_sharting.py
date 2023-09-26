from bs4 import BeautifulSoup
import requests


def get_urls_list(filename="urls.txt"):
    try:
        with open(filename, 'r') as files:
            urls = files.read().strip().split('\n')
            return urls
    except FileNotFoundError:
        raise SystemExit(f'URLs list "{filename}" does not exist')
    except PermissionError:
        raise SystemExit(f'Permission denied for file "{filename}"')


def main():
    urls = get_urls_list()
    print('\n'.join(urls))


if __name__ == '__main__':
    main()

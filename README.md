# Price Charting

A simple web scraper to make an Excel spreadsheet of Pokemon card values from [pricecharting.com](https://www.pricecharting.com/) data.
<img src="https://github.com/bxbrenden/price_charting/blob/main/spreadsheet-example.png" width="900px" title="Spreadsheet Example">

**Note**: this repository is for reference only, and I won't accept any PRs, issues, or suggestions.
As it stands, this tool harvests publicly-accessible data and is not meant to circumvent any DRM or legal restrictions.
Please do not use this tool to abuse any terms of service or do anything illegal.


## Prerequisites
- You need python3 installed and accessible in `$PATH`.
- You also need `pipenv`, which can be installed with this command: `python3 -m pip install pipenv`.

## Installing
Use `pipenv` to install all needed dependencies:
```
pipenv install
```

Then enter pipenv's virtual environment:
```
pipenv shell
```

## Setup
You need to feed the `price_charting.py` script a file called `urls.yaml` filled with Pokemon names and URLs like so:
```
---
# content of urls.yaml
Alakazam Base Set: https://www.pricecharting.com/game/pokemon-base-set/alakazam-1
Ampharos 1st Edition: https://www.pricecharting.com/game/pokemon-neo-genesis/ampharos-1st-edition-1
Ancient Mew: https://www.pricecharting.com/game/pokemon-promo/ancient-mew
```

## Running
To run the script, ensure you've installed dep's and entered the pipenv virtualenv, then run the script:
```
python3 price_charting.py
```

You'll see some debugging output that shows scraping progress, e.g.:
```
Scraping URL: https://www.pricecharting.com/game/pokemon-base-set/alakazam-1
Scraping URL: https://www.pricecharting.com/game/pokemon-neo-genesis/ampharos-1st-edition-1
Scraping URL: https://www.pricecharting.com/game/pokemon-promo/ancient-mew
```

## Getting Results
After running the script, you will see a preview of the results in the form of a Pandas DataFrame:
```
                       Ungraded  Grade 7  Grade 8  Grade 9  Grade 9.5  Grade 10
Pokemon
Alakazam Base Set         14.90    44.57    56.86   120.93     152.98    533.95
Ampharos 1st Edition      41.84    55.30    57.50    90.00     197.50    390.90
Ancient Mew               26.00    35.51    36.80    62.58     131.99    336.90
```

To see the full results, check the directory where you ran the script for a new Excel spreadsheet.
The file name will be something like this:
```
Pokemon-Prices-2023-01-01-12:00:00.xlsx
```

Open the spreadsheet with your spreadsheeting program of choice.

## References
I found [this page](https://relentlessdragon.com/pokemon-card-game/identifying-early-pokemon-cards/) helpful for identifying old series of Pokemon cards.

These pages from PSA helped me learn about card grading:
- https://www.psacard.com/photograde/1/1952-topps-mickey-mantle-311
- https://blog.psacard.com/2020/09/17/declared-value-is-easy-to-determine/

I found these sites helpful when making this tool:
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find
- https://tedboy.github.io/bs4_doc/generated/generated/bs4.NavigableString.html
- https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class
- https://stackoverflow.com/questions/6287529/how-to-find-children-of-nodes-using-beautifulsoup
- https://pandas.pydata.org/docs/reference/api/pandas.Series.html
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html
- https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component
- https://stackoverflow.com/questions/34509198/no-module-named-openpyxl-python-3-4-ubuntu
- https://stackoverflow.com/questions/31765295/convert-float-to-currency-in-pandas-before-writing-to-excel-the-right-way
- https://stackoverflow.com/questions/59794843/xlsxwriter-error-attributeerror-workbook-object-has-no-attribute-add-format
- https://stackoverflow.com/questions/76090979/xlsxwriter-object-has-no-attribute-save-did-you-mean-save
- https://stackoverflow.com/questions/64568432/xlsxwriter-how-to-increase-decimal-precision-of-float-number
- https://stackoverflow.com/questions/18022845/how-to-get-set-a-pandas-index-column-title-or-name
- https://stackoverflow.com/questions/49641690/thick-border-in-xlsxwriter
- https://xlsxwriter.readthedocs.io/format.html#set_align
- https://stackoverflow.com/questions/21599809/python-xlsxwriter-set-border-around-multiple-cells
- https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/#
- https://stackoverflow.com/questions/58741879/how-to-fix-alignment-problem-in-xlsxwriter

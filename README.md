Purpose
========

Scrape https://www.nytimes.com/crosswords/game/mini web page.
Clues under "Across" and "Down" list are save in a json file.    

Requirements
============

* Python 3.8+
* Works on Linux

Install
=======

    pip install pandas
    pip install requests
    pip install beautifulsoup4

Run
=======   
    python Scraper.py export.json

* File name is optional, default file name "Export_DataFrame.json"

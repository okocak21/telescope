'''
Web scraping https://www.nytimes.com/crosswords/game/mini
Scraping  "Across" and "Down" List
The script will loop through "Across" and "Down"  list.
'''

import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd


def df_print(p_df):
    """
    This function prints DataFrame
    """
    l_gr = p_df['Group']
    l_number = p_df['Number']
    l_string = p_df['String']

    for i in range(l_gr.count()):
        print("=== {} ===".format(str(l_gr[i])))
        for j in range(len(l_number[i])):
            print('{}. {}'.format(l_number[i][j], l_string[i][j]))


def scrap_url(url, file_name):
    '''
    Scraps url
    :param url: Web URL
    :param file_name:   json file name
    '''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    divs = soup.find_all('div', 'ClueList-wrapper--3m-kd')
    parse_values(divs, file_name)

def parse_values(divs, file_name):
    '''
    Parse html div values
    :param divs: html div
    :param file_name: json file name
    '''
    data = []
    for div in divs:
        soup = BeautifulSoup(str(div), "html.parser")
        h3s = soup.find_all('h3', 'ClueList-title--1-3oW')
        group = h3s[0].text.strip()

        lis = soup.find_all('li', 'Clue-li--1JoPu')

        f_list = []
        v_list = []
        for li in lis:
            field = li.find('span').text
            value = li.text.replace(field, '')
            f_list.append(field)
            v_list.append(value)
        data.append([group, f_list, v_list])
    save_json(data, file_name)


def save_json(data, file_name):
    '''
    Save dataframe to json file
    :param data: Data Frame
    :param file_name: json file name
    '''
    df = pd.DataFrame(data)
    df.columns = ['Group', 'Number', 'String']
    # json file name
    df.to_json(file_name, orient='records', indent=4)
    df_print(df)


def main(argv):
    json_file_name = 'Export_DataFrame.json'
    if len(argv) > 0:
        json_file_name = argv[0]
    # web url
    url = "https://www.nytimes.com/crosswords/game/mini"
    scrap_url(url, json_file_name)


if __name__ == "__main__":
    main(sys.argv[1:])


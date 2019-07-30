#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
"""
page = requests.get('http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2019/start/1')
url = "http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2019/start/1"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
attrs = {'class': 'oddrow player-10-33900'}
soup.find_all('tr', attrs)
row = soup.find('tr', attrs)
newAttrs = {'class': 'colhead'}
header = soup.find('tr', newAttrs)
columns = [col.get_text() for col in header.find_all('td')]
final_df = pd.DataFrame(columns=columns)
players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})
players = soup.find_all('tr', attrs = {'class':re.compile('row player-10-')})
for player in players:
    stats = [stat.get_text() for stat in player.find_all('td')]
    print(stats)
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    final_df = pd.concat([final_df, temp_df], ignore_index=True)
"""
def pitching_leaders(category, year=None):
    if category == 'season':
        url = ("http://www.espn.com/mlb/history/leaders/_/breakdown/season/type/pitching/year/{}/sort/era").format(year)
    elif category == 'career':
        url = "http://www.espn.com/mlb/history/leaders/_/type/pitching/sort/ERA"
    else:
        url = "http://www.espn.com/mlb/history/leaders/_/type/pitching/breakdown/singlepost/sort/ERA"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    attrs = {'class':'colhead'}
    header = soup.find('tr', attrs)
    columns = [col.get_text() for col in header.find_all('td')]
    players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})
    results = [columns]
    for player in players:
        stats = batting_stats(player)
        results += [stats]
    return results

def batting_leaders(category, year=None):
    if category == 'season':
        url = ("http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/{}/start/1").format(year)
    elif category == 'career':
        url = "http://www.espn.com/mlb/history/leaders"
    else:
        url = "http://www.espn.com/mlb/history/leaders/_/breakdown/singlepost"
    page= requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    attrs = {'class':'colhead'}
    header = soup.find('tr', attrs)
    columns = [col.get_text() for col in header.find_all('td')]
    players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})
    results = [columns]
    for player in players:
        stats = batting_stats(player)
        results += [stats]
    return results

def make_df(stats):
    columns = stats[0][1:]
    players = stats[1:]
    df = pd.DataFrame(columns=columns)
    df.index = df.index + 1
    for player in players:
        temp_df = pd.DataFrame(player[1:]).transpose()
        temp_df.columns = columns
        df = pd.concat([df, temp_df], ignore_index=True)
    return df






def batting_stats(player):
    stats = [stat.get_text() for stat in player.find_all('td')]
    return stats



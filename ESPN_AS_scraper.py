#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import re
import requests
from bs4 import BeautifulSoup


def games():
    page = requests.get('http://www.espn.com/mlb/allstargame/history')
    soup = BeautifulSoup(page.text, 'html.parser')
    attrs = {'class': 'colhead'}
    header = soup.find('tr', attrs)
    columns = [col.get_text() for col in header.find_all('td')]
    newAttrs = {'class': re.compile('row')}
    games = soup.find_all('tr', newAttrs)
    scores = [columns]
    for game in games:
        stats = [game.get_text() for game in game.find_all('td')]
        scores += [stats]
    return scores

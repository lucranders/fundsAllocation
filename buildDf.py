# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 21:16:51 2021

@author: 55119
"""

import urllib.request
from bs4 import BeautifulSoup
from numpy import e
import pandas as pd

def getInfo_(fii_):

    try:
        response = urllib.request.urlopen('https://www.infomoney.com.br/cotacoes/fundos-imobiliarios-' + fii_)
    except:
        response = urllib.request.urlopen('https://www.infomoney.com.br/cotacoes/fundo-imobiliario-' + fii_)

    html_doc = response.read()
    soup = BeautifulSoup(html_doc , 'html.parser')

    try:
        pvp_ = float(soup.find("td", text="P/VP").find_next_sibling("td").text.strip().replace(',','.'))
    except:
        pvp_ = 0
    try:
        open_= float(soup.find("td", text="Abertura").find_next_sibling("td").text.strip().replace(',','.'))
    except:
        try:
            open_ = float(soup.find("td", text="Fechamento anterior").find_next_sibling("td").text.strip().replace(',','.'))
        except:
            open_ = 0

    try:
        yield_ = float(soup.find("td", text="Yield 12M").find_next_sibling("td").text.strip().replace(',','.').replace('%',''))
    except:
        yield_ = 0

    print(fii_ + ': done')

    return([fii_,pvp_,open_,yield_])

def gather_(list_):

    infos_ = []
    for fii_ in list_:
        infos_.append(getInfo_(fii_))
    
    newDf_ = pd.DataFrame(infos_)
    
    return newDf_



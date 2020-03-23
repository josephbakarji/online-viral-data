from bs4 import BeautifulSoup
import re
import urllib3
from random import randrange
import json
from random import randint
from tabulate import tabulate
from datetime import datetime
import numpy as np
import pdb
import sys
from __init__ import *

def scrapeWorldometer():
    # Get html file using urllib
    http = urllib3.PoolManager()
    homepage = "https://www.worldometers.info/coronavirus/"
    home_html3 = http.request('GET', homepage)
    
    # Parse with beautifulsoup
    soup = BeautifulSoup(home_html3.data, "html.parser")
    
    table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="main_table_countries_today") 
    rows = table.find_all(lambda tag: tag.name=='tr')

    # Get headers (automatically) - NOT USED 
    header = rows[0].find_all(lambda tag: tag.name=='th')
    header_list = []
    for h in header:
       header_list.append( h.renderContents().strip() )

    # Parse main table 
    crows = table.find_all(lambda tag: tag.name=='td')
    embeddings = ["a", "span", "strong"]
    all_cols = [[] for i in range(len(MAINTABLE_HEAD))]
    for i, row in enumerate(rows):
        tds = row.find_all("td")
        col = []
        for jdx, elem in enumerate(tds):
            found_emb = False 
            for emb in embeddings:
                if elem.find(emb) is not None:
                    text = elem.find(emb).renderContents().strip()
                    found_emb = True 
            if not found_emb:
                text = elem.renderContents().strip()
            all_cols[jdx].append( text.decode("utf-8") )

    # Transpose
    all_rows = map(list, zip(*all_cols))

    # convert strings to numbers
    new_all_rows = []
    for idx, row in enumerate(all_rows):
        new_row = []
        for jdx, elem in enumerate(row):
            if jdx != 0:
                if elem == '':
                    elem = 0
                elif ',' in elem:
                    elem = int(''.join(elem.split(',')))
                elif '.' in elem:
                    elem = float(elem)
                else:
                    elem = int(elem)
            new_row.append(elem)
        new_all_rows.append(new_row)



    # Save the data

    ## IF file is empty use this line
    # data = {str(datetime.now()): new_all_rows}

    with open(SAVEFILE) as jsonfile:
        data = json.load(jsonfile)
    data[str(datetime.now())] = new_all_rows
    with open(SAVEFILE, 'w') as jsonfile:
        json.dump(data, jsonfile)

if __name__ == "__main__":
    scrapeWorldometer()

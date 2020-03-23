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
import matplotlib.pyplot as plt

# Will input them manually 


class DisplayData: 
    def __init__(self, filename):
        self.filename = filename
        self.data = self.getData()

    def getData(self):
        with open(self.filename) as jsonfile:
            data = json.load(jsonfile)
        return data

    def getTimes(self, verbose=False):
        time_list = [time for time in self.data.keys()]
        time_list.sort()
        if verbose:
            for t in time_list:
                print(t)
        return time_list

    def printLastTable(self):
        times = self.getTimes()
        print('Last Updated: %s'%(times[-1]))
        print(tabulate(self.data[times[-1]], headers=MAINTABLE_HEAD)) # Include that in data maybe separate json file (?)

    def getCountryData(self, req_country):
        time_list = self.getTimes()
        country_data = []
        for time in time_list:
            for country in self.data[time]:
                if country[0] == req_country:
                    country_data.append(country)
                    found_country = True

            if found_country == False:
                raise Exception("Country doesn't exist")

        country_data_t = list(map(list, zip(*country_data)))
        return country_data_t

    def plotCountryData(self, country_data, req_feature):
        # req_feature is one of ['Total Cases', 'New Cases', 'Total Deaths', 'New Deaths', 'Total Recovered', 'Active Cases','Serious/Critical', 'Tot Cases/1M']
        times = self.getTimes()
        datenum = self.dateToNumber(times)
        #datenum = [i for i in range(len(times))] # for testing
        for idx, feature in enumerate(MAINTABLE_HEAD):
            if req_feature == feature:
                feat_idx = idx
                break

        # plot
        fig = plt.figure()
        plt.plot(datenum, country_data[feat_idx], '-o') 
        plt.show()
        
    def dateToNumber(self, times):
        numberdates = []
        for date in times:
            number = float(''.join(re.split(r'[-:\s]\s*', date)))
            numberdates.append( int(number/100) )
        return numberdates



if __name__ == "__main__":
    D = DisplayData(SAVEFILE)

    if len(sys.argv) >= 2:
        if sys.argv[1] == 'plot_country':
            country_data = D.getCountryData(sys.argv[2])
            print(sys.argv)
            if len(sys.argv) <= 3:
                D.plotCountryData(country_data, "Total Cases")
            else:
                D.plotCountryData(country_data, sys.argv[3])
        elif sys.argv[1] == 'latest':
            D.printLastTable() 
        elif sys.argv[1] == 'data_times':
            D.getTimes(verbose=True)
        else:
            raise Exception("Option "+ sys.argv[1:] + " Unavailable ")
    else:
        D.printLastTable() 



## Description ##

This code scrapes coronavirus data and plots it. Data is to be used as part of financial, social, viral spreading models etc. 

## Usage ##

* Change the `MAINDIR` variable in `__init__.py` to match your main directory
* Install crontab using `sudo -H pip install python-crontab`.
* Make sure all the packages are installed using `sudo -H pip install ...` so that crontab can access them
* Run `python scheduler.py time_period` where `time_period` is in minutes 

### Examples ###

* `python analyze.py plot_country USA "New Cases"` plots new cases in the US
* `python analyze.py plot_country Lebanon` plots total cases in Lebanon (default argument) 
* `python analyze.py latest` print latest data in table format (on terminal) - also works without arguments
* `python scraper.py` aggregates data from website at the moment

## TO DO ##

* Save U.S data from [worldometers.info](https://www.worldometers.info/coronavirus/country/us/).
* Fix plotting axes: time has to be displayed as (Day Month) like: 20 March.
* Specify time period and make sure data points are regular.
* Add previous data from links.
* Explore using other sources.

...

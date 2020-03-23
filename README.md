## Description ##

This code scrapes coronavirus data and plots it. Data could is to be used as part of financial, social, viral spreading models etc. 

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

* Save US data in [Worldometer](https://www.worldometers.info/coronavirus/us/).
* Fix plotting axes: time needs to be displayed as (Day Month) like: March 20.
* Specify time period and make sure data points are regular.

...
## NBA Stats Scraper

This is an ongoing project to make it easy to gather NBA player and team data. The resulting data can be exported as a csv or as a pandas dataframe with more options to come. The resulting data can be used to team analysis or for third party content creation.

For more info on how to contribute to NBA stats scraper please see CONTRIBUTING.md, remember to follow the Code of Conduct.  If you are looking for good first issues there are several in the open issues tab. If you have any questions please feel free to open an issue.


## Basic Overview

The layout of the program is very simple. The entry point is in `__init__.py__` and the GUI is initialized from `NBAStatsScraper.py` 

The primary UI logic resides in `MainForm.py` and the data layer and requests are funneled through `NBAData.py` 
For a full rundown of the endpoints exposed by the API wrapper please see https://github.com/swar/nba_api/tree/master/docs for further info.
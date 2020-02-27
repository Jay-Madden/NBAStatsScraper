#!/bin/bash

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
brew install nba_api
brew install npyscreen
python3 __init__.py

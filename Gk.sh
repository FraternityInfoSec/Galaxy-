#!/bin/bash

command -v curl > /dev/null 2>&1 || {  echo >&2 "we require curl but it is not installed. \n installing it.."; apt install curl -y; }

command -v python > /dev/null 2>&1 || {  echo >&2 "we require python but it is not installed. \n installing it.."; apt install python -y; }

command -v pip > /dev/null 2>&1 || {  echo >&2 "we require pip but it is not installed. \n installing it.."; curl https:bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py ; }

command -v toilet > /dev/null 2>&1 || {  echo >&2 "we require toilet package but it is not installed. \n installing it.."; apt install toilet -y; }

command -v fish > /dev/ull 2>&1 || { echo >&2 "we require fish but it isn't important and not installed it is required in case if you forget coding for installation later. \installing it.."; apt install fish -y;} 

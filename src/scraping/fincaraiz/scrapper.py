import urllib
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from urllib.parse import urljoin
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException,  TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

import pymongo
import matplotlib.pyplot as plt
import seaborn as sns

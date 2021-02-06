# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 14:15:02 2017

@author: Bill
"""

import pandas as pd 
import urllib2

url= 'http://www.tse.com.tw/ch/trading/fund/BFI82U/BFI82U.php'

df= pd.read_html(url)

print df
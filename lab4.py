#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:13:51 2022

@author: skyejung
"""

'''
YAHOO EXAMPLE
'''

import json
import requests
import pandas

stock = input() # this asks the user for a stock/ticker or something
stock

# step 1 set up url where is this endpoint that I want
# base url https://query1.finance.yahoo.com/v7/finance/quote
urlQuote = 'https://query1.finance.yahoo.com/v7/finance/quote'
querystring = {"symbols": stock}
print(querystring)

header_var ={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 1
    0_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.request("GET",urlQuote, headers=header_var,params=querystring)
# response.content

stock_json = response.json()
# stock_json

stock_json['quoteResponse']['result'][0]['longName']


url2="https://query1.finance.yahoo.com/v10/finance/quoteSummary/"
query_str = {"symbol": stock, "modules":"defaultKeyStatistics"}

response = requests.request("GET",url2, headers=header_var,params=query_str)

stock_json = response.json()

stock_json


# !pip install yfinance

import yfinance as yf
import utils

stock = input()
stock
data = yf.Ticker(stock)

data

data.balance_sheet

url = "https://query1.finance.yahoo.com/v7/finance/quote"

user_agent_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

headers=user_agent_headers
headers
querystring = querystring = {"symbols":stock}
#querystring = querystring = {"symbols":"msft,goog"}


querystring

response = requests.request("GET",url, headers=headers,params = querystring)

response.content

stock_json = response.json()
stock_json



"""
Lab 4
"""

# step 1 set up url where is this endpoint that I want
# base url https://query1.finance.yahoo.com/v7/finance/quote
# https://query1.finance.yahoo.com/v11/finance/quoteSummary/{symbol}
stock='ie'
urlQuote = 'https://query1.finance.yahoo.com/v7/finance/quote'
querystring = {"symbols": stock}
print(querystring)

header_var ={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.request("GET",urlQuote, headers=header_var,params=querystring)
# response.content

stock_json = response.json()

# name ticker
name_ticker = stock_json['quoteResponse']['result'][0]['symbol']

# full name of the stock
full_name = stock_json['quoteResponse']['result'][0]['longName']



## financialData module

urlQuote2 = 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/ie?modules=financialData'
querystring2 = {"symbols": stock}
print(querystring2)

header_var2 ={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response2 = requests.request("GET",urlQuote2, headers=header_var2,params=querystring2)
# response.content

stock_json2 = response2.json()
stock_json2

# current price
current_price = stock_json2['quoteSummary']['result'][0]['financialData']['currentPrice']

# target mean price
target_mean_price = stock_json2['quoteSummary']['result'][0]['financialData']['targetMeanPrice']

# cash on hand
cash_on_hand = stock_json2['quoteSummary']['result'][0]['financialData']['totalCash']

# profit margins
profit_margins = stock_json2['quoteSummary']['result'][0]['financialData']['profitMargins']

lab4 = {'Name Ticker':name_ticker, 'Full Name of Stock':full_name,'Current Price':current_price,'Target Mean Price':target_mean_price, 'Cash on Hand':cash_on_hand, 'Profit Margins':profit_margins}

lab4

writeToJSONFile('/Users/skyejung/Desktop/ds 2002','lab4',lab4)

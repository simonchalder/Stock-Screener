# Imports

from dotenv import load_dotenv
import requests

# Class Definition

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        
        # API Calls

        self.overview = requests.get('https://www.alphavantage.co/query?function=OVERVIEW&symbol={0}&interval=5min&apikey=KEY'.format(symbol))
        self.balance = requests.get('https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={0}&apikey=KEY'.format(symbol))
        self.cash = requests.get('https://www.alphavantage.co/query?function=CASH_FLOW&symbol={0}&apikey=KEY'.format(symbol))
        self.income = requests.get('https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={0}&apikey=KEY'.format(symbol))

        # Class variable assignment

        self.name = self.overview.json()['Name']
        self.cap = self.overview.json()['MarketCapitalization']
        self.balance.json()['annualReports'][0]['totalLiabilities']
        self.peRatio = self.overview.json()['PERatio']
        self.eps = self.overview.json()['EPS']
        self.cash = self.cash.json()['annualReports'][0]['operatingCashflow']
        self.borrowings = self.balance.json()['annualReports'][0]['currentDebt']
        self.shareholder_equity = self.balance.json()['annualReports'][0]['totalShareholderEquity']
        self.annual_profits = self.income.json()['annualReports'][0]['comprehensiveIncomeNetOfTax']

# Test code

code = input("Enter stock code").upper()

newStock = Stock(code)

print(newStock.annual_profits)

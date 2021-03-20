from dotenv import load_dotenv
import requests
import time

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        
        # API Calls

        self.overview = requests.get('https://www.alphavantage.co/query?function=OVERVIEW&symbol={0}&interval=5min&apikey=KEY'.format(symbol))
        time.sleep(1)
        self.balance = requests.get('https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={0}&apikey=KEY'.format(symbol))
        time.sleep(1)
        self.cash = requests.get('https://www.alphavantage.co/query?function=CASH_FLOW&symbol={0}&apikey=KEY'.format(symbol))
        time.sleep(1)
        self.income = requests.get('https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={0}&apikey=KEY'.format(symbol))
        time.sleep(1)

        # Class variable assignment

        self.name = self.overview.json()['Name']
        self.cap = int(self.overview.json()['MarketCapitalization'])
        self.debt = int(self.balance.json()['annualReports'][0]['totalLiabilities'])
        self.peRatio = float(self.overview.json()['PERatio'])
        self.eps = float(self.overview.json()['EPS'])
        self.cash = int(self.cash.json()['annualReports'][0]['operatingCashflow'])
        self.borrowings = int(self.balance.json()['annualReports'][0]['currentDebt'])
        self.shareholder_equity = int(self.balance.json()['annualReports'][0]['totalShareholderEquity'])
        self.annual_profits = int(self.income.json()['annualReports'][0]['comprehensiveIncomeNetOfTax'])
        self.score = []
        
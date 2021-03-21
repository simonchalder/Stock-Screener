from dotenv import load_dotenv
import requests
import time

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        
        # API Calls
        try:
            self.overview = requests.get('https://www.alphavantage.co/query?function=OVERVIEW&symbol={0}&interval=5min&apikey=KEY'.format(symbol))
        except:
            print(self.overview.status_code)

        try:
            self.balance = requests.get('https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={0}&apikey=KEY'.format(symbol))
        except:
            print(self.overview.status_code)

        try:
            self.cash_flow = requests.get('https://www.alphavantage.co/query?function=CASH_FLOW&symbol={0}&apikey=KEY'.format(symbol))
        except:
            print(self.overview.status_code)

        try:
            self.income = requests.get('https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={0}&apikey=KEY'.format(symbol))
        except:
            print(self.overview.status_code)

        # Class variable assignment

        self.name = self.overview.json()['Name']
        self.cap = int(self.overview.json()['MarketCapitalization'])
        self.debt = int(self.balance.json()['annualReports'][0]['totalLiabilities'])
        self.peRatio = float(self.overview.json()['PERatio'])
        self.eps = float(self.overview.json()['EPS'])
        self.cash = int(self.cash_flow.json()['annualReports'][0]['operatingCashflow'])
        try:
            self.borrowings = int(self.balance.json()['annualReports'][0]['currentDebt'])
        except:
            self.borrowings = 'None'
        self.shareholder_equity = int(self.balance.json()['annualReports'][0]['totalShareholderEquity'])
        self.annual_profits = int(self.income.json()['annualReports'][0]['comprehensiveIncomeNetOfTax'])
        self.profit_margin = float(self.overview.json()['ProfitMargin'])
        self.total_assets = int(self.balance.json()['annualReports'][0]['totalAssets'])
        self.total_liabilities = int(self.balance.json()['annualReports'][0]['totalLiabilities'])
        self.score = []
        
    def assessStock(self):
        if self.cap <= 50000000 and self.cap < 950000000: # Market Cap
            self.score.append(1)
        else:
            self.score.append(0)

        if self.debt < (self.annual_profits * 3): # Check debt is no more than 3 times annual profits
            self.score.append(1)
        else:
            self.score.append(0) 

        if self.profit_margin > 10: # Check profit margin above 10%
            self.score.append(1)
        else:
            self.score.append(0)

        if self.peRatio >= 12 and self.peRatio <=20: # Check PE ratio between 12 and 20
            self.score.append(1)
        else:
            self.score.append(0)

        if (self.borrowings - self.cash) / self.shareholder_equity >= 25 and (self.borrowings - self.cash) / self.shareholder_equity <= 50:
            self.score.append(1) # Check gearing ratio is between 25 and 50 %
        else:
            self.score.append(0)

        if self.cap < (self.annual_profits * 15): # Billionaire test - is mcap less than 15 times annual profits?
            self.score.append(1)
        else:
            self.score.append(0)

        if self.total_liabilities / self.total_assets >= 50 and self.total_liabilities / self.total_assets <= 60:
            self.score.append(1) # Debt ratio - between 50 and 60 %
        else:
            self.score.append(0)
        


        
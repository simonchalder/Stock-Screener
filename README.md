# Stock-Screener

Developer: Simon Chalder

Project Start Date: March 2021

GitHub Url: https://github.com/simonchalder/Image-Converter

Requests library Page: https://2.python-requests.org/en/master/

All data taken from the Alpha Vantage API: https://www.alphavantage.co/documentation/

Stock Screener is a desktop GUI application for screening a particular stock against logical criteria to determine if the stock is worthy of further investigation

The criteria used in this application are taken from Robbie Burns book 'The Naked Trader: How Anyone Can Make Money Trading Shares'

***DISCLAIMER***

This is a practice application. The developer is not a financial advisor and any data obtained through this app should NOT be construed as financial advice or acted upon.

***________________***

The app, still under development is written in Python using the requests library for API calls and Tkinter for the GUI

***LIMITATIONS***

The Alpha Vantage API allows only 5 calls per minute. Currently the app makes calls to 4 endpoints to retrieve the necessary data. This means the app can currently only retrieve new data once per minute. The API does not seem to recognise international stock codes and so is limited to the US Dow Jones and S&P500. These seem to be limitations of the free API.

***Issues / still to-do:***

Integration of further financial measurments

Logic implementation

GUI improvements

Testing
# Imports

import stock

# Test code

code = input("Enter stock code:  ").upper()

newStock = stock.Stock(code)

print(newStock.debt)



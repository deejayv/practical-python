# report.py
#
# # Exercise 2.4: A list of tuples (Read file into a list of tuples x[(a,b),(c,d),(e,f)])

# import csv

# def read_portfolio(filename):
    
    # portfolio = []
    
    # with open(filename, 'rt') as f:
        # rows = csv.reader(f)
        # headers = next(rows)
        
        # for row in rows:
            # holding = (row[0], int(row[1]), float(row[2]))
            # portfolio.append(holding)
            
    # return portfolio
    
# # Exercise 2.5: List of dictionaries (Read file into a list of dictionaries x[{a:b},{c:d},{e:f}]

# import csv

# def read_portfolio(filename):
    
    # portfolio = []
    
    # with open(filename, 'rt') as f:
        # rows = csv.reader(f)
        # headers = next(rows)
        
        # for row in rows:
            # holding = {
                # 'name'   : row[0],
                # 'shares' : int(row[1]),
                # 'price'  : float(row[2])
                # }
            # portfolio.append(holding)
            
    # return portfolio
    
# # Exercise 2.6 : Dictionaries as a container

# import csv

# def read_prices(filename):
    
    # stock_prices = {}
    
    # with open(filename, 'rt') as f:
        # rows = csv.reader(f)
        
        # for row in rows:
            # try:
                # stock_prices[row[0]] = float(row[1])
            # except IndexError:
                # print("Couldn't parse", row)
            
    # return stock_prices

# Exercise 2.7: Compute gain/loss. Take the list of stocks and the dictionary of prices and compute the current value of the portfolio with the gain/loss

import csv

def read_prices(filename):
    
    stock_prices = {}
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        
        for row in rows:
            try:
                stock_prices[row[0]] = float(row[1])
            except IndexError:
                print("Couldn't parse", row)
            
    return stock_prices
    
def read_portfolio(filename):
    
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            holding = {
                'name'   : row[0],
                'shares' : int(row[1]),
                'price'  : float(row[2])
                }          
            portfolio.append(holding)
            
        # for row in rows:
            # portfolio[row]['price'] = prices[portfolio[row]['name']] || Still can't figure why this not working!!
            
    return portfolio

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0

for s in portfolio:
    total_cost += s['shares'] * s['price']
    
print('\nTotal cost of portfolio is:', total_cost)
    
total_value = 0.0

for s in portfolio:
    total_value += s['shares'] * prices[s['name']]
    
print('\nCurrent value of portfolio is:', total_value)

gain = total_value - total_cost

if total_value - total_cost < 0:
    print(f"\nLoss is {gain: .2f}")
else:
    print(f"\nGain is {gain: .2f}")
    
# # report.py
# #
# # Solution

# import csv

# def read_portfolio(filename):
    # '''
    # Read a stock portfolio file into a list of dictionaries with keys
    # name, shares, and price.
    # '''
    
    # portfolio = []
    # with open(filename) as f:
        # rows    = csv.reader(f)
        # headers = next(rows)
        
        # for row in rows:
            # stock = {
                # 'name'   : row[0],
                # 'shares' : int(row[1]),
                # 'price'  : float(row[2])
            # }
            # portfolio.append(stock)
            
    # return portfolio
    
# def read_prices(filename):
    # '''
    # Read a CSV file of price date in a dict mapping names to prices.
    # '''
    # prices = {}
    # with open(filename) as f:
        # rows = csv.reader(f)
        # for row in rows:
            # try:
                # prices[row[0]] = float(row[1])
            # except IndexError:
                # pass
                
    # return prices

# portfolio = read_portfolio('Data/portfolio.csv')
# prices    = read_prices('Data/prices.csv')

# # Calculate the total cost of the portfolio

# total_cost = 0.0

# for s in portfolio:
    # total_cost += s['shares'] * s['price']
    
# print('Total cost', total_cost)

# # Compute the current value of the portfolio

# total_value = 0.0

# for s in portfolio:
    # total_value += s['shares'] * prices[s['name']]
    
# print('Current value', total_value)
# print('Gain', total_value - total_cost)

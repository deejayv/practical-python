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

# # Exercise 2.7: Compute gain/loss. Take the list of stocks and the dictionary of prices and compute the current value of the portfolio with the gain/loss

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
            
        # # for row in rows:
            # # portfolio[row]['price'] = prices[portfolio[row]['name']] || Still can't figure why this not working!!
            
    # return portfolio

# portfolio = read_portfolio('Data/portfolio.csv')
# prices = read_prices('Data/prices.csv')

# total_cost = 0.0

# for s in portfolio:
    # total_cost += s['shares'] * s['price']
    
# print('\nTotal cost of portfolio is:', total_cost)
    
# total_value = 0.0

# for s in portfolio:
    # total_value += s['shares'] * prices[s['name']]
    
# print('\nCurrent value of portfolio is:', total_value)

# gain = total_value - total_cost

# if total_value - total_cost < 0:
    # print(f"\nLoss is {gain: .2f}")
# else:
    # print(f"\nGain is {gain: .2f}")


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


# # Exercise 2.9 : Write a function make_report() that takes a list of stocks and dictionary of prices as input and returns a list of tuples

# import csv

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

# def make_report(portfolio, prices):
    
    # portfolio = read_portfolio('Data/portfolio.csv')
    # prices    = read_prices('Data/prices.csv')
    
    # holding = []
    
    # for s in portfolio:
        # stock = (s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price'])
        # holding.append(stock)
        
    # return holding

# portfolio = read_portfolio('Data/portfolio.csv')
# prices    = read_prices('Data/prices.csv')

# report = make_report(portfolio, prices)

# for r in report:
    # print(r)
    

# # Exercise 2.10 : Take the output of make_report() function and print a nicely formatted table

# import csv

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

# def make_report(portfolio, prices):
    
    # portfolio = read_portfolio('Data/portfolio.csv')
    # prices    = read_prices('Data/prices.csv')
    
    # holding = []
    
    # for s in portfolio:
        # stock = (s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price'])
        # holding.append(stock)
        
    # return holding

# portfolio = read_portfolio('Data/portfolio.csv')
# prices    = read_prices('Data/prices.csv')

# report = make_report(portfolio, prices)

# for r in report:
    # print('%10s %10d %10.2f %10.2f' % r)
    

# # Exercise 2.11 : Add some formatted headers (My take)

# import csv

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

# def make_report(portfolio, prices):
    
    # holding = []
    
    # for s in portfolio:
        # stock = (s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price'])
        # holding.append(stock)
        
    # return holding

# print(f'\n{'Name': >10}{'Shares': >11}{'Price': >11}{'Change': >11}')
# print(f'{'----------': >10}{'----------': >11}{'----------': >11}{'----------': >11}')

# portfolio = read_portfolio('Data/portfolio.csv')
# prices    = read_prices('Data/prices.csv')

# report = make_report(portfolio, prices)

# for r in report:
    # print('%10s %10d %10s %10.2f' % r)


# # Solution 2.11

# import csv

# def read_portfolio(filename):
    # '''
    # Read a stock portfolio file into a list of dictionaries with keys
    # name, shares, and price.
    # '''
    # portfolio = []
    # with open(filename) as f:
        # rows = csv.reader(f)
        # headers = next(rows)

        # for row in rows:
            # stock = {
                 # 'name'   : row[0],
                 # 'shares' : int(row[1]),
                 # 'price'   : float(row[2])
            # }
            # portfolio.append(stock)

    # return portfolio

# def read_prices(filename):
    # '''
    # Read a CSV file of price data into a dict mapping names to prices.
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

# def make_report_data(portfolio, prices):
    # '''
    # Make a list of (name, shares, price, change) tuples given a portfolio list
    # and prices dictionary.
    # '''
    # rows = []
    # for stock in portfolio:
        # current_price = prices[stock['name']]
        # change = current_price - stock['price']
        # summary = (stock['name'], stock['shares'], current_price, change)
        # rows.append(summary)
    # return rows
        
# # Read data files and create the report data        

# portfolio = read_portfolio('Data/portfolio.csv')
# prices = read_prices('Data/prices.csv')

# # Generate the report data

# report = make_report_data(portfolio, prices)

# # Output the report
# headers = ('Name', 'Shares', 'Price', 'Change')
# print('%10s %10s %10s %10s' % headers)
# print(('-' * 10 + ' ') * len(headers))
# for row in report:
    # print('%10s %10d %10.2f %10.2f' % row)

    
# # Exercise 2.12

# import csv

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

# def make_report(portfolio, prices):
    
    # holding = []
    
    # for s in portfolio:
        # stock = (s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price'])
        # holding.append(stock)
        
    # return holding

# print(f'\n{'Name': >10}{'Shares': >11}{'Price': >11}{'Change': >11}')
# print(f'{'----------': >10}{'----------': >11}{'----------': >11}{'----------': >11}')

# portfolio = read_portfolio('Data/portfolio.csv')
# prices    = read_prices('Data/prices.csv')

# report = make_report(portfolio, prices)

# for r in report:
    # print('%10s %10d %10s %10.2f' % (r[0], r[1], '$%.2f' % r[2], r[3])) # Co-pilot helped to write this part


# # Exercise 2.16b: Using the zip() function

# import csv
# import sys

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

# def read_portfolio(filename):
    # '''
    # Read a stock portfolio file into a list of dictionaries with keys
    # name, shares, and price.
    # '''
    # portfolio = []
    # with open(filename) as f:
        # rows    = csv.reader(f)
        # headers = next(rows)
        
        # for row_no, row in enumerate(rows, start=1):
            # record = dict(zip(headers, row))
            
            # try:
                # record['shares'] = int(record['shares'])
                # record['price'] = float(record['price'])
                # portfolio.append(record)
            # except ValueError:
                # pass
                
    # return portfolio

# def make_report(portfolio, prices):
    
    # holding = []
    
    # for s in portfolio:
        # stock = (s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price'])
        # holding.append(stock)
        
    # return holding

# print(f'\n{'Name': >10}{'Shares': >11}{'Price': >11}{'Change': >11}')
# print(f'{'----------': >10}{'----------': >11}{'----------': >11}{'----------': >11}')

# if len(sys.argv) == 2:
    # filename = sys.argv[1]
# else:
    # filename = 'Data/portfolio.csv'

# portfolio = read_portfolio(filename)
# prices    = read_prices('Data/prices.csv')

# report = make_report(portfolio, prices)

# for r in report:
    # print('%10s %10d %10s %10.2f' % (r[0], r[1], '$%.2f' % r[2], r[3])) # Co-pilot helped to write this part


# # Exercise 3.1

# import csv

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

# def read_portfolio(filename):
    # '''
    # Read a stock portfolio file into a list of dictionaries with keys
    # name, shares, and price.
    # '''
    # portfolio = []
    # with open(filename) as f:
        # rows    = csv.reader(f)
        # headers = next(rows)
        
        # for row_no, row in enumerate(rows, start=1):
            # record = dict(zip(headers, row))
            
            # try:
                # record['shares'] = int(record['shares'])
                # record['price'] = float(record['price'])
                # portfolio.append(record)
            # except ValueError:
                # pass
                
    # return portfolio

# def make_report_data(portfolio, prices):
    
    # holding = []
    
    # for s in portfolio:
        # stock = (s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price'])
        # holding.append(stock)
        
    # return holding

# def print_report(reportdata):
    # '''
    # This function prints a tabulated report of any data inputted as reportdata
    # '''
    # headers = ('\nName', 'Shares', 'Price', 'Change')
    # print('%10s %10s %10s %10s' % headers)
    # print(('-' * 10 + ' ') * len(headers))
    
    # portfolio = read_portfolio(reportdata)
    # prices    = read_prices('Data/prices.csv')
        
    # report = make_report_data(portfolio, prices)
    
    # for r in report:
        # print('%10s %10d %10s %10.2f' % (r[0], r[1], '$%.2f' % r[2], r[3]))


# # Exercise 3.2

# import csv
# import sys

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

# def read_portfolio(filename):
    # '''
    # Read a stock portfolio file into a list of dictionaries with keys
    # name, shares, and price.
    # '''
    # portfolio = []
    # with open(filename) as f:
        # rows    = csv.reader(f)
        # headers = next(rows)
        
        # for row_no, row in enumerate(rows, start=1):
            # record = dict(zip(headers, row))
            
            # try:
                # record['shares'] = int(record['shares'])
                # record['price'] = float(record['price'])
                # portfolio.append(record)
            # except ValueError:
                # pass
                
    # return portfolio

# def make_report_data(portfolio, prices):
    
    # holding = []
    
    # for s in portfolio:
        # stock = (s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price'])
        # holding.append(stock)
        
    # return holding

# def print_report(reportdata):
    # '''
    # This function prints a tabulated report of any data inputted as reportdata
    # '''
    # headers = ('Name', 'Shares', 'Price', 'Change')
    # print('%10s %10s %10s %10s' % headers)
    # print(('-' * 10 + ' ') * len(headers))
    
    # for row in reportdata:
        # print('%10s %10d %10.2f %10.2f' % row)

# def portfolio_report(portfolio_filename, prices_filename):
    
    # portfolio = read_portfolio(portfolio_filename)
    # prices    = read_prices(prices_filename)
        
    # report = make_report_data(portfolio, prices)

    # print_report(report)        

# if len(sys.argv) == 3:
    # portfolio_filename = sys.argv[1]
    # prices_filename = sys.argv[2]
# else:
    # portfolio_filename = 'Data/portfolio.csv'
    # prices_filename = 'Data/prices.csv'

# portfolio_report(portfolio_filename, prices_filename)

# Exercise 3.12: Using library module

import sys
import fileparse

def read_prices(filename):
    '''
    Use parse_csv module to read prices
    '''
    return dict(fileparse.parse_csv(filename, has_headers=False, types=[str,float]))

def read_portfolio(filename):
    '''
    Use parse_csv module to read portfolio
    '''
    return fileparse.parse_csv(filename, types=[str, int, float], select=['name', 'shares', 'price'])

def make_report_data(portfolio, prices):
    
    holding = []
    
    for s in portfolio:
        stock = (s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price'])
        holding.append(stock)
        
    return holding

def print_report(reportdata):
    '''
    This function prints a tabulated report of any data inputted as reportdata
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfolio_filename, prices_filename):
    
    portfolio = read_portfolio(portfolio_filename)
    prices    = read_prices(prices_filename)
        
    report = make_report_data(portfolio, prices)

    print_report(report)
    
if len(sys.argv) == 3:
    portfolio_filename = sys.argv[1]
    prices_filename = sys.argv[2]
else:
    portfolio_filename = 'Data/portfolio.csv'
    prices_filename = 'Data/prices.csv'

portfolio_report(portfolio_filename, prices_filename)

# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
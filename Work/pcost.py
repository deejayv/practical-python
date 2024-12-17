# # pcost.py
# #
# # My take
# #
# # Exercise 1.27 (Write a program that opens the file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio)

# portfolio_open = open('Data/portfolio.csv', 'rt')

# headers = next(portfolio_open)

# # print(headers)

# total_per_stock = 0

# for line in portfolio_open:
    # row = line.split(',')
    # # print(row)
    
    # total_per_stock = total_per_stock + (int(row[1]) * float(row[2]))
    
# print(f"\nTotal cost is {total_per_stock}\n")

# portfolio_open.close()


# # Solution

# total_cost = 0.0

# with open('Data/portfolio.csv', 'rt') as f:
    # headers = next(f)
    
    # for line in f:
        # row = line.split(',')
        # nshares = int(row[1])
        # price = float(row[2])
        # total_cost += nshares * price
        
# print('Total cost', total_cost)

# # pcost.py
# #
# # Exercise 1.30 (Turning a script into a function)

# def portfolio_cost(filename):
    
    # 'This function calculates the total cost of the portfolio in the file'
    
    # total_cost = 0.0
    
    # with open(filename, 'rt') as f:
        
        # headers = next(f)
        
        # for line in f:
            # row = line.split(',')
            # nshares = int(row[1])
            # price = float(row[2])
            # total_cost += nshares * price
            
    # return total_cost
    
# cost = portfolio_cost('Data/portfolio.csv')
# print('Total cost:', cost)

# # pcost.py
# #
# # Exercise 1.31: Errorhandling (Modify the pcost.py program to catch the exception, print a warning message, and continue processing the rest of the file)

# def portfolio_cost(filename):
    
    # 'This function calculates the total cost of the portfolio in the file'
    
    # total_cost = 0.0
    
    # with open(filename, 'rt') as f:
        
        # headers = next(f)
        
        # for line in f:
            # row = line.split(',')
            
            # try:
                # nshares = int(row[1])
                # price = float(row[2])
                # total_cost += nshares * price
            # except ValueError:
                # print("Couldn't parse", line)
            
    # return total_cost
    
# cost = portfolio_cost('Data/portfolio.csv')
# print('Total cost:', cost)

# # pcost.py
# #
# # Exercise 1.32: Using a library function (Modify the program so that it uses the csv module for parsing and try running earlier examples)

# import csv

# def portfolio_cost(filename):
    
    # 'This function calculates the total cost of the portfolio in the file'
    
    # total_cost = 0.0
    
    # with open(filename, 'rt') as f:
        
        # rows = csv.reader(f)
        
        # headers = next(rows)
        
        # # print(headers)
        
        # for row in rows:
            
            # try:
                # nshares = int(row[1])
                # price = float(row[2])
                # total_cost += nshares * price
            # except ValueError:
                # print("Couldn't parse", row)
            
    # return total_cost
    
# cost = portfolio_cost('Data/portfolio.csv')
# print('Total cost:', cost)


# # Exercise 1.33: Reading from the command line (Pass the name of the file in as an argument, in the terminal, to a script)

# import csv
# import sys

# def portfolio_cost(filename):
    
    # 'This function calculates the total cost of the portfolio in the file'
    
    # total_cost = 0.0
    
    # with open(filename, 'rt') as f:
        
        # rows = csv.reader(f)
        
        # headers = next(rows)
        
        # # print(headers)
        
        # for row in rows:
            
            # try:
                # nshares = int(row[1])
                # price = float(row[2])
                # total_cost += nshares * price
            # except ValueError:
                # print("Couldn't parse", row)
            
    # return total_cost
   
# if len(sys.argv) == 2:
    # filename = sys.argv[1]
# else:
    # filename = 'Data/portfolio.csv'
    
# cost = portfolio_cost(filename)
# print('Total cost:', cost)


# # Exercise 2.15: A practical enumerate() example (Using enumerate(), modify the program to print line number with warning message when it encounters bad input)

# import csv
# import sys

# def portfolio_cost(filename):
    # '''    
    # This function calculates the total cost of the portfolio in the file
    # '''
    
    # total_cost = 0.0
    
    # with open(filename, 'rt') as f:
        
        # rows = csv.reader(f)
        
        # headers = next(rows)
        
        # for row_no, row in enumerate(rows, start=1):
            
            # try:
                # nshares = int(row[1])
                # price = float(row[2])
                # total_cost += nshares * price
                # print(f"Row {row_no}: Converted")
            # except ValueError:
                # print(f"Row {row_no}: Couldn't convert: {row}")
            
    # return total_cost
   
# if len(sys.argv) == 2:
    # filename = sys.argv[1]
# else:
    # filename = 'Data/portfolio.csv'
    
# cost = portfolio_cost(filename)
# print(f"Total cost: {cost}")


# # Exercise 2.16a: Using the zip() function

# import csv
# import sys

# def portfolio_cost(filename):
    # '''    
    # This function calculates the total cost of the portfolio in the file
    # '''
    
    # total_cost = 0.0
    
    # with open(filename, 'rt') as f:
        
        # rows = csv.reader(f)
        
        # headers = next(rows)
        
        # for row_no, row in enumerate(rows, start=1):
            # record = dict(zip(headers, row))
            # try:
                # nshares = int(record['shares'])
                # price = float(record['price'])
                # total_cost += nshares * price
                # # print(f"Row {row_no}: Converted")
            # except ValueError:
                # print(f"Row {row_no}: Bad row: {row}")
            
    # return total_cost
   
# if len(sys.argv) == 2:
    # filename = sys.argv[1]
# else:
    # filename = 'Data/portfolio.csv'
    
# cost = portfolio_cost(filename)
# print(f"Total cost: {cost}")

# Exercise 3.14: Using more library module

import report

def portfolio_cost(filename):
    '''    
    This function calculates the total cost of the portfolio in the file
    '''
    portfolio = report.read_portfolio(filename)

    return sum([s['shares'] * s['price'] for s in portfolio])
    
import sys   

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')
    
cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
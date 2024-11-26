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


# Solution

total_cost = 0.0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    
    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        total_cost += nshares * price
        
print('Total cost', total_cost)


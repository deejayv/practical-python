# stock.py
#
# # Exercise 4.1 Objects as Data Structures

# class Stock:
    # '''
    # Represents a single holding of stock
    # '''
    # def __init__(self, name, shares, price):
        # self.name = name
        # self.shares = shares
        # self.price = price

    # def cost(self):
        # return self.shares * self.price

    # def sell(self, nshares):
        # self.shares -= nshares

# Module 4.3 Exercise 4.9: Better output for printing objects

class Stock:
    '''
    Represents a single holding of stock
    '''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
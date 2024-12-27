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

# # Module 4.3 Exercise 4.9: Better output for printing objects

# class Stock:
    # '''
    # Represents a single holding of stock
    # '''
    # def __init__(self, name, shares, price):
        # self.name = name
        # self.shares = shares
        # self.price = price

    # def __repr__(self):
        # return f'Stock({self.name},{self.shares},{self.price})'

    # def cost(self):
        # return self.shares * self.price

    # def sell(self, nshares):
        # self.shares -= nshares

# # Module 5.2 Exercise 5.6: Simple Properties

# class Stock:
    # '''
    # Represents a single holding of stock
    # '''
    # def __init__(self, name, shares, price):
        # self.name = name
        # self.shares = shares
        # self.price = price

    # def __repr__(self):
        # return f'Stock({self.name},{self.shares},{self.price})'

    # @property
    # def cost(self):
        # return self.shares * self.price

    # def sell(self, nshares):
        # self.shares -= nshares

# # Module 5.2 Exercise 5.7: Properties and Setters

# class Stock:
    # '''
    # Represents a single holding of stock
    # '''
    # def __init__(self, name, shares, price):
        # self.name = name
        # self.shares = shares
        # self.price = price

    # @property
    # def shares(self):
        # return self._shares

    # @shares.setter
    # def shares(self, value):
        # if not isinstance(value, int):
            # raise TypeError('expected an integer')
        # self._shares = value

    # def __repr__(self):
        # return f'Stock({self.name},{self.shares},{self.price})'

    # @property
    # def cost(self):
        # return self.shares * self.price

    # def sell(self, nshares):
        # self.shares -= nshares

# Module 5.2 Exercise 5.8: Adding Slots

class Stock:
    '''
    Represents a single holding of stock
    '''
    __slots__ = ('name', '_shares', 'price')
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('expected an integer')
        self._shares = value

    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
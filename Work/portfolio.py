# portfolio.py
#
# # Module 6.1 Exercise 6.2: Supporting Iteration

# class Portfolio:
    
    # def __init__(self, holdings):
        # self._holdings = holdings

    # def __iter__(self):
        # return self._holdings.__iter__()

    # @property
    # def total_cost(self):
        # return sum([s.cost for s in self._holdings])

    # def tabulate_shares(self):
        # from collections import Counter
        # total_shares = Counter()
        # for s in self._holdings:
            # total_shares[s.name] += s.shares
        # return total_shares

# # Module 6.1 Exercise 6.3: Making a more proper container

# class Portfolio:
    
    # def __init__(self, holdings):
        # self._holdings = holdings

    # def __iter__(self):
        # return self._holdings.__iter__()

    # def __len__(self):
        # return len(self._holdings)
    
    # def __getitem__(self, index):
        # return self._holdings[index]
    
    # def __contains__(self, name):
        # return any([s.name == name for s in self._holdings]) 
    
    # @property
    # def total_cost(self):
        # return sum([s.cost for s in self._holdings])

    # def tabulate_shares(self):
        # from collections import Counter
        # total_shares = Counter()
        # for s in self._holdings:
            # total_shares[s.name] += s.shares
        # return total_shares

# Module 6.4 Exercise 6.14: Generator Expressions in Functions Arguments

class Portfolio:
    
    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)
    
    def __getitem__(self, index):
        return self._holdings[index]
    
    def __contains__(self, name):
        # return any([s.name == name for s in self._holdings])
        return any(s.name == name for s in self._holdings)
    
    @property
    def total_cost(self):
        # return sum([s.cost for s in self._holdings])
        return sum(s.cost for s in self._holdings)

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
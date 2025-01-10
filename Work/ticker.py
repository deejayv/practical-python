# ticker.py
#
# # Module 6.2 Exercise 6.10: Making more pipeline components

# from follow import follow
# import csv

# def select_columns(rows, indices):
    # for row in rows:
        # yield [row[index] for index in indices]

# def convert_types(rows, types):
    # for row in rows:
        # yield [func(val) for func, val in zip(types, row)]

# def make_dicts(rows, headers):
    # for row in rows:
        # yield dict(zip(headers, row))

# def parse_stock_data(lines):
    # rows = csv.reader(lines)
    # rows = select_columns(rows, [0, 1, 4])
    # rows = convert_types(rows, [str, float, float])
    # rows = make_dicts(rows, ['name', 'price', 'change'])
    # return rows

# if __name__ == '__main__':
    # lines = follow('Data/stocklog.csv')
    # rows = parse_stock_data(lines)
    # for row in rows:
        # print(row)

# # Module 6.2 Exercise 6.11: Filtering data

# from follow import follow
# import csv

# def select_columns(rows, indices):
    # for row in rows:
        # yield [row[index] for index in indices]

# def convert_types(rows, types):
    # for row in rows:
        # yield [func(val) for func, val in zip(types, row)]

# def make_dicts(rows, headers):
    # for row in rows:
        # yield dict(zip(headers, row))

# def filter_symbols(rows, names):
    # for row in rows:
        # if row['name'] in names:
            # yield row

# def parse_stock_data(lines):
    # rows = csv.reader(lines)
    # rows = select_columns(rows, [0, 1, 4])
    # rows = convert_types(rows, [str, float, float])
    # rows = make_dicts(rows, ['name', 'price', 'change'])
    # return rows

# if __name__ == '__main__':
    # lines = follow('Data/stocklog.csv')
    # rows = parse_stock_data(lines)
    # for row in rows:
        # print(row)

# Module 6.2 Exercise 6.12: Puttng it all together

import report
from follow import follow
import csv
import tableformat

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}" ])

def main(args):
    if len(args) != 4:
        raise SystemExit('USage: %s portfoliofile logfile fmt' % args[0])
    ticker(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
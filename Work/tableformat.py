# tableformat.py
#
# # Module 4.2 Exercise 4.5: An Extensibility Problem

# class TableFormatter:
    # def headings(self, headers):
        # '''
        # Emit the table headings
        # '''
        # raise NotImplementedError()
        
    # def row(self, rowadata):
        # '''
        # Emit a single row of table data.
        # '''
        # raise NotImplementedError()
        
# # Module 4.2 Exercise 4.6a: Using Inheritance to Produce Different Output (TextTableFormatter)

# class TableFormatter:
    # def headings(self, headers):
        # '''
        # Emit the table headings
        # '''
        # raise NotImplementedError()
    
    # def row(self, rowadata):
        # '''
        # Emit a single row of table data.
        # '''
        # raise NotImplementedError()

# class TextTableFormatter(TableFormatter):
    # '''
    # Emit a table in plain-text format
    # '''
    # def headings(self, headers):
        # for h in headers:
            # print(f'{h:>10s}', end = ' ')
        # print()
        # print(('-' * 10 + ' ') * len(headers))
    
    # def row(self, rowdata):
        # for d in rowdata:
            # print(f'{d:>10s}', end = ' ')
        # print()

# # Module 4.2 Exercise 4.6b: Using Inheritance to Produce Different Output (CSVTableFormatter)

# class TableFormatter:
    # def headings(self, headers):
        # '''
        # Emit the table headings
        # '''
        # raise NotImplementedError()
    
    # def row(self, rowadata):
        # '''
        # Emit a single row of table data.
        # '''
        # raise NotImplementedError()

# class TextTableFormatter(TableFormatter):
    # '''
    # Emit a table in plain-text format
    # '''
    # def headings(self, headers):
        # for h in headers:
            # print(f'{h:>10s}', end = ' ')
        # print()
        # print(('-' * 10 + ' ') * len(headers))
    
    # def row(self, rowdata):
        # for d in rowdata:
            # print(f'{d:>10s}', end = ' ')
        # print()

# class CSVTableFormatter(TableFormatter):
    # '''
    # Output portfolio data in CSV format.
    # '''
    # def headings(self, headers):
        # print(','.join(headers))
    
    # def row(self, rowdata):
        # print(','.join(rowdata))
    
# # Module 4.2 Exercise 4.6c: Using Inheritance to Produce Different Output (HTMLTableFormatter)

# class TableFormatter:
    # def headings(self, headers):
        # '''
        # Emit the table headings
        # '''
        # raise NotImplementedError()
    
    # def row(self, rowadata):
        # '''
        # Emit a single row of table data.
        # '''
        # raise NotImplementedError()

# class TextTableFormatter(TableFormatter):
    # '''
    # Emit a table in plain-text format
    # '''
    # def headings(self, headers):
        # for h in headers:
            # print(f'{h:>10s}', end = ' ')
        # print()
        # print(('-' * 10 + ' ') * len(headers))
    
    # def row(self, rowdata):
        # for d in rowdata:
            # print(f'{d:>10s}', end = ' ')
        # print()

# class CSVTableFormatter(TableFormatter):
    # '''
    # Output portfolio data in CSV format.
    # '''
    # def headings(self, headers):
        # print(','.join(headers))
    
    # def row(self, rowdata):
        # print(','.join(rowdata))

# class HTMLTableFormatter(TableFormatter):
    # '''
    # Output portfolio data in HTML format.
    # '''
    # def headings(self, headers):
        # print('<tr>',end='')
        # for h in headers:
            # print('<th>',h,'</th>', end = '')
        # print('</tr>')
    
    # def row(self, rowdata):
        # print('<tr>',end='')
        # for d in rowdata:
            # print('<td>',d,'</td>', end = '')
        # print('</tr>')

# # Module 4.2 Exercise 4.7: Polymorphism in Action

# class TableFormatter:
    # def headings(self, headers):
        # '''
        # Emit the table headings
        # '''
        # raise NotImplementedError()
    
    # def row(self, rowadata):
        # '''
        # Emit a single row of table data.
        # '''
        # raise NotImplementedError()

# class TextTableFormatter(TableFormatter):
    # '''
    # Emit a table in plain-text format
    # '''
    # def headings(self, headers):
        # for h in headers:
            # print(f'{h:>10s}', end = ' ')
        # print()
        # print(('-' * 10 + ' ') * len(headers))
    
    # def row(self, rowdata):
        # for d in rowdata:
            # print(f'{d:>10s}', end = ' ')
        # print()

# class CSVTableFormatter(TableFormatter):
    # '''
    # Output portfolio data in CSV format.
    # '''
    # def headings(self, headers):
        # print(','.join(headers))
    
    # def row(self, rowdata):
        # print(','.join(rowdata))

# class HTMLTableFormatter(TableFormatter):
    # '''
    # Output portfolio data in HTML format.
    # '''
    # def headings(self, headers):
        # print('<tr>',end='')
        # for h in headers:
            # print(f'<th>{h}</th>', end = '')
        # print('</tr>')
    
    # def row(self, rowdata):
        # print('<tr>',end='')
        # for d in rowdata:
            # print(f'<td>{d}</td>', end = '')
        # print('</tr>')

# def create_formatter(name):
    # if name == 'txt':
        # formatter = TextTableFormatter()
    # elif name == 'csv':
        # formatter = CSVTableFormatter()
    # elif name == 'html':
        # formatter = HTMLTableFormatter()
    # else:
        # raise RuntimeError(f'Unknown format {name}')
    # return formatter

# # Module 4.3 Exercise 4.10: An example of using getattr()

# class TableFormatter:
    # def headings(self, headers):
        # '''
        # Emit the table headings
        # '''
        # raise NotImplementedError()
    
    # def row(self, rowadata):
        # '''
        # Emit a single row of table data.
        # '''
        # raise NotImplementedError()

# class TextTableFormatter(TableFormatter):
    # '''
    # Emit a table in plain-text format
    # '''
    # def headings(self, headers):
        # for h in headers:
            # print(f'{h:>10s}', end = ' ')
        # print()
        # print(('-' * 10 + ' ') * len(headers))
    
    # def row(self, rowdata):
        # for d in rowdata:
            # print(f'{d:>10s}', end = ' ')
        # print()

# class CSVTableFormatter(TableFormatter):
    # '''
    # Output portfolio data in CSV format.
    # '''
    # def headings(self, headers):
        # print(','.join(headers))
    
    # def row(self, rowdata):
        # print(','.join(rowdata))

# class HTMLTableFormatter(TableFormatter):
    # '''
    # Output portfolio data in HTML format.
    # '''
    # def headings(self, headers):
        # print('<tr>',end='')
        # for h in headers:
            # print(f'<th>{h}</th>', end = '')
        # print('</tr>')
    
    # def row(self, rowdata):
        # print('<tr>',end='')
        # for d in rowdata:
            # print(f'<td>{d}</td>', end = '')
        # print('</tr>')

# def create_formatter(name):
    # if name == 'txt':
        # formatter = TextTableFormatter()
    # elif name == 'csv':
        # formatter = CSVTableFormatter()
    # elif name == 'html':
        # formatter = HTMLTableFormatter()
    # else:
        # raise RuntimeError(f'Unknown format {name}')
    # return formatter

# def print_table(objects, columns, formatter):
    # '''
    # Make a nicely formatted table from a list of objects and attribute names.
    # '''
    # formatter.headings(columns)
    # for obj in objects:
        # rowdata = [str(getattr(obj, name)) for name in columns]
        # formatter.row(rowdata)

# Module 4.4 Exercise 4.11: Defining a custom exception

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()
    
    def row(self, rowadata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end = ' ')
        print()
        print(('-' * 10 + ' ') * len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end = ' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>',end='')
        for h in headers:
            print(f'<th>{h}</th>', end = '')
        print('</tr>')
    
    def row(self, rowdata):
        print('<tr>',end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end = '')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in columns]
        formatter.row(rowdata)

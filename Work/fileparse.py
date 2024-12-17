# fileparse.py
#
# # Exercise 3.3 : Reading CSV Files

# import csv

# def parse_csv(filename):
    # '''
    # Parse a CSV file into a list of records
    # '''
    # with open(filename) as f:
        # rows = csv.reader(f)
        
        # # Read the file headers
        # headers = next(rows)
        # records = []
        # for row in rows:
            # if not row: # Skip rows with no data
                # continue
            # record = dict(zip(headers, row))
            # records.append(record)
            
    # return records

# # Exercise 3.4 : Building a Column Selector

# import csv

# def parse_csv(filename, select=None):
    # '''
    # Parse a CSV file into a list of records
    # '''
    # with open(filename) as f:
        # rows = csv.reader(f)
        
        # # Read the file headers
        # headers = next(rows)
        
        # # If a column selector was given, find indices of the specified columns.
        # # Also narrow the set of headers used for resulting dictionaries
        
        # if select:
            # indices = [headers.index(colname) for colname in select]
            # headers = select
        # else:
            # indices = []
        
        # records = []
        # for row in rows:
            # if not row: # Skip rows with no data
                # continue
            # # Filter the row if specific columns were selected
            # if indices:
                # row = [row[index] for index in indices]
            
            # # Make a dictionary
            # record = dict(zip(headers, row))
            # records.append(record)
            
    # return records
    
# # Exercise 3.5 : Performing Type Conversion

# import csv

# def parse_csv(filename, types, select=None):
    # '''
    # Parse a CSV file into a list of records
    # '''
    # with open(filename) as f:
        # rows = csv.reader(f)
        
        # # Read the file headers
        # headers = next(rows)
        
        # # If a column selector was given, find indices of the specified columns.
        # # Also narrow the set of headers used for resulting dictionaries
        
        # if select:
            # indices = [headers.index(colname) for colname in select]
            # headers = select
        # else:
            # indices = []
        
        # records = []

        # for row in rows:
            # if not row: # Skip rows with no data
                # continue
            # # Filter the row if specific columns were selected
            # if indices:
                # row = [row[index] for index in indices]
            # # Convert strings to appropriate type
            # if types:
                # row = [func(val) for func, val in zip(types, row)]
            # # Make a dictionary
            # record = dict(zip(headers, row))
            # records.append(record)
            
    # return records
    
# # Exercise 3.6 : Working without headers

# import csv

# def parse_csv(filename, types, select=None, has_headers=False):
    # '''
    # Parse a CSV file into a list of records
    # '''
    # with open(filename) as f:
        
        # rows = csv.reader(f)
        
        # # Check if headers exist and read the file headers
        # if has_headers:
            
            # headers = next(rows)
            
            # # If a column selector was given, find indices of the specified columns.
            # # Also narrow the set of headers used for resulting dictionaries
            # if select:
                # indices = [headers.index(colname) for colname in select]
                # headers = select
                
            # else:
                # indices = []
                
            # records = []
            
            # for row in rows:
                
                # if not row: # Skip rows with no data
                    # continue
                    
                # # Filter the row if specific columns were selected
                # if indices:
                    # row = [row[index] for index in indices]
                    
                # # Convert strings to appropriate type
                # if types:
                    # row = [func(val) for func, val in zip(types, row)]
                    
                # # Make a dictionary
                # record = dict(zip(headers, row))
                
                # records.append(record)
        # else:
            # records = []
            
            # for row in rows:
                
                # if not row: # Skip rows with no data
                    # continue
                    
                # if types:
                    # row = [func(val) for func, val in zip(types, row)]
                    
                # # Make a tuple
                # record = (row[0], row[1])
                
                # records.append(record)
                
    # return records
    
# # Exercise 3.7 : Picking a different column identifier (My take)

# import csv

# def parse_csv(filename, types, select=None, has_headers=False, delimiter = ','):
    # '''
    # Parse a CSV file into a list of records
    # '''
    # with open(filename) as f:
        
        # if delimiter == ' ':
            # rows = csv.reader(f, delimiter=' ')
            
        # else:
            # rows = csv.reader(f)
            
        # # Check if headers exist and read the file headers
        # if has_headers:
            
            # headers = next(rows)
            
            # # If a column selector was given, find indices of the specified columns.
            # # Also narrow the set of headers used for resulting dictionaries
            # if select:
                # indices = [headers.index(colname) for colname in select]
                # headers = select
                
            # else:
                # indices = []
                
            # records = []
            
            # for row in rows:
                
                # if not row: # Skip rows with no data
                    # continue
                    
                # # Filter the row if specific columns were selected
                # if indices:
                    # row = [row[index] for index in indices]
                    
                # # Convert strings to appropriate type
                # if types:
                    # row = [func(val) for func, val in zip(types, row)]
                    
                # # Make a dictionary
                # record = dict(zip(headers, row))
                
                # records.append(record)
        # else:
            # records = []
            
            # for row in rows:
                
                # if not row: # Skip rows with no data
                    # continue
                    
                # if types:
                    # row = [func(val) for func, val in zip(types, row)]
                    
                # # Make a tuple
                # record = (row[0], row[1])
                
                # records.append(record)
                
    # return records
    
# # Exercise 3.7 : Solution

# import csv

# def parse_csv(filename, types=None, select=None, has_headers=True, delimiter = ','):
    # '''
    # Parse a CSV file into a list of records
    # '''
    # with open(filename) as f:
        # rows = csv.reader(f, delimiter = delimiter)
        
        # headers = next(rows) if has_headers else []
        
        # # Make indices for filtering, if specific columns selected
        # if select:
            # indices = [headers.index(colname) for colname in select]
            # headers = select
            
        # records = []
        
        # for row in rows:
            # if not row: # Skip rows with no data
                # continue
                
            # # Filter the row if specific columns were selected
            # if select:
                # row = [row[index] for index in indices]
                
            # # Convert strings to appropriate type
            # if types:
                # row = [func(val) for func, val in zip(types, row)]
                
            # # Make a dictionary or a tuple
            # if headers:
                # record = dict(zip(headers, row))
                
            # else:
                # record = tuple(row)
                
            # records.append(record)
                
    # return records
    
# # Exercise 3.8 : Raising exceptions

# import csv

# def parse_csv(filename, types=None, select=None, has_headers=True, delimiter = ','):
    # '''
    # Parse a CSV file into a list of records
    # '''
    # with open(filename) as f:
        # rows = csv.reader(f, delimiter = delimiter)
        
        # headers = next(rows) if has_headers else []
        
        # # Make indices for filtering, if specific columns selected
        # if select:
            # try:
                # indices = [headers.index(colname) for colname in select]
                # headers = select
            # except Exception as e:
                # raise RuntimeError("select argument requires column headers")
                
        # records = []
        
        # for row in rows:
            # if not row: # Skip rows with no data
                # continue
                
            # # Filter the row if specific columns were selected
            # if select:
                # row = [row[index] for index in indices]
                
            # # Convert strings to appropriate type
            # if types:
                # row = [func(val) for func, val in zip(types, row)]
                
            # # Make a dictionary or a tuple
            # if headers:
                # record = dict(zip(headers, row))
                
            # else:
                # record = tuple(row)
                
            # records.append(record)
                
    # return records
    
# # Exercise 3.9 : Catching exceptions

# import csv

# def parse_csv(filename, types=None, select=None, has_headers=True, delimiter = ','):
    # '''
    # Parse a CSV file into a list of records
    # '''
    # with open(filename) as f:
        # rows = csv.reader(f, delimiter = delimiter)
        
        # headers = next(rows) if has_headers else []
        
        # # Make indices for filtering, if specific columns selected and warn for invalid argument
        # if select:
            # try:
                # indices = [headers.index(colname) for colname in select]
                # headers = select
            # except Exception as e:
                # raise RuntimeError("select argument requires column headers")
                
        # records = []
        
        # for row_no, row in enumerate(rows, start=1):
            # if not row: # Skip rows with no data
                # continue
                
            # # Filter the row if specific columns were selected
            # if select:
                # row = [row[index] for index in indices]
                
            # # Convert strings to appropriate type and catch exceptions
            # try:
                # if types:
                    # row = [func(val) for func, val in zip(types, row)]
                    
                # # Make a dictionary or a tuple
                # if headers:
                    # record = dict(zip(headers, row))
                # else:
                    # record = tuple(row)
                # records.append(record)
            # except Exception as e:
                # print(f"Row {row_no}: Couldn't convert {row}")
                # print(f"Row {row_no}: Reason", e)
                
    # return records

# Exercise 3.10 : Silencing errors (My take)

import csv

def parse_csv(filename, types=None, select=None, has_headers=True, delimiter = ',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter)
        
        headers = next(rows) if has_headers else []
        
        # Make indices for filtering, if specific columns selected and warn for invalid argument
        if select:
            try:
                indices = [headers.index(colname) for colname in select]
                headers = select
            except Exception as e:
                raise RuntimeError("select argument requires column headers")
                
        records = []
        
        for row_no, row in enumerate(rows, start=1):
            if not row: # Skip rows with no data
                continue
                
            # Filter the row if specific columns were selected
            if select:
                row = [row[index] for index in indices]
                
            # Convert strings to appropriate type and catch exceptions
            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                    
                # Make a dictionary or a tuple
                if headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except Exception as e:
                if silence_errors == False:
                    print(f"Row {row_no}: Couldn't convert {row}")
                    print(f"Row {row_no}: Reason", e)
                else:
                    pass
                
    return records

# # Exercise 3.10 : Silencing errors (Solution)

# import csv

# def parse_csv(filename, types=None, select=None, has_headers=True, delimiter = ',', silence_errors=False):
    # '''
    # Parse a CSV file into a list of records
    # '''
    # if select and not has_headers:
        # raise RuntimeError('select requires column headers')
        
    # with open(filename) as f:
        # rows = csv.reader(f, delimiter = delimiter)
        
        # headers = next(rows) if has_headers else []
        
        # # Make indices for filtering, if specific columns selected and warn for invalid argument
        # if select:
            # indices = [headers.index(colname) for colname in select]
            # headers = select
                
        # records = []
        
        # for row_no, row in enumerate(rows, start=1):
            # if not row: # Skip rows with no data
                # continue
                
            # # Filter the row if specific columns were selected
            # if select:
                # row = [row[index] for index in indices]
                
            # # Convert strings to appropriate type and catch exceptions
            # if types:
                # try:
                    # row = [func(val) for func, val in zip(types, row)]
                # except ValueError as e:
                    # if not silence_errors:
                        # print(f"Row {row_no}: Couldn't convert {row}")
                        # print(f"Row {row_no}: Reason {e}")
                    # continue
                    
            # # Make a dictionary or a tuple
            # if headers:
                # record = dict(zip(headers, row))
            # else:
                # record = tuple(row)
                
            # records.append(record)
                
    # return records
# # mortgage.py
# #
# # Exercise 1.7 (Mortgage)

# principal  = 500000.0
# rate       = 0.05
# payment    = 2684.11
# total_paid = 0.0

# while principal > 0:
    # principal = principal * (1+rate/12) - payment
    # total_paid = total_paid + payment

# print('Total paid', total_paid)

# # mortgage.py
# #
# # Exercise 1.8 (Extra Payments)

# principal      = 500000.0
# rate           = 0.05
# payment        = 2684.11
# total_paid     = 0.0
# payment_start_month = 0
# extra_payment_months = 0

# while principal > 0:
    
    # while extra_payment_months < 12:
        # extra_payment_months += 1
        # payment_start_month += 1
        # principal = (principal * (1 + rate/12) - payment) - 1000
        # total_paid = total_paid + payment + 1000
        # #print('Payment #', payment_start_month, 'Total Paid', total_paid, 'Extra Payment Month #', extra_payment_months)
        
    # payment_start_month += 1
    # principal = principal * (1+rate/12) - payment
    # total_paid = total_paid + payment
    # #print('Payment #', payment_start_month, 'Total Paid', total_paid)

# print('Total paid', round(total_paid,2), 'over', payment_start_month, 'months')

# mortgage.py
#
# Exercise 1.9 (Making an Extra Payment Calculator: Modify the program so that extra payment information can be more generally handled. Make it so that the user can set the specified variables)

# principal      = 500000.0
# rate           = 0.05
# payment        = 2684.11
# total_paid     = 0.0
# payment_start_month = 1

# extra_payment_start_month = int(input('Enter month number you want to start extra payment: '))
# extra_payment_end_month   = int(input('Enter month number you want to stop extra payment: '))
# extra_payment             = int(input('Enter how much extra payment you want to make: '))

# extra_payment_months = extra_payment_start_month

# while principal > 0:
    
    # if payment_start_month < extra_payment_start_month and payment_start_month < extra_payment_end_month:
        # principal = principal * (1+rate/12) - payment
        # total_paid = total_paid + payment
        # #print('Payment Month #', payment_start_month, 'Total Paid', total_paid)
        # payment_start_month += 1
        
    # elif extra_payment_months <= extra_payment_end_month and extra_payment != 0:
        # principal = (principal * (1 + rate/12) - payment) - extra_payment
        # total_paid = total_paid + payment + extra_payment
        # #print('Payment Month #', payment_start_month, 'Total Paid', total_paid, 'Extra Payment Month #', extra_payment_months)
        # extra_payment_months += 1
        # payment_start_month += 1

    # else:
        # principal = principal * (1+rate/12) - payment
        # total_paid = total_paid + payment
        # #print('Payment Month #', payment_start_month, 'Total Paid', total_paid)
        # payment_start_month += 1
    
# if extra_payment == 0:
    # extra_payments = extra_payment
# else:
    # extra_payments = extra_payment_end_month - extra_payment_start_month + 1
    
    
# payment_finish_month = payment_start_month - 1   
# print('Total paid', round(total_paid,2), 'over', payment_finish_month, 'months after making', extra_payments, 'extra payments')

# mortgage.py
#
# Exercise 1.10 (Making a table: Modify the program to print out a table showing the month, total paid so far, and the remaining principal)

# principal           = 500000
# rate                = 0.05
# payment             = 2684.11
# total_paid          = 0.0
# payment_start_month = 1
# mortgage            = principal

# extra_payment_start_month = int(input('Enter month number you want to start extra payment: '))
# extra_payment_end_month   = int(input('Enter month number you want to stop extra payment: '))
# extra_payment             = int(input('Enter how much extra payment you want to make: '))

# extra_payment_months = extra_payment_start_month

# while principal > 0:
    
    # if payment_start_month < extra_payment_start_month and payment_start_month < extra_payment_end_month:
        # principal_before = principal
        # principal = round(principal * (1+rate/12) - payment, 2)
        # principal_after = principal
        # amount_towards_principal = round(principal_before - principal_after, 2)
        # total_paid = round(total_paid + payment, 2)
        # print(payment_start_month, total_paid, principal, amount_towards_principal)
        # payment_start_month += 1
        
    # elif extra_payment_months <= extra_payment_end_month and extra_payment != 0:
        # principal_before = principal
        # principal = round((principal * (1 + rate/12) - payment) - extra_payment, 2)
        # principal_after = principal
        # amount_towards_principal = round(principal_before - principal_after, 2)
        # total_paid = round(total_paid + payment + extra_payment, 2)
        # print(payment_start_month, total_paid, principal, amount_towards_principal )
        # extra_payment_months += 1
        # payment_start_month += 1

    # else:
        # principal_before = principal
        # principal = round(principal * (1+rate/12) - payment, 2)
        # principal_after = principal
        # amount_towards_principal = round(principal_before - principal_after, 2)
        # total_paid = round(total_paid + payment, 2)
        # print(payment_start_month, total_paid, principal, amount_towards_principal)
        # payment_start_month += 1
    
# if extra_payment == 0:
    # extra_payments = extra_payment
# else:
    # extra_payments = extra_payment_end_month - extra_payment_start_month + 1
    
    
# payment_finish_month = payment_start_month - 1   
# print('Total paid', round(total_paid,2), 'for', mortgage, 'mortgage', 'over', payment_finish_month, 'months after making', extra_payments, 'extra payments')

# mortgage.py
#
# Exercise 1.11 (Bonus: Fix the program to correct for the overpayment that occurs in the last month)

# principal           = 500000
# rate                = 0.05
# payment             = 2684.11
# total_paid          = 0.0
# payment_start_month = 1
# mortgage            = principal

# extra_payment_start_month = int(input('Enter month number you want to start extra payment: '))
# extra_payment_end_month   = int(input('Enter month number you want to stop extra payment: '))
# extra_payment             = int(input('Enter how much extra payment you want to make: '))

# extra_payment_months = extra_payment_start_month

# while principal > 0:
    
    # if payment_start_month < extra_payment_start_month and payment_start_month < extra_payment_end_month:
        # principal_before = principal
        # principal = round(principal * (1+rate/12) - payment, 2)
                
        # if principal < payment:
            # payment = principal
            
        # principal_after = principal
        # amount_towards_principal = round(principal_before - principal_after, 2)
        # total_paid = round(total_paid + payment, 2)
            
        # print(payment_start_month, total_paid, principal, amount_towards_principal)
        # payment_start_month += 1
        
    # elif extra_payment_months <= extra_payment_end_month and extra_payment != 0:
        # principal_before = principal
        # principal = round((principal * (1 + rate/12) - payment) - extra_payment, 2)
        
        # if principal < payment:
            # payment = principal
        
        # principal_after = principal
        # amount_towards_principal = round(principal_before - principal_after, 2)
        # total_paid = round(total_paid + payment + extra_payment, 2)
        
        # print(payment_start_month, total_paid, principal, amount_towards_principal )
        # extra_payment_months += 1
        # payment_start_month += 1

    # else:
        # principal_before = principal
        # principal = round(principal * (1+rate/12) - payment, 2)
                
        # if principal < payment:
            # payment = principal
            
        # principal_after = principal
        # amount_towards_principal = round(principal_before - principal_after, 2)
        # total_paid = round(total_paid + payment, 2)
            
        # print(payment_start_month, total_paid, principal, amount_towards_principal)
        # payment_start_month += 1

# if extra_payment == 0:
    # extra_payments = extra_payment
# else:
    # extra_payments = extra_payment_end_month - extra_payment_start_month + 1

# payment_finish_month = payment_start_month - 1   
# print('Total paid', round(total_paid,2), 'for', mortgage, 'mortgage', 'over', payment_finish_month, 'months after making', extra_payments, 'extra payments')

# # mortgage.py
# #
# # Solution

# principal = 500000.0
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0
# month = 0

# extra_payment = int(input('How much extra payment do you want to make? '))
# extra_payment_start_month = int(input('Month to start extra payment: '))
# extra_payment_end_month = int(input('Month to stop extra payment: '))

# while principal > 0:
    # month += 1
    # principal = principal * (1 + (rate/12)) - payment
    
    # total_paid = total_paid + payment
    
    # if month >= extra_payment_start_month and month <= extra_payment_end_month:
        # principal = principal - extra_payment
        
        # total_paid = total_paid + extra_payment
    
    # print(month, round(total_paid, 2), round(principal, 2))
       
# print('Total paid', round(total_paid, 2))
# print('Months', month)

# mortgage.py

# Exercise 1.17: f-strings(Modify the mortgage.py program from Exercie 1.10 to create its output using f-strings. 
# Try to make it so that the output is nicely aligned

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = int(input('How much extra payment do you want to make? '))
extra_payment_start_month = int(input('Month to start extra payment: '))
extra_payment_end_month = int(input('Month to stop extra payment: '))

print(f"\n{'Month' : <6}{'Total Paid' : >11}{'Principal' : >11}\n")

while principal > 0:
    month += 1
    principal = principal * (1 + (rate/12)) - payment
    
    total_paid = total_paid + payment
    
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        
        total_paid = total_paid + extra_payment
   
    print(f"{month : <6}{round(total_paid, 2) : >11}{round(principal, 2) : >11}")

print(f"\nTotal paid is {total_paid: .2f} in {month} months.\n")
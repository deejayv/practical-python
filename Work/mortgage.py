# # mortgage.py
# #
# # Exercise 1.7

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
# # Exercise 1.8

# principal      = 500000.0
# rate           = 0.05
# payment        = 2684.11
# total_paid     = 0.0
# payment_number = 0
# extra_payment_months = 0

# while principal > 0:
    
    # while extra_payment_months < 12:
        # extra_payment_months += 1
        # payment_number += 1
        # principal = (principal * (1 + rate/12) - payment) - 1000
        # total_paid = total_paid + payment + 1000
        # #print('Payment #', payment_number, 'Total Paid', total_paid, 'Extra Payment Month #', extra_payment_months)
        
    # payment_number += 1
    # principal = principal * (1+rate/12) - payment
    # total_paid = total_paid + payment
    # #print('Payment #', payment_number, 'Total Paid', total_paid)

# print('Total paid', round(total_paid,2), 'over', payment_number, 'months')

# mortgage.py
#
# Exercise 1.9

principal      = 500000.0
rate           = 0.05
payment        = 2684.11
total_paid     = 0.0
payment_number = 0

extra_payment_start_month = input('Enter month number you want to start extra payment: ')
extra_payment_end_month   = input('Enter month number you want to stop extra payment: ')
extra_payment             = input('Enter how much extra payment you want to make: ')

extra_payment_months = extra_payment_start_month

print('Extra Payment Start Month',extra_payment_start_month)
print('Extra Payment End Month',extra_payment_end_month)
print('Extra Payment',extra_payment)
print('Extra Payment Month #', extra_payment_months)

while principal > 0:
    
    while extra_payment_months < extra_payment_end_month:
        extra_payment_months = extra_payment_months + 1
        payment_number += 1
        principal = (principal * (1 + rate/12) - payment) - extra_payment
        total_paid = total_paid + payment + extra_payment
        #print('Payment #', payment_number, 'Total Paid', total_paid, 'Extra Payment Month #', extra_payment_months)
        
    payment_number += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    #print('Payment #', payment_number, 'Total Paid', total_paid)

print('Total paid', round(total_paid,2), 'over', payment_number, 'months')
# %%
'''
Exercise 2.2:
Write a program to prompt the user for hours and rate per
hour to compute gross pay.
'''

hour = float(input('Enter Hours:'))     # prompt for working hours
rate = float(input('Enter Rate:'))      # prompt for hourly rate


def payroll(hour, rate):                # define the payroll function
    return round(hour*rate, 2)


print(payroll(hour, rate))              # print the gross pay

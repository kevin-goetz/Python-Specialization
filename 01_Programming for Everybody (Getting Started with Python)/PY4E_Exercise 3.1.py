# %%

'''
Exercise 3.1:
Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
'''

hour = float(input('Enter Hours:'))     # prompt for working hours
rate = float(input('Enter Rate:'))      # prompt for hourly pay

if hour <= 40:                          # pay normal rate for hours <= 40
    pay = hour * rate
else:
    pay = 40*rate+(hour-40)*rate*1.5    # pay 50% bonus for hours > 40

print(pay)                              # print total pay

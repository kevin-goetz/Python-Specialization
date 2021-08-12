# %%

'''
Exercise 5.1:
Write a program which repeatedly reads numbers until theuser enters “done”.
Once “done” is entered, print out the total, count, and average of the numbers.
If the user enters anything other than anumber, detect their mistake
using try and except and print an error message and skip to the next number.
'''

# initialize variables
number = '0'
count = 0
sum = 0
avg = 0

# prompt until user writes 'done'
while number != 'done':
    number = input('Please enter a number:')
    try:
        if number != 'done':
            num = float(number)
        else:
            break
    except:  # noqa
        print('please only numbers!')
        continue

    # compute the (intermediate) results
    count = count+1
    sum = sum+num
    avg = sum/count

# print the results
print(sum, count, avg)

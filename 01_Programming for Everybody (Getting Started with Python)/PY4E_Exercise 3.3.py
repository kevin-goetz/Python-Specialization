# %%

'''
Exercise 3.3:
Write a program to prompt for a score between 0.0 and
1.0. If the score is out of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table:
Score       Grade
>= 0.9      A
>= 0.8      B
>= 0.7      C
>= 0.6      D
< 0.6       F

Enter score: 0.95
A
Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F

Run the program repeatedly as shown above to test the various different values
for input.
'''

# prompt for a score until it is a float ranging between 0.0 and 1.0
while True:
    try:
        score = float(input('Enter Score:'))
        if 0 <= score <= 1:
            break
        else:
            print('Bad Score')
            continue
    except:  # noqa
        print('Bad Score')
        continue

# grading the score
if score >= 0.9:
    Grade = 'A'
elif score >= 0.8:
    Grade = 'B'
else:
    Grade = 'Loser'

print(Grade)

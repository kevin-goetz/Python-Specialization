# %%

'''
# Exercise 2.3:
Assume that we execute the following assignment statements:

width = 17
height = 12.0

For each of the following expressions, write the value of the expression and
the type (of the value of the expression).

1. width//2
2. width/2.0
3. height/3
4. 1 + 2 * 5
'''

width = 17                          # initialize variable
height = 12.0                       # initialize variable

print(width//2, type(width//2))     # Test 1
print(width/2.0, type(width/2.0))   # Test 2
print(height/3, type(height/3))     # Test 3

sum = 1 + 1 * 5
print(sum, type(sum))               # Test 4

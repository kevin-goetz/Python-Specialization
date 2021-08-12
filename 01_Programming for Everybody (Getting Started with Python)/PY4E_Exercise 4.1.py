# %%

"""
Exercise 4.1: Run the program on your system and see what numbers you get.
Run the program more than once and see what numbers you get.
"""

import random  # noqa
for i in range(10):
    x = round(random.random()*100)
    print(x)

# %%

'''
Exercise 6.1:
Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing the reverse string in the end.
'''

word = input('Please enter a word:')    # user prompt
reverse = ''                            # initialize variable

for i in word:                          # loop through the word
    reverse = reverse+word[-1]          # add last letter
    word = word[0:-1]                   # shorten the prompt by last letter

print(reverse)                          # print the results

# %%
# Exercise 6.1 in compact form
word2 = input('Please enter a word:')   # user prompt
print(word2[::-1])                      # slicing the whole string to reverse

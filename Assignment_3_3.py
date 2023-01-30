# Write a Python function that accepts a string and calculate the number of upper case letters
# and lower case letters.
# ﻿Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
sentence = input("Enter the strings which are required for lower/upper count:")
def string_test(sentence):
    UPPER_CASE = 0
    LOWER_CASE = 0
    for i in sentence:
        if i.isupper():
           UPPER_CASE +=1
        elif i.islower():
           LOWER_CASE +=1
        else:
           pass
    print ("Original/Entered String : ", sentence)
    print ("No. of Upper case characters in Entered String : ", UPPER_CASE)
    print ("No. of Lower case Characters in Entered String : ", LOWER_CASE)
string_test(sentence)
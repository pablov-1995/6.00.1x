"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""
def count_vowels(s):
    count = len([c for c in s if c in 'aeiou'])
    print("Number of vowels:", count)

count_vowels('azcbobobegghakl')
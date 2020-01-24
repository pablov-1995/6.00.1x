"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
"""
def longest_alphabetical_string(s):
    substring = ''
    new_substring = ''
    for i in range(0, len(s) - 1):
        new_substring = s[i]
        while ord(s[i + 1]) >= ord(s[i]) and i < (len(s) - 1):
            new_substring += s[i + 1]
            i += 1
            if i == len(s) - 1:
                break
        if len(new_substring) > len(substring):
            substring = new_substring
    print("Longest substring in alphabetical order is:", substring)

longest_alphabetical_string('azcbobobegghakl')

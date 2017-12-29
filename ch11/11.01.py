# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary. It doesn't matter what the values are. Then you can use
# the in operator as a fast way to check whether a string is in the
# dictionary. If you did Exercise 10.8, you can compare the speed of this
# implementation with the list in operator and the bisection search.

# Current Status: Complete

import uuid

with open('words.txt') as fd:
    words = fd.read().splitlines()

result = dict()


def dictionary():
    for line in words:
        result[line] = uuid.uuid4()
    return result

print dictionary()
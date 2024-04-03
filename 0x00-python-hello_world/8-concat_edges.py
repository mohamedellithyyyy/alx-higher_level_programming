#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[66:][:-30] + str[-23:-17] + str[7:14] + str[:6] + str[-1]
print(str)

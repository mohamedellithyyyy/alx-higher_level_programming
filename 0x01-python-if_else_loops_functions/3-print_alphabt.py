#!/usr/bin/python3
# Author - Tolulope Fakunle
for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in 'qe':
        print("{}".format(chr(i)), end="")


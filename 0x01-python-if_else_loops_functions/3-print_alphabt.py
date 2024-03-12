#!/usr/bin/python3
# Using a single loop and print function with string format
print(''.join(chr(97 + i) for i in range(26) if chr(97 + i) not in ['q', 'e']), end='')


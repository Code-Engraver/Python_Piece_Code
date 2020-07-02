# A practice file for the print function

import os
import sys
import time

# basic print
# You can see the four string expressions that Python uses.
print('Hello Python!')
print("Hello Python!")
print('''Hello Python!''')
print("""Hello Python!""")

print('=' * 100)

# Separator Option
# Links multiple strings to the specified separator. 
# The default value is one space.
print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('codeengrarver', 'gmail.com', sep='@')

print('=' * 100)

# End Option
# The end parameter allows you to use the specified character instead of [Enter] 
# when the print function is then executed.
print('Welcome To', end=' ')
print('Python world!', end=' ')
print("You're gonna love it.")

print('=' * 100)

# File Option
# The file parameter allows you to save it to a file rather than output it to the console. 
# This is useful when you log.
# There is something beyond the level of this document, and you can just refer to it.

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'result_files', '001_result.txt'), 'w') as f:
    print("It's written to the file.", file=f)

# Flush Option
# flush is a parameter related to the I/O buffer. 
# It's a difficult concept, and there aren't many places to use it, 
# so it's something you can skip. 
# For example, a keyboard has the concept of 'buffer' between the keyboard and the screen. 
# The buffer is a place to store content for a short time before printing it.
# Printing what's stored in the buffer is expensive in terms of efficiency. 
# In other words, the less push, the more efficient it is. 
# So sometimes the contents of the buffer may not be output immediately for efficiency.
# The concept of this buffer exists in the print function. 
# The flush parameter determines whether the contents of the buffer are forced out. 
# Default value is False, where the contents of the buffer may not be printed immediately to reduce costs. 
# When set to True, however, the push is forced without considering the cost. 
# I think the example below will help you understand.
print('This will be output in five seconds.')
time.sleep(5)

print("It's printed out immediately.", flush=True)
time.sleep(5)

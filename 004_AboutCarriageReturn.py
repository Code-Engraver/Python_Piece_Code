# In this file, I will explain about Carrie Return. 
# There is not much to explain. 
# Carrie Return is the act of sending the cursor to the starting point. 
# You can understand it right away if you just run the example below.
print("Python is Wonderful Programing Language!!!")
print("Python is Wonderful Programing Language!!!\rnodejs")

# Doesn't it make sense right away? 
# If you look at the simple application, 
# you will be able to use various applications when you create programs that print out to the console.

import time

def print_time_one_line(time):
    print('Time Remaining: %d'%time, end='\r')

count = 0
while count <= 5:
    print_time_one_line(count)
    count += 1
    time.sleep(1)

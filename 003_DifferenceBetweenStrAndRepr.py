# This file wants to explain the difference between __str__ and _repr_. 
# Many people are curious and look for it because it looks similar but has different usage methods. 
# It doesn't seem so important to look at, but it's necessary for programming based on OOP.
# I'll continue to explain by executing an example.

from datetime import datetime
today = datetime.now()
print(today)
print(f"__str__ : {str(today)}")
print(f"__repr__ : {repr(today)}")

# What __str__ and __repr__ have in common is that they are expressed in strings. 
# The difference is that the purpose of the use is different. 
# It makes the object readable for __str_, and clearly represents the object for __repr_. 
# To put it simply, if __str__ is a function for this user, __repr__ is a function for the developer. 
# Copying and printing the __repr_ results from the example shows that the same results can be obtained.

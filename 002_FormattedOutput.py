# Enter the link at the bottom to see the description provided by the Python Course site.
# https://www.python-course.eu/python3_formatted_output.php
# I will do various practical exercises using the contents of Python Course site.

# From now on, we are going to introduce various string formatting methods. 
# Personally, I recommend the last method. 
# That's what Python Course site introduces.

# I'll take a quick look at the most primitive method. 
# You can print it out as it is through type conversion, 
# and the way to go a little further is to use the comma and sep parameters.
print("=" * 50, "Primitive Method", "=" * 50)
number1 = 60
number2 = 100

print(str(number1) + " " + str(number2) + " " + str(number1 + number2))
print(number1, number2, number1 + number2)
print(str(number1) + "," + str(number2) + "," + str(number1 + number2))
print(number1, number2, number1 + number2, sep=',')

# In Python, "%" replaces the printf function of other languages. 
# Use the designated characters to determine the format of the string. (an integer type, a real type, etc.)
# It's a very old-fashioned way.
# Python Course site introduces that one day you can disappear from language, 
# but says you have to know to read the old codes.
"""
Conversion Summary
d	Signed integer decimal.
i	Signed integer decimal.
o	Unsigned octal.
u	Obsolete and equivalent to 'd', i.e. signed integer decimal.
x	Unsigned hexadecimal (lowercase).
X	Unsigned hexadecimal (uppercase).
e	Floating point exponential format (lowercase).
E	Floating point exponential format (uppercase).
f	Floating point decimal format.
F	Floating point decimal format.
g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
c	Single character (accepts integer or single character string).
r	String (converts any python object using repr()).
s	String (converts any python object using str()).
%	No argument is converted, results in a "%" character in the result.
"""
# How to use : %[flags][width][.precision]type
print("=" * 50, "Using %", "=" * 50)
name = "A"
subject1 = "Math"
subject2 = "English"
score1 = 85
score2 = 90
print("%c : %r's score %5d, %s's score %i"%(name, subject1, score1, subject2, score2))

number3 = 6666
print("%u's decimal expression is %u"%(number3, number3))
print("%u's octal expression is %o"%(number3, number3))
print("%u's hexadecimal expression(lowercase) is %x"%(number3, number3))
print("%u's hexadecimal expression(uppercase) is %X"%(number3, number3))

float1 = 1235143695.748321
float2 = 13832.1
print("%f%%, %3.2f%%"%(float1, float1))
print("%e, %E"%(float1, float1))
print("%g, %G"%(float1, float2))

# String formatting is also possible using the format function.
# Various methods of use exist within the format function. 
# I'll get to know you through a lot of practice.
# The character representing the type used in the example is almost the same as when using "%".
# How to use : [[fill]align][sign][#][0][minimumwidth][.precision][type]
print("=" * 50, "Using format Function", "=" * 50)
name1 = "Frank"
name2 = "Dennis"
age1 = 25
age2 = 32
height1 = 176.384
height2 = 169.123

print("{0}'s age is {1} and height is {2}".format(name1, age1, height1))
print("The person who is {1:d} years old and {2:.1f}cm is {0:s}".format(name1, age1, height1))
print("{name}'s age is {age} and height is {height}".format(name=name2, age=age2, height=height2))
# In locals() the declared variables are stored in dect type and can be used as follows
# You can just name the variable, but it's more useful than you think.
print("name1={name1}, name2={name2}".format(**locals()))

# In addition, the format function allows you to specify string formats through various flags. 
# It can also be implemented in flag, such as central alignment, text placement on left and right sides, 
# or a function that is implemented separately can also be used. 
# Since I can't find good examples that are diverse and suitable, you'd better use the link below if necessary,
# so we'll move on without introducing it.
# https://pyformat.info/

# From now on, I highly recommend the method to introduce. 
# There is no reason to code something behind, such as using format function or "%" by inserting variables into a string as they are.
# It is a good way to increase readability.
print("=" * 50, "Using f for fomatting (After Python 3.6)", "=" * 50)
product = "pen"
price = 15000

print(f"Product is {product} and price is {price}, I have 45000 so can buy {int(45000/price)}")

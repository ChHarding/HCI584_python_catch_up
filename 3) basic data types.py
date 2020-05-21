# basic data types

#
# numbers: int and floats 
# HCI 574 end of lecture 2 and lecture 4
#

# whole numbers, integers (ints)
i = 7 
print(i / 3) # / dividing an number  by an int yields a float (in Python 3!)
print(i // 3) # // means integer division
print(i % 3)  # % means remainder ( 7 = 3 + 3 + 1)
print(int(123.456)) # int() truncates floats
print(int("123"))    # or converts a string with a valid integer into an int
print(int("123.456")) # error: "123.456" is not a valid integer string
# there's no comma allowed in large ints
print(1,000) # "works" b/c 1,000 is a shortcut to (1,000) which is a tuple

# decimal numbers (floating point numbers or floats)
# floats ALWAYS have a decimal point!
f = 123.456 # a float
f2 = 7.0 # also a float! 
print(type(f2)) # see the type (or class) of a variable(*)
print(4 / 2) # / division always makes a float (2.0), even if it could be an int (2)

# floats seem infinitely precise but have in fact limitations (not only in Python)!
# https://docs.python.org/3/tutorial/floatingpoint.html
# There's normally no single vs double precision (a normal float is 64 bits)
# (numpy can give you 128 bit floats)

# float() converts to floats
print(float(123), float("123"), float("123.456") )


# Doing math 
# Mixing int and floats results in floats
print(1.1 + 2)
# python has the typical math operations +, -, *, /, ** 
print((1.1 - 2) * 2**3) # (an example of precision limitation from earlier!)
# you can use +=, -=, *=, /= as shortcuts to "update" a variable
print(i)
i += 3 # same as i = i + 3
print(i)
print(i++) # this ain't C/C++!

# styling: leave spaces around operators and =  


# rounding (properly up or down)
f = 123.456
print(round(f, 1)) # round to 1 (post period) digit
print(round(f, 2)) # round to 2 digits


# for even simple math functions (log, sin) you must import the math module
#  https://docs.python.org/3/library/math.html
import math # imports the names defined in math module into the current namespace
print(dir(math)) # quick and dirty way to see all functions/constants in math module
print(pi) # despite the import pi is not directly available!
print(math.log10(3) * math.pi)  
# as pi and log10 are defined in the math namespace, you must put math. in front of them!

# random numbers https://docs.python.org/3/library/random.html
import random
print(random.random()) # random float from 0.0 up to 1.0
print(random.randint(10, 20)) # random in between 10 and 20
help(random.randint)  # shows info about name,  help(random.randint()) <- NO ()

#
# Strings
# HCI574 lecture 4
#

# strings are sequences of characters
# must start and end with (the same type) of quote, either double or single
s1 = "a double quoted string"
s2 = 'single quotes work, too!'
print(s1,s2, repr(s2)) # repr() will put quotes around strings when printed

# triple quotes are useful to make strings that contain quotes
s3 = '''It's "nice" to see you!'''

# can also be used to temporarily comment out multiple lines
'''
a = 3
print(a)
b = a + 4
'''
# special characters 
# start with \
# \n = new line (line break)
# \t = tab
print("1\t2\t3\n4.0\t-4\t234")

# indexing
# way to get a single char from a string
# first letter has index 0 ! (not 1)
s = "abc"
print(s[0])
print(s[3]) # index out of range, the index of c is 2!

# negative index: start from the last char and go left
print(s[-1], s[-2], s[-3])

# slicing (HCI574 lecture 5)
# way to get a chunk of chars
# uses a start(left) and end(right) index
s = "Python"
print(s, s[0:3], s[2:5])
# Important: slice start/end index refers to gaps "around: chars
# 0   1   2   3   4   5   6 
# +---+---+---+---+---+---+ 
# | P | y | t | h | o | n | 
# +---+---+---+---+---+---+
#-6  -5  -4  -3  -2  -1    <- blank

print(s[2: ]) # end index is blank, not 0!
print(s[-4:-1]) # can use negative numbers, still left:right!
print(s[1:-1]) # or mix them
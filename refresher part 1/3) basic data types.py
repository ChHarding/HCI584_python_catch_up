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
print(1000) # "works" b/c 1,000 is a shortcut to (1,000) which is a tuple

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
# Bools (HCI574 lecture 6)
#

# Used for boolean evaluations and true/false flags in general
a = True
b = False

i1 = 4
i2 = 2
b = i1 > 2 # is i1 bigger than 2? True/False
print(b) 
print(i1 == i2) # is i1 the same value as i2?
print("th" in "Monty Python") # does string contain "th" somewhere?

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
s = "bacASdsa3da"
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

# index and slicing gives you a copy!
c = s[0:3]
s = "different string" # new content, old content is gone
print(c,s)

# Strings are immutable
# you cannot directly manipulate a string!
s[0:9] = "Another" # error: 'str' object does not support item assignment
del s[0] # I want to delete the fist char but this also won't work


# String manipulation - despite immutability
# in general: get a copy and minupulate that, then overwrite the original string

# delete the first char in s
s = s[1: ] # make a slice and re-assign!
print(s) # the old s is gone but the effect is that the first char was "deleted"

# remove last 4 chars from filename
s = "somefile.txt"
s = s[:-4]
print(s) 

# String methods https://www.w3schools.com/python/python_ref_string.asp
print(s.upper(), s) # print a uppercasified copy, s was NOT changed
s = "This is a line with a few words in it"
l = s.split() # split into list of words defined by spaces (whitespace, incl. \t and \n)
print(l)
print("-*-".join(l)) # join list into string with - between words

# gluing strings together (concatenation)
s2 = s + ", and that's just fine!"
print(s2)

############################


# empty strings are legal and useful
s = "" # empty for now, ready to add chars later
s += "adding "
s += "words "
s += "together "
print(s)


# str() converts to a string
i = 77
f = 12.34
s = "item #" + str(i) + " is worth $" + str(f) 
print(s)


# string formatting (https://realpython.com/python-f-strings/)
# HCI 574 lecture 10
money = 1000
name = "Chris"
print(f"Hey {name}, you owe us ${money}!")

# print()
# takes multiple args, comma separated, of any type
# will convert each arg to string and separates them by a space
print("item #", i, " is worth $", f) # compare to above!
# sep arg defines what char(s) to use for separation
print("item #", i, " is worth $", f, sep="")
# use end="" to supress new line
# print can also print into opened files

# regular expressions (regex), pattern matching
# HCI 574 lecture 26 (https://regex101.com)



#
# Lists (HCI574 lecture 7)
#

# sequence of elements (any type of object)
l = [1, "two", 3.0, "FOUR"]
print(l)

# index and slices work the same as for strings
print(l[0], l[-1], l[1:-1])

# lists are mutable, so you CAN overwrite elements
l[0] = "START"
l[1:3] = [2, 3]
print(l)

# lists can be nested, i.e. another list can be an element
l[-1] = ["another", "list", -999, 12314.45354,] # overwrite last element with list
print(l)
# regular nested lists can be matrices or tables
m = [ 
      [1, 2],
      [3, 4]
    ]

t = [ 
      ["year", "income"],
      [2003,    231423],
      [2004,    334223],
      [2005,     98424],   # it's OK to have a superfluous , at the end
    ]

#  Python also has numpy for proper arrays and dataframes for proper tables (later)

# list() makes a list of chars from a string
print(list("Monty Python"))


# grow lists
l = [1, "two", 3.0, "FOUR"]
l = [0] + l + [5, "six"]  # pre and append lists with +
print(l) # note that you need to make a 1 element list from the 0! 

# empty lists
l = []
l.append(1)  # quick way to append a single new element (change-in-place method!)
l.append(["x", "y"]) # append a 2 element (sub) list
print(l)
# More list methods: https://www.w3schools.com/python/python_ref_list.asp

# list comprehension (but advanced!)
l = ["Monty", "Pythonista's", "fly-catching", "Circus"]
len_lst = [len(e) for e in l] # make a lists of lengths foe each element in l
print(l)
print(len_lst)

len_combo_lst = [[len(e), e] for e in l] # combo list for length and string
print(len_combo_lst)

# sort sublists: 
sl = sorted(len_combo_lst, reverse=True)
print(sl)
# Whats the longest word?
print(sl[0][1], "is longest with", sl[0][0], "chars")


#
# Tuples and Sets
#

# Tuples a immutable lists (constant)
t = (1,2)
t[0] = 999 # won't work, can't change tuple elements
t = 1,2  # short for (1,2)
print(t)
t = 1,  # single element tuple (gotcha warning)
print(t)


# Sets are list with guaranteed unique elements
s1 = set([3,2,3,2,1,2,1,1,1,1,2,0])
s2 = set([2,3,4,3,4,5,6,0,2,4,4])

# sets have no order, they always appear(1) to be sorted
print(s1, s2) # note the { } to show it's not a list (it's not a dictionary!)

# set operations https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
print(s1.intersection(s2)) # which elements occur in BOTH lists?



#
# Dictionaries (dicts)  HCI 574 lecture 8
#

# dicts are bags of key-value-pairs   key:value
# bag => does not have the concept of order, despite appearing to be sorted (like sets)
# key needs to be immutable, typically a string is used
# keys act like an index but with a string instead of a number# 

chris = {}  # empty dict
chris["name"] = "Harding" # add a new key and assign value
chris["height_cm"] = 184

bob = {"name":"Bobbington", "height_cm":174}
print(chris, bob)

# update/overwrite value for existing key
bob["height_cm"] = 172

# add new key
bob["height_inch"] = round(bob["height_cm"] / 2.54, 2)
print(bob)

# conversion to list
print(bob.keys()) # list of all keys, note its a special list type dict_keys
values = list(bob.values()) # list of all values, converted to normal list
print(values)
print(list(bob.items())) # list of key, value tuples

# these lists are NOT connected to its dict anymore
keys[0] = "NAME WAS CHANGED!"
print(keys, bob)

# make dict from list of "pairs"
anne = dict([["name","Albright"], ["height_inch", 5.5]])
print(anne)


#
# None
#

# special value, not a Bool
# sometimes use to indicate a "failure" without rasing a exception (error)

# print() doesn't return anything but this is NOT an error
r = print("bla") 
print(r) 

# Gotcha!
l = [1,2,3]
l.append(4) # append() returns None
print(l)
l = l.append(5) # easy mistake to make!
print(l) # what happend?
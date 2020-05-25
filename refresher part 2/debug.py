# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Flow control (branching and loops)
# Python refresher - part 2
# May 25, 2020
# 
# 
# - this is a jupyter notebook
# - it has markdown (formated text cells) and python (code) cells
# - both can be edited
# - all lines in a code cell are evaluated from the top and the result is shown below the cell (output)
# 
# 
# - below is a code cell for you to test
# - click on the code (so the code cell is active) and hit __Shift__-Enter (Or: click on the green arrow

# %%
# test code cell
print("I'm a code cell")
a = 3
a  # the last line is evaluated and the result is shown (no need for print)
#a; # if you want to suppress the output for the last line evaluations, end in ; 

# %% [markdown]
# # if elif else statement
# HCI 574 lecture 13
# 
# - basic branching statement
# - each keyword ends with : and so requires a block
# - if and elif blocks need to be followed by a test that evaluates into either True or False

# %%
a = 4

if a > 3: # <- ends with:, next line(s) need to be indented
    print("It's True,", a, "is bigger than 3")  # block is run if evaluates to True
    # indented line, so I'm still part of the block
# de-dentend, so I've left the block!
# there's no else, so in case of False, no block is visited and nothing happens


# %%
# if you want to cover the False case, use the else statement
a = 3

if a > 3: # <- ends with:, next line(s) need to be indented
    print("It's True,", a, "is bigger than 3")  # this block is run when True
else:
    print("Nope ", a, "is NOT bigger than 3") # this block is run otherwise i.e. when False


# %%
# elif(s) are used for more tests
a = 3

if a > 3: # first test
    print("It's True,", a, "is bigger than 3")  # this block is run when first test is True
elif a == 3: # 1. test must have been False, now run a 2. test
    print(a, "is 3") # 2. test was True
else: # neither 1. nor 2. test were true
    print("logically,", a, "must be smaller than 3")

# %% [markdown]
# #### Ternary operator in Python
# - fancy, but very compact
# - there are no : and no elifs
# 
# 
# - traditional form:
# ```
# a = -4
# if a < 0:
#     sign = "negative"
# else:
#     sign = "positive"
# ```

# %%
a = -4
sign = "negative" if a < 0 else "positive" # with this 0 is positive
print(a, "is", sign)

# %% [markdown]
# # Block structure
# HCI574 lecture 12
# 
# - a block is one or more lines of code
# - blocks are only defined via increasing or decreasing indentations:
#     - if the next line is farther to the right, you're about to enter a block
#     - if the next line is farther to the left, you're about to left this block
# - blocks can be nested
# 
# - use 4 spaces as indents and de-dents, hitting tab in VS will inline 4 spaces for you
# - don't mix tabs and spaces
# 
# - to move blocks around:
#     - paint the lines you want moved
#     - hit tab (move block right) or shift-tab (left)
# 

# %%
s = ''
while len(s) < 5:
# indent the next 3 lines
for a in range(0, 10):
    print(s)
    s += str(a)

# %% [markdown]
# - make sure your block boundaries create the structure you want!
# - It's very easy to accidentally create a perfectly "legal" block structure that gives radically different result

# %%
# I forgot to move the last line ... with unindented consequences!
s = ''
while len(s) < 5:
    for a in range(0, 10):
        print(s)
    s += str(a)

# %% [markdown]
# ### temporarily disable a block
# - Scenario: a block can probably go, but needs more testing first. Maybe you still needs it later, so you don't want to actually delete it
# - comment out block with ''', this can be evaluated and thus counts as a vaild block
# - make sure to line up the '''s
# - to deactivate a block with a single line:
#     - use #
#     - add `pass` (a dummy or noop command) so it's still a valid block

# %%
a = 3
if a > 3:
    #print("True")
    pass
else:
    '''
    a = 4
    v = input("enter value")
    print(v,a)
    '''

# %% [markdown]
# # while loops
# HCI 574 lecture 14 
# 
# - `while:` statement must be followed but a True/False expression (test)
# - while block will be run if test is True
# - block will be run again and again, UNTIL test fails! (False) 
# - The code of the block MUST somehow, eventually make the test fail, otherwise you'll get an endless (infinite) loop
# - here, the initial value of i is changed inside the loop, so it test of i will eventually fail

# %%
i = 5
counter = 0

while i > 0:
    print(counter, i)
    counter += 1
    i -= 1  # if this is commented out, while will loop forever!

# %% [markdown]
# - an endless loop will make its cell have a [*] (busy) in front of it
# - to jump out, hit the red hollow Square (Interrupt)
# %% [markdown]
# ### `break` and `continue`  
# - `while True:` will set up an endless loop  
# -  you can still "bail out" of the block with `break`
# - `continue` will immediatly jump back to the while test 
# 
# - Here, I stay in the loop until my try to convert a string with `float` does NOT raise an exception

# %%
# get a string from user, validate it and convert to float
f = None
while True:
    s = input("Enter a valid float")
    try:
        f = float(s)
    except e as Exception:
        print(s, "is NOT a valid float. try again")
        #print(e) # this would print the exception opject and it's error message
        continue # jump back to while True:
    else:
        print(s, "is a valid float. Thank you for your cooperation!")
        break # jump out
print(f)

# %% [markdown]
# # Exceptions (try except else)
# (HCI 574 lecture 22 - error handling)
# 
# - branching as a result of an error 
# - an error in python will raise an exception, which, for us, will exit the code and show an error message
# - 'try:' will protect the code in its block (typically a __single line__)
# - if the code raises an exception, the `exception` block is executed, if the code was OK, an optional `else:` block will be run
# - It's often useful to catch the exeption object that was raised, here it will be put in e. Printing it out will usually give you a hint as to what's wrong
# 
# %% [markdown]
# # For loops
# 
# HCI 574 lecture 15
# 
# - the [range](https://www.geeksforgeeks.org/python-range-function/) function generates a sequence ("list") of ints often used with for loops
# - range is a [generator](https://wiki.python.org/moin/Generators)
# - `range(start, end (not reached!), step_size)`
# 

# %%
r = range(1, 10, 2) # from 1, up to (but not including!) 10, in steps of 2
print(r) # shows generator object, not the list
l = list(r) 
for e in l: #
    print(e)
    e = -999 
print(l) # l was not changed!

# %% [markdown]
# - `e` is the so-called target variable, i.e. the "current" element
# - `e` is a copy(!) of each element in l, i.e. changing `e` will not affect l!
# - `e` is a proper variable (created when the for loop is first entered), you can use any name for it
# 
# 
# - the for loop __sequence__ can be any list or string, or more generally, any [iterator](https://anandology.com/python-practice-book/iterators.html)
# - when you loop over a block, you __iterate__ over it, each pass is an __interation__
# - for dictionaries, you'll iterate over a (ad hoc created) list of its key

# %%
s = "Monty Python"
for e in s:
    print(e, end=" ") # instead of newline, put space at the end


# %%
dct = {"x":12, "a":57, "d": 43}
for k in dct:
    print(k, end=" ")

# %% [markdown]
# - list, tuple, dictionary comprehensions use the same syntax

# %%
s = "list, tuple, dictionary comprehensions use the same syntax"
words = s.split(" ") # make list of words
d = {k:len(k) for k in words}
print(d)

# %% [markdown]
# - enumerate() will generate a list of tuples, with index and element
# - very useful to get a counter when iterating
# - note how the tuple is unpacked into 2 target variables

# %%
s = "Monty Python"
for i,e in enumerate(s):
    print(i, e)

# %% [markdown]
# - zip(a, b. ...) will create a list of combo tuples from 2 or more lists/tuples

# %%
# keys and values for the dictionary from above
k = d.keys() 
v = d.values()

# zip into a duo tuple list and iterate of it 
for t in zip(k,v):
    print(t)

# %% [markdown]
# # How to change a list via a loop?
# 
# ### Change in place (i.e. change the same object)
# - while loop: 
#     - get your own counter, which is also your index into the list
#     - as long as the counter is within the range of the list, access and change each element via the index

# %%
# square the numbers in this list
L = [1,3,4,2,5,8,6,3,5,0]

c = 0 # counter
length = len(L)
print(length) # length is 1 more than the highest valid list index!
#print(L(length)) # out of range!

while c < length-1: # from 0 (first element) to last 
    L[c] = L[c] * L[c] # read current element, square and wrinte back
    c += 1 # increment to index of next element

print(L)

# %% [markdown]
# - for loop:
#     - use enumerate() to get the index of the current element
#     - change current element

# %%
# square the numbers in this list
L = [1,3,4,2,5,8,6,3,5,0]

for i,e in enumerate(L):
    L[i] = e * e # or L[i] = L[i] * L[i]

print(L)

# %% [markdown]
# ### return changed copy
# 
# - I prefer to not change the list but rather assemble a copy of it with changed elements
# - start with empty, 2. list
# - iterate over list
#     - from targe variable, make new content
#     - append to 2. list

# %%
L = [1,3,4,2,5,8,6,3,5,0]
Lc = [] # changed copy

for e in L:
    sq = e * e
    Lc.append(sq)
    
print(L)
print(Lc)

# %% [markdown]
# ## How to debug a jupyter notebook (sort of works)
# - click _convert and save to a python script_ (rightmost icon on top of notebook)
# - you will see a strange new "file" (new edit tab), which is NOT yet saved!
# - Use Control-S ro manually save it as a temporary .py file, e.g. as debug.py
# - debug.py will show the notebook in pure text with special comments to siginfy the start of each cell:
# - markdown will start with `# %% [markdown]`
# - code will start with `# %%`:
# ```
# # %%
# a = -4
# sign = "negative" if a < 0 else "positive" # with this 0 is positive
# print(a, "is", sign)
# ```
# - you can debug this version with the standard debugger. Just hit _Debug Cell_
# - you will see lots of weird variables that jupyter (ipython) needs
# - Big Caveat:
#     - after you've fixed debug.py you cannot simply convert it back to your (.ipynb) notebook!
#     - solution: you have to copy/paste the cell's code into your notebook
# - your debug.py is not magically connected to the notebook you converted it from!
# - I suggest that you treat the notebook as master and either overwrite debug.py every time you want to debug or delete it after you're done
# 
# 
# 
# 
# 

# %%



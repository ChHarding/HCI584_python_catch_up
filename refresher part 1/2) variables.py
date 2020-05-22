# variables

# using literal values
print("Monty Python") # literal string
print("Monty Python".split()[1]) # literal 1
print("bla" * 3) # literal 3 

# Same with variables
s = "Monty Python"
r = 3
print(s * r)

# variables are created only(!) via assignment
# whatever is right of the = is given the name that's left to the =

# fills a chunk of memory with some chars  and call that var
var = "I'm a string" 

# python variables are just labels (tags) to something in memory space (memory object)
# variables don't have types, only the memory object it refers to has a type
# id() gives you the address of the memory object (as decimal int)
print(hex(id(var))) # hex address of the (start of) the memory object

# as the variable name has no concept of type, we can just make it refer
# to a different memory object, say a list:
var = ["Now", "I'm", "a", "list!", 1,2,3]
print(hex(id(var))) # the mem. obj, var refers to now sits at a different address!

# the earlier string object is now inaccessible, so it will be recycled (garbage collection) 

# compact multi value assignments (essentially unpacking a tuple)
a, b, c = 1, 2, 3 # short for a tuple (1, 2, 3)
print(a,b,c)


# assignments: copy vs alias
L1 = [1,2,3] # list (mutable)
print(hex(id(L1)), L1)

# assigning an existing variable name to a different variable creates an alias to the same mem. obj.
L2 = L1
print(hex(id(L2)), L2) # same address

# changing (mutating) the mem. obj.
L2[0] = -999
print(hex(id(L2)), L2) # yep, different content
print(hex(id(L1)), L1) # L1 (refering to the same mem.obj. also shows the change!

# what happens if one of the 2 references is "deleted"?
del L1 # "unlinks" L1 from the mem. obj. 
print(L2) # but as we still have L2 refering to it, it's still alive!
del L2 # last link is gone, now the memory can be properly released

# How to make a copy?
L1 = [1,2,3] # list (mutable)
print(hex(id(L1)), L1)

L2 = L1[:]  # [:] is a slice from beginning to end i.e. all of the list. Same as L1.copy()
# note on copy() vs deepcopy(): https://docs.python.org/3/library/copy.html 
print(hex(id(L2)), L2) # same "content", different address

L2[0] = -999
print(hex(id(L2)), L2) # yep, different content
print(hex(id(L1)), L1) # as L2 was a copy, and we changed a copy, L1 still shows the same content

# Local variables
def foo(x):
    var = x * x # var is a local variable
    print("local var is", var, hex(id(var)))
    return var # after the return, var gets deleted

var = 123 # var in a "global" scope
print("global var is", hex(id(var)))

print(foo(3))  # force use of local var
print(var) # global var is unchanged

# local variables are critically important for isolating the code inside the function(def part)
# from code that uses that function (call) from the outside!

# variable names
# - lower case, use underscores
# - name should describe the variables role
# - the more important the variable is the more descriptive and understandable the name should be
time_to_impact = 12.3
master_timestamp_deviation_by_type_list = [["Type_a", [1.34, 454.2]], ["Type_b", [4.3, 536.32]]]

# if needed, you can always use an alias for less typing and better comprehension
m = master_timestamp_deviation_by_type_list # m is a short alias
print(m[0][0][-1], m[0][1][1]-m[0][1][0], m[1][0][-1], m[1][1][1]-m[1][1][0]) 
# not pretty but a lot compacter than if I had used master_timestamp_list

# - it's ok to use (very) short names as helpers or within snippets

# - maybe encode the type - if that helps to counter possible confusion
size_str = input("Enter size: ") # returns a string
size_num = float(size_str) # convert to int
print(size_num * 12.3) # do do math we need to use a number, not the string!


# constants
# there's no real way in python to make a read-only variable, so constants are
# simply indicated via all uppercase names 
GRAVITY = 9.81



# for later:
# write a function that takes a string with words and repeats the string times the number of words
s = "this has oh so many words"
w = s.split()
l = len(w)
print(s, w, l)
print(s * l)


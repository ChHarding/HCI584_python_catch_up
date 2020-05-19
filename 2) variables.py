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

# assignments: copy vs alias




# for later:
# write a function that takes a string with words and repeats the string times the number of words
s = "this has oh so many words"
w = s.split()
l = len(w)
print(s, w, l)
print(s * l)


# 







# given a list of netids, print out the ISU email addresses as a single line with 
# commas in between (for pasting them into a text field on Piazza)

# input
netids = ["gvrossum", "ScroodgeMD", "mchammer", "charding"]
# output:
# gvrossum@iastate.edu,ScroodgeMD@iastate.edu,mchammer@iastate.edu,charding@iastate.edu,
for n in netids:
    print(n+"@iastate.edu,", end="")

# 
initial_gap = "       "
base_length = 9
x = "+"
gap = " "
middle = x
spaces = ""
for i in range(int(base_length / 2)):
    space_additions = (base_length / 2) - i
    for y in range(int(space_additions)):
        spaces += " "
    print(initial_gap + spaces + middle + spaces)
    middle = x + gap + x
    gap += "  "
    spaces = ""
print(initial_gap + spaces + middle + spaces)
spaces = ""
x = ""
for i in range(len(middle)):
    spaces += " "
for i in range(7):
    x += "+"
print(x + spaces + x)
for i in range(5):
    

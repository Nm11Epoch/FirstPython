base_length = int(input("How long would you like the base of your equilateral triangle to be? (Must be an odd number) "))
x = "+"
gap = " "
middle = x
spaces = ""
for i in range(int(base_length / 2)):
    for y in range(int((base_length / 2) - i)):
        spaces += " "
    print(spaces + middle + spaces)
    middle = x + gap + x
    gap += "  "
    spaces = ""
print(spaces + middle + spaces)
x = "+"
gap = " "
for i in range(int(base_length / 2) - 1):
    space_additions = (base_length / 2) - i
    for y in range(int(space_additions - 2)):
        gap += "  "
    spaces += " "
    middle = x + gap + x
    print(spaces + middle + spaces)
    x = "+"
    gap = " "
print(spaces + " " + x + spaces)
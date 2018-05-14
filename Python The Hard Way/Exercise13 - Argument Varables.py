from sys import argv
# tells the script what paramaters to accept at runtime these paramaters are
# also reffered to as arument variables
script, varFirst, varSecond, varThird = argv

print(f"the script is called:{script}")
print("this is the first", varFirst)
print("this is the second", varSecond)
print("this is the third", varThird)

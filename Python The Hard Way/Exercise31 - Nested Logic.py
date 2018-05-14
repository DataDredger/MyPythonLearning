# exercise using basic logic statements to build a choose your own adventure
# using the 3 quotes will allow the string to cross line breaks

print("""there are two old dorrs in front of you one with with a giant blue  1
and then some more text""")
door = input("> ")

if door == "1":
    print("""truely a wise coice, you reach a beat stand on the side of the road
    where an odd beat farmer farmer apporaches you and asks QUESTION! brown
    bear or black bear, what say you""")
    beartype = input("> ")
    if beartype == "brown":
        print("incorrect! you are pre-fired!")
    elif beartype == "black":
        print("incorrect! you are pre-fired!")
    elif beartype == "there are really two schools of thoughts":
        print("there just might be hope for you yet!")
    else:
        print("what kind of answer is that?!?!")
elif door == "2":
    print("what an even choice")
else:
    "you aren't very good at following instructions are you?"

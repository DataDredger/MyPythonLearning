mystring = 'hello world'
print(mystring)
mystring[::-1]

# Getting my concatanation on like badass

name = 'sam'

lastletters = name[1:]
print('p'+lastletters)


# basic string methods
lastletters.upper()
lastletters.lower()
# splits the string based on the deliminatior passed to the method
mystring.split('o')

# getting ready to do some fancy stuff with printing
# first up we wiiil use the .format method

'string here{} and then also here {}'.format('name1', 'name2')

# inserting strings via indexing
print('{0} {3} {2} {1}'.format('the', 'fox', 'brown', 'quick'))

# inserting strings via key words
print('{t} {q} {b} {f}'.format(t='the', q='quick', b='brown', f='fox'))

# time for some float formatting witht the formatting function woohoo!!
# formating in floating point is width and then percision
result = 100/777
print('the result was {r:1.3f}'.format(r=result))mn

# formatting strings using the f string methods
name = 'jose'
print(f'hello his name is {name}')

# homework for formatting strings
print('{}'.format('Python rules!'))


# time to get started with lists

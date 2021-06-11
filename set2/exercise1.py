"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think it will declare a variable called some_words
# and it'll put a list of strings into it
some_words = ['what', 'does', 'this', 'line', 'do', '?']

# ngl i have no idea as i'm barely grasping the concepts currently. but once it runs it makes sense 
for word in some_words:
    print(word)

for x in some_words:
    print(x)

print(some_words)

# This was interesting as len is the grasshopper equivalent of list length
if len(some_words) > 3:
    print('some_words contains more than 3 words')

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()

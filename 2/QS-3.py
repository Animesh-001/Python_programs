'''Write a Python function which accepts a string and
returns a string made of the first 2 and the last 2
characters of the given string. If the string length
is less than 2,return-1.

 Note: If the string length is equal to 2,
 consider the 2 characters to be the first
 as well as the last two characters.'''

def task(str):
    if len(str)>1:
        return str[:2]+str[-2:]
    else:
        return -1

str = input("Enter a string:")
print(task(str))
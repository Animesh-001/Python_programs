'''Write a python program to display all the common characters
between two strings. Return -1 if there are no matching

Note: Ignore blank spaces if there are any. Perform case
sensitive string comparison wherever necessary.'''

str1="I like Python"
str2="Java is a very popular language"
st = ""
for i in str1:
    if i==' ':
        continue
    for j in str2:
        if i==j:
            st=st+i

print(*set(st))
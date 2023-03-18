#list comprehension

#for loop version
result=[]
l1=4
for i in range(l1):
    result.append(i)
print(result)

#list comprehension version
print([i for i in range(l1)])

#for loop version-->odd elements
result1=[]
for i in range(l1):
    if i%2!=0:
        result1.append(i)
print(result1)
print([i for i in range(l1)if i%2!=0])

#another one
result2=[]
for i in range(l1):
    if i%2!=0:
        result2.append(i)
    else:
        result2.append(i**2)
print(result2)
print([i if i%2!=0 else i**2 for i in range(l1)])
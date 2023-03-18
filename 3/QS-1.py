mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
arr=[]
for i in list_b:
    arr.append((i,mylist.index(i)))
print(arr)
t=[*set(arr)]
print("removing duplicate tuples:",t)

#print in dict
result={}
for i in list_b:
    result[i]=mylist.index(i)
print("Dictionary:",result)
print({i:mylist.index(i) for i in list_b})



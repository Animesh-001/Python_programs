'''list is mutable'''
l1=[1,'sumi',True,'a',3.2]
print(l1)
print(type(l1))
print(l1[0])
print(l1[-1])
l1[0]=100
print(l1)
l1.append("situ")
print(l1)
l1.pop()
print(l1)
l1.reverse()
print(l1)
l1.insert(1,"Sanu")  # insert any value
print(l1)
print(l1*3)
l2=["Ani","sumi","situ","sanu","Rohit"]
l2.sort()
print(l2)

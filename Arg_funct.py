#no of variable we can add in the function
def f4(*var):
    for i in var:
        print(i,end=" ")

f4(10,20)
print()
def add(*var):
    sum=0
    for i in var:
        sum=sum+i
    return sum

print("sum is",add(10,20))
print("sum is",add(13,15,25,43))
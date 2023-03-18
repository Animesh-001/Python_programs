# case-1
n=int(input("enter a no:"))
print("even no")
for i in range(1,n+1):
    if i%2==0:
        print(i)

print("odd no:")
for i in range(1, n + 1):
    if i%2!=0:
        print(i)

# case-2
print("odd no")
for i in range(1,51,2):
    print(i)
'''Find the number of distinct subarrays in an array of position integers
such that the sum of the subarray is an odd integer, two subarray are
consisdered different if they start or end at different index input.'''

n1=int(input())
n2=int(input())
arr=[i for i in range(n1,n2+1)]
print(arr)
result=[]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        result.append(arr[i:j+1])
print(result)
print()
print("Method-2")
result1=[arr[i:j+1] for i in range(len(arr))
        for j in range(i,len(arr))]
print(result1)

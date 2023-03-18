'''Write a python function, check_double (number) which accepts a whole number and
returns True if it satisfies the given conditions.

1. The number and its double should have exactly the same number of digits.
2. Both the numbers should have the same digits, but in different order.

Otherwise it should return False.

Example: If the number is 125874 and its double, 251748,
contain exactly the same digits, but in a different order.'''

'''Method-1'''

print("Method-1")
def task(str1):
    count=0
    c=int(str1)+int(str1) # c=str(int(str1)+int(str1)) or c=int(str1)*2
    d=str(c)
    for i in range(len(str1)):
        for j in range(len(d)):
            if str1[i]==d[j]:
                count=count+1
    if count==len(str1):
        return True
    else:
        return False

print(task("125874"))

print()
'''Method-2'''

print("Method-2")
def check_double(number):
    num1=str(number*2)
    number1=str(number)
    count=0
    for x in number1:
        if x in num1:
            count+=1
        else:
            return False
            break
    if count==len(number1):
        return True

print(check_double(125874))
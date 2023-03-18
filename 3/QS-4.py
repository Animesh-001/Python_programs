def sumSqrDigit(num):
    X = int(num)
    N = 0
    while(X>0):
        rev = X%10
        rev *= rev
        N += rev
        X = X//10
    return N
def rotateRight(string):
        n=''
        x=''
        n+=string[-1]
        x+=string[:-1:]
        x=n+x
        return x
def rotateLeft(string):
        n=''
        x=''
        n+=string[:2]
        x+=string[2:]
        x+=n
        return x
series = input().split(':')
for i in series:
    if(i.isdigit()):
        n=i
    else:
        stg=i
if(sumSqrDigit(n)%2==0):
    print(rotateRight(stg))
else:
    print(rotateLeft(stg))
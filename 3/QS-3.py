'''Input a string of comma seperated numbers. the number 5 and 8 are
present in the list. Assume that 8 always comes after 5.
case1:num1= add all the numbers which do not lie
between 5 output sum of num1 and num2 example and 8 in the input
case2: num2 = number formed by concatenating all numbers from 5 to 8
1) 3,2,6,5,1,4,8,9
num1=3+2+6+9=20
num2=5148
o/p=5248+20=5168  '''

n=list(map(int,input().split(",")))
add=sum(n[:n.index(5)])+sum(n[n.index(8)+1:])
print("num1=",add)
l=n[n.index(5):n.index(8)+1]
num=""
for i in l:
    num+=str(i)
print("num2=",int(num)+add)

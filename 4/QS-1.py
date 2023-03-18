'''Write a python function, nearest_palindrome ()
which accepts a number and returns the nearest
palindrome greater than the given number
#i/p:-999
#o/p:-1001'''
def nearest_palindrome(number):
    number=number+1 # 1000
    s=str(number)
    if s == s[::-1]: # false
        return number
    else:
        return nearest_palindrome(number)
number=int(input())
print(nearest_palindrome(number))
'''n=input(input())
while(n!=0):
    t = str(n)
    if t[:]==t[::-1]:
        print()'''

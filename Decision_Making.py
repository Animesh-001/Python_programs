n=int(input())
if n%3==0 and n%5==0:
    print("multiple 3 and 5 both")
elif n%3==0:
    print("multiple of 3")
elif n%5==0:
    print("multiple of 5")
else:
    print("invalid input")

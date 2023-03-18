def f1(n1,n2,n3):
    print("value1:", n1, "value2:", n2,"value3:", n3)
f1(5, 8, 10)  # it will give type error if we don't give 3 argument(positional argument)
print()
f1(n1=1, n2="Ani", n3=99.99)  # keyword argument
print()
f1(n3=14.5, n1=False, n2="Rohit")

print()
print("Student Detail:")
# Default argument
def f2(rollno,name,branch,collegename="GIET"):
    print(rollno,name,branch,collegename)

f2("20EEE001", "Animesh Nayak", "EEE")
f2("20EE004", "Deepak Mohanty", "EE")
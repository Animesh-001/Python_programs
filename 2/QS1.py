'''Write a python function which accepts a sentence and finds the number
of letters and digits in the sentence.It should return a list in which
the first value should be letter count and second value should be digit count.
Ignore the spaces or any other special character in the sentence'''

'''method-1'''
print("METHOD-1")
def funct(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return [l_count,d_count]

print(funct("Infosys 123"))

print()

'''method-2(when space is not present in a string)'''

print("METHOD-2")
alpha,string,l=0,"Infosys 12345",[]
for i in string:
    if i.isalpha():
        alpha+=1
t=string.count(" ")
digit=len(string)-(alpha+len(str(t)))
l.append(alpha)
l.append(digit)
print(l)

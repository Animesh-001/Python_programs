no_of_1=int(input())
no_of_5=int(input())
amount_to_be_made=int(input())
count=0
for i in range(no_of_1+1):
    for j in range(no_of_5 + 1):
        if (i*1+j*5)==amount_to_be_made:
            print(i,j)
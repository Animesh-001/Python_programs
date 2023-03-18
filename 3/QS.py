'''mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for loop--odd_>square it
even-->cube it'''


mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for i in mat:
    for j in i:
       if j%2==0:
           result.append(j**3)
       else:
           result.append(j**2)
print(result)

#list comprehension(method-2)

print([j**2 if j%2!=0 else j**3 for i in mat for j in i])

#print in list wise
result1=[]
mat1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for row in mat1:
    row_data=[]
    for ele in row:
        if ele%2!=0:
            row_data.append(ele**2)
        else:
            row_data.append(ele**3)
    result1.append(row_data)
print(result1)

#list comprehension
print([[ele**2 if ele%2!=0 else ele**3 for ele in row]
       for row in mat1])
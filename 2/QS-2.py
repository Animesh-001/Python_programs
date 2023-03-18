'''Write a python function, find_pairs_of_numbers() which
accepts a list of positive integers with no repetitions and
returns count of pairs of numbers in the list that adds up to n
The function should return 0, if no such pairs are found in the list.'''

def find_pairs_of_numbers(num_list,n):
    count=0
    for x in num_list:
        index=num_list.index(x)+1  # index=0+1=1
        for y in range(index,len(num_list)): # [2,7]
            if x+num_list[y]==n:
                count+=1
    return count
num_list=[3,4,1,8,5,9,0,6]
n=9
print("No of pair of sum of 2 no is:",find_pairs_of_numbers(num_list,n))
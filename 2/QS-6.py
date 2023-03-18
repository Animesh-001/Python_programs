'''A teacher is in the process of generating few reports based on
the marks scored by the students of her class in a project | assessment.

Assume that the marks of her 10 students are available in a
tuple. The marks are out of 25.

Write a python program to implement the following functions:
1.find_more_than_average(); Find and return the percentage of students
who have scored more than the average mark of the class.

2. generate_frequency(): Find how many students have scored the same marks.
For example, how many have scored 0, how many have scored 1,
how many have scored 3... how many have scored 25.
The result should be populated in a list and returned.

3.sort_marks(): Sort the marks in the increasing order from 0 to 25.
The sorted values should be populated in a list and returned'''

list_of_marks=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_avg():
    global list_of_marks
    marks=0
    count=0
    for x in list_of_marks:
        marks+=x
    avg=marks/len(list_of_marks)
    for x in list_of_marks:
        if x>avg:
            count+=1
    percentage=(count*100)/len(list_of_marks)
    return percentage

def generate_frequency():
    freq=[]
    global list_of_marks
    for x in range(26):
        count=0
        for y in list_of_marks:
            if x == y:
                count+=1
        freq.append(count)
    return freq

def sort_marks():
    global list_of_marks
    list_of_marks=sorted(list_of_marks)
    return list_of_marks

print(find_more_than_avg())
print(generate_frequency())
print(sort_marks())

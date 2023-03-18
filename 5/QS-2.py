'''A university wants to automate their admission process.
Students are admitted based on marks scored in a qualifying exam.
A student is identified by student id, age and marks in Data are valid,
if:
Age is greater than 20
Marks is between 0 and 100 (both inclusive)
A student qualifies for admission, if
Age and marks are valid and Marks is 65 or more

Write a python program to represent the students
seeking admission in the university.

RULES TO FOLLOW:
The details of student class are given below.
Class name: Student
--Attributes: (private)
               student_id
               marks
               age
Methods
(public)init()
     Create and initialize all instance variables to None
validate_marks()
     If data is valid, return true. Else, return false
validate_age()
     check_qualification()    Validate marks and age.
If valid, check if marks is 65 or more.
   if so return true
   else return false
   else return false
setter methods Include setter methods for all instance variables to get its values
getter methods Include getter methods for all instance variables to get its values


Continuing with the previous scenario, a student eligible for admission has to choose a course and pay the fees for it.
If they have scored more than 85 marks in qualifying exam, they get 25% discount on fees.

Valid course ids and fees are given below:

course id   fees
1001        25575.0
1002        15500.0'''


class Student:
    def _init_(self):
        self.__student_id = None
        self.__age = None
        self.__marks = 0
        self.__course_id = None
        self.__fees = None

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def get_course_id(self):
        return self.__course_id

    def get_fees(self):
        return self.__fees

    def validate_marks(self):
        if (self.__marks >= 0 and self.__marks <= 100):
            return True
        else:
            return False

    def validate_age(self):
        if (self.__age > 20):
            return True
        else:
            return False

    def check_qualification(self):
        if (self.__age > 20 and self.__marks >= 65 and self.validate_marks()):
            return True
        else:
            return False

    def choose_course(self, course_id):
        if (self.check_qualification() and (course_id == 1001 or course_id == 1002)):
            self.__course_id = course_id
            if (course_id == 1001):
                self.__fees = 25575.0
            elif (course_id == 1002):
                self.__fees = 15500.0
            if (self.__marks > 85):
                self.__fees = self.__fees - (self.__fees * 25 / 100)
            return True
        return False


maddy = Student()
maddy.set_student_id(1001)
maddy.set_age(21)
maddy.set_marks(84)
if (maddy.check_qualification()):
    print("Student has qualified")
    if (maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")

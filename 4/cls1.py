''''class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self, num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())  #  10
obj.set_num(15)
print(obj.get_num())''' # 15

'''pr-1'''
class Customer:
    def __init__(self):
        self.cust_id=100 # self is mandatory

c1=Customer()
print(c1.cust_id)
print()
'''pr-2'''
class Customer:
    def __init__(self,id):
        self.id=100  # value assigned to id

c1=Customer(200)
print(c1.id)
print()
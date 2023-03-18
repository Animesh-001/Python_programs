'''class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material
s1=Shoe(1000, "Nike")
print(s1)
print(s1.price,s1.material)
print("the unique id of the object",id(Shoe))'''
class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material
    def __str__(self):
        return "Shoe with price: " + str(self.price) + "\nand material: " + self.material
s1 = Shoe(1000, "Nike")
print(s1)
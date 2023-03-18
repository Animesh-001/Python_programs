'''
PizzaForYou is a pizza store which sells different kinds of pizzas based on customer's order.40 min
Customer can either collect the order in person or opt for a door delivery.
Write a python program based on the class diagram given below.
Customer class:
validate_quantity(): A customer can order 1 to 5 pizzas
If quantity is valid, return true. Else return false
Pizzaservice class:
Initialize static variable counter to 100
Attribute, additional_topping is a boolean value which indicates whether additional topping is required or not.
True – additional topping is required, False – additional topping is not required
validate_pizza_type(): Customers can order "small" or "medium" type pizzas
If pizza type is valid, return true. Else return false
calculate_pizza_cost(): Calculate pizza cost
Validate pizza type and quantity
If valid,
Identify pizza cost based on details mentioned in the table
Set attribute, pizza_cost with the calculated pizza cost
Auto-generate service_id starting from 101 prefixed by first letter of pizza type. Example – S101, s102, m103, S104, M105 etc
If invalid, set pizza_cost to -1
PizzaType	Cost/Pizza(in Rs)	Additional topping cost/Pizza       (in Rs), if applicable
Small	150	35
Medium	200	50
Door delivery class:
validate_distance_in_kms(): Minimum distance for door delivery is 1km and maximum is 10kms
Validate distance_in_kms
If valid, return true. Else, return false
calculate_pizza_cost: Calculate pizza cost
Validate distance in kms
If valid,
Calculate pizza cost (Hint: Invoke overridden method in parent class)
If pizza_cost is not -1, identify delivery charge based on details mentioned below and add it to attribute, pizza_cost
Distance in kms	Delivery Charge in km(in Rs)
For first 5 kms	5
For remaining 5 kms	7
Else, set pizza_cost to -1
Note: Perform case insensitive string comparison
For testing:
Create objects of Pizzaservice and Doordelivery classes
Invoke calculate_pizza_cost() on Pizzaservice and Doordelivery objects
Display the details
'''

class Customer:
    def __init__(self, customer_name, quantity):
        self.__customer_name = customer_name
        self.__quantity = quantity

    def get_customer_name(self):
        return self.__customer_name

    def get_quantity(self):
        return self.__quantity

    def validate_quantity(self):
        if self.__quantity >= 1 and self.__quantity <= 5:
            return True
        return False


class Pizzaservice:
    counter = 100

    def __init__(self, customer, pizza_type, additional_topping=False):
        self.__service_id = None
        self.__customer = customer
        self.__pizza_type = pizza_type
        self.__additional_topping = additional_topping
        self.pizza_cost = None

    def validate_pizza_type(self):
        if self.__pizza_type.lower() in ["small", "medium"]:
            return True
        return False

    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            Pizzaservice.counter += 1
            if self.__pizza_type.lower() == "small":
                self.pizza_cost = 150 * self.__customer.get_quantity()
                if self.__additional_topping == True:
                    self.pizza_cost += 35 * self.__customer.get_quantity()
                self.__service_id = "S" + str(Pizzaservice.counter)
            if self.__pizza_type.lower() == "medium":
                self.pizza_cost = 200 * self.__customer.get_quantity()
                if self.__additional_topping == True:
                    self.pizza_cost += 50 * self.__customer.get_quantity()
                self.__service_id = "M" + str(Pizzaservice.counter)
        else:
            self.pizza_cost = -1

    def get_service_id(self):
        return self.__service_id

    def get_customer(self):
        return self.__customer

    def get_pizza_type(self):
        return self.__pizza_type

    def get_additional_topping(self):
        return self.__additional_topping

class Doordelivery(Pizzaservice):
    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        super().__init__(customer, pizza_type, additional_topping)
        self.__delivery_charge = None
        self.__distance_in_kms = distance_in_kms

    def validate_distance_in_kms(self):
        if self.__distance_in_kms >= 1 and self.__distance_in_kms <= 10:
            return True
        return False

    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if self.pizza_cost != -1:
                if self.__distance_in_kms <= 5:
                    self.__delivery_charge = self.__distance_in_kms * 5
                else:
                    self.__delivery_charge = 25 + (self.__distance_in_kms - 5) * 7
                self.pizza_cost += self.__delivery_charge
        else:
            self.pizza_cost = -1

    def get_delivery_charge(self):
        return self.__delivery_charge

    def get_distance_in_kms(self):
        return self.__distance_in_kms
c=Customer("Animesh",4)
p=Pizzaservice("Animesh","medium",False)
d=Doordelivery("Animesh","medium",False,5)
print("Customer name:",c.get_customer_name())
print("Quantity is:",c.get_quantity())
print("valid quantity:",c.validate_quantity())
print("valid pizza type:",p.validate_pizza_type())
print("valid distance in kms:",d.validate_distance_in_kms())

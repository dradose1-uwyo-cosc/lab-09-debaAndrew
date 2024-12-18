# Andrew Deba
# UWYO COSC 1010
# 11/14/2024
# Lab 09
# Lab Section: 18
# Sources, people worked with, help given to: https://www.geeksforgeeks.org/default-arguments-in-python/, https://www.geeksforgeeks.org/g-fact-34-class-or-static-variables-in-python/


# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.

class Pizza:
    def __init__(self, size = 10, sauce = "red"):
        self.size = size
        self.sauce = sauce
        self.toppings = ["cheese"]

    def get_size(self):
        if type(self.size) == "int":
            return self.size
        if not (self.size).isnumeric() or int(self.size) < 11:
            self.size = "10"
        return int(self.size)
    
    def set_size(self,size):
        self.size = size

    def get_sauce(self):
        #if self.sauce == "":
            #return "red"
        return self.sauce
    
    def get_toppings(self):
        return self.toppings
    
    def get_number_of_toppings(self):
        return len(self.get_toppings())
    
    def add_topping(self, topping_name):
        self.toppings.append(topping_name)

class Pizzeria:
    PRICE_PER_INCH = 0.6
    PRICE_PER_TOPPING = 0.3
    def __init__(self):
        self.orders = 0
        self.pizzas = []

    def get_Price(self, pizza_order):
        return (self.get_Price_size(pizza_order) + self.get_Price_toppings(pizza_order))

    def get_Price_size(self, pizza_order):
        return (pizza_order.get_size()*Pizzeria.PRICE_PER_INCH)
    
    def get_Price_toppings(self, pizza_order):
        return (len(pizza_order.get_toppings())*Pizzeria.PRICE_PER_TOPPING)
        #Assuming cheese counts towards the topping price

    def place_order(self):
        size_input = input("What size of pizza would you like? Our smallest option is 10 inches.")
        sauce_input = input("What sauce would you like on your pizza?")
        
        pizza_order = Pizza(size_input, sauce_input)

        while True:
            topping_input = input("Next topping?")

            if topping_input == "":
                break

            pizza_order.add_topping(topping_input)

        print(f"You have selected to order a {pizza_order.get_size()} inch pizza with {pizza_order.get_sauce()} sauce{self.format_toppings(pizza_order)}.")

        self.pizzas.append(pizza_order)
        self.orders += 1
        return pizza_order

    def get_num_orders(self):
        return self.orders
    
    def get_reciept(self, pizza_order):
        print(f"You ordered a {pizza_order.get_size()} inch for ${self.get_Price_size(pizza_order)}.")
        print(f"You ordered {pizza_order.get_number_of_toppings()} topping for ${self.get_Price_toppings(pizza_order)}.")
        print(f"Your total price is ${self.get_Price(pizza_order)}")

    def format_toppings(self, pizza_order):
        toppings_string = ""
        count = 1
        for i in (pizza_order.get_toppings()):
            if count != 1 and count == (pizza_order.get_number_of_toppings()):
                toppings_string = toppings_string + (", and ")
            elif count == 1 and count == (pizza_order.get_number_of_toppings()):
                toppings_string = toppings_string + (" and ")
            else:
                toppings_string = toppings_string + (", ")

            toppings_string = toppings_string + i
            count += 1

        return toppings_string

pizza_shop = Pizzeria()

while True:
    if input("Would you like to place an order?").upper() == "YES":
        final_pizza = pizza_shop.place_order()
        pizza_shop.format_toppings(final_pizza)
        pizza_shop.get_reciept(final_pizza)
    else:
        break

print(f"You have sold {pizza_shop.get_num_orders()} pizza(s) today.")


# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.


# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.





















# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""
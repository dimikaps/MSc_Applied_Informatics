from datetime import datetime, timedelta
from random import choice, randint
import os
import csv
from shop import Shop

class Order():

    sum_orders = Shop.load_orders()
    id = len(sum_orders) + 1

    def __init__(self):
        self.datetime = datetime.now()
        self.id = Order.id
        Order.id += 1  # After the creation of an object, += adds 1 to the id, so the next order take the next id
        self.customer_name = self.set_customer_name()
        self.arrival = self.datetime + timedelta(days=7)  # Timedelta is a function from datetime by which we can add days, in order to canculate the estimated arrival
        self.product = choice(["Sofa", "Chair", "Table"])
        self.quantity = self.set_quantity()
        self.price = randint(200, 500)
        self.tax = choice([0.13, 0.24])
        self.cart = (self.price + self.price * self.tax) * self.quantity
        self.status = "Active"
        Order.auto_save(self)  # auto_save method is called every time we create an object

    def __str__(self):
        return f"Order(id={self.id}, customer='{self.customer_name}', product='{self.product}', quantity={self.quantity}, cart={self.cart:.2f}, datetime={self.datetime}, arrival={self.arrival})"

    def set_customer_name(self):  # setter function to customer's name
        while True:    
            user_input = input("Type customer's name: ")
            if user_input.replace(" ","").isalpha():  # with .replace() I remove every space to check that only letters remain and isalpha() returns True or False based on the user_input
                listed_name = user_input.strip().split()  # .strip() removes right and left spaces (ex. "   DIMItris   kaPSOUris  ") and .split() splits the string to whitespaces and adds every word in a list
                formated_customers_name = (" ").join(listed_name).title()  # .title() formats every word to a Title Formation (ex. "DIMItris kaPSOUris" -> "Dimitris Kapsouris")
                self.customer_name = formated_customers_name
                break
            else:
                print("Invalid Input")
        return self.customer_name

    def set_quantity(self):  # setter function to quantity
        while True:
            try:
                self.quantity = int(input(f"How many {self.product} do you want to add to your cart? "))
                return self.quantity
            except ValueError:
                print("Invalid Input, quantity has to be an integer")

    def auto_save(self):
        file_exists = os.path.exists("orders.csv")  # checks if the path exists | if "orders.csv" exists on the root folder of this file it will return True
        with open("orders.csv", "a", newline="") as f:
            orders_writter = csv.writer(f)
            if not file_exists:  # if the file doesn't exists, an empty file will be created, so in the next line we create the first line as a header
                orders_writter.writerow(["datetime", "id", "customer_name", "arrival", "product", "quantity", "price", "tax", "cart", "status"])
            orders_writter.writerow([self.datetime, self.id, self.customer_name, self.arrival, self.product, self.quantity, self.price, self.tax, self.cart, self.status])

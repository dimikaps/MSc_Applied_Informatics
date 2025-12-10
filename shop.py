import csv
import re


class Shop():

    @staticmethod  # Static method decorator states that this method can work without 'cls' or 'self'
    def load_orders():  # Load method to store all the orders from the csv file to a list, in order to extract data later
        loaded_orders = []
        try:
            with open("orders.csv", "r", newline="") as f:
                orders_reader = csv.DictReader(f)
                for row in orders_reader:
                    loaded_orders.append(row)
        except FileNotFoundError:
            print("Couldn't load 'orders.csv'")
        finally:
            return loaded_orders

    @staticmethod
    def search_assistant():  # An assistant method to validate the parameters for a search
        while True:    
            print("By which field do you want to search for an order? \n"
                  "Type N for Name\n"
                  "Type I for ID\n"
                  "Type D for Datetime\n"
                  "Type S for Status\n"
                  "Type A for Arrival\n")
            user_input = input(">>> ").strip().upper()  # .upper() turns the input to UPPERCASE
            if user_input == "N":
                search_field = "customer_name"
                break
            elif user_input == "I": 
                search_field = "id"
                break
            elif user_input == "D":
                search_field = "datetime"
                break
            elif user_input == "A":
                search_field = "arrival"
                break
            elif user_input == "S":
                search_field = "status"
                break
            else:
                print("Invalid Input")

        value = input(f"Type the {search_field} you want to search (full or a part of it): ")
        return search_field, value
    
    @staticmethod
    def search_orders(search_field, value):  # Searching method on the csv file based on the parameters
        search_results = []
        try:
            with open("orders.csv", "r", newline="") as f:
                order_reader = csv.DictReader(f)
                for row in order_reader:
                    if re.search(value, row[search_field], re.IGNORECASE):
                        search_results.append(row)
        except FileExistsError:
            print("There is no file called 'orders.csv'")
        return search_results
            
    @staticmethod        
    def list_customers(loaded_orders):  # A method to list every customer based on the loaded orders
        customers = []    
        for order in loaded_orders:
            if order["customer_name"] not in customers:
                customers.append(order["customer_name"])
        return customers

    @staticmethod
    def data_extraction(customers, loaded_orders):  # Search method for the best customer
        max_carts = 0
        best_customer = None
        for customer in customers:
            customer_carts = 0
            for order in loaded_orders:
                if customer == order["customer_name"] and order["status"] == "active":
                    customer_carts += int(order["cart"])
            if customer_carts > max_carts:
                max_carts = customer_carts
                best_customer = customer
        return best_customer
    
    @staticmethod
    def manual_save(loaded_orders):
        fieldnames = ["datetime", "id", "customer_name", "arrival", "product", "quantity", "price", "tax", "cart", "status"]
        with open("orders.csv", "w", newline="") as f:
            orders_writter = csv.DictWriter(f, fieldnames=fieldnames)
            orders_writter.writeheader()
            orders_writter.writerows(loaded_orders)

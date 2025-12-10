from order import Order
from shop import Shop


def main():

    while True:

        print("Welcome to Order Manager app v1.0:\n"
              "1. Place New Order\n"
              "2. Cancel Order\n"
              "3. Preview Orders\n"
              "4. Search For The Best Customer\n"
              "0. Exit Programm")
        
        user_input = input("Press the corresponding number to what you want to do: ")

        if user_input == "1":
            new_order = Order()
            print(new_order)

        elif user_input == "2":
            loaded_orders = Shop.load_orders()
            search_field, value = Shop.search_assistant()
            for order in loaded_orders:
                if order[search_field] == value:
                    order["status"] = "Canceled"
            Shop.manual_save(loaded_orders)

        elif user_input == "3":
            search_field, value = Shop.search_assistant()
            search_results = Shop.search_orders(search_field, value)
            print(search_results)

        elif user_input == "4":
            loaded_orders = Shop.load_orders()
            customers = Shop.list_customers(loaded_orders)
            best_customer = Shop.data_extraction(customers, loaded_orders)
            print(best_customer)

        elif user_input == "0":
            break

        else:
            print("Invalid Input\n")

if __name__ == "__main__":
    main()

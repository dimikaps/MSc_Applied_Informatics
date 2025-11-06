while True:  # I used a while loop to continuously ask the user for a valid number
     try:  # I used try/except to catch possible errors
         yearly_income = (input("Type your yearly income: ")) 
         yearly_income = float(yearly_income  # At this point, I use string methods to format the user input correctly and then convert it to a float
                               .strip()  
                               .replace(" ", "")
                               .replace(".", "")
                               .replace(",", "."))

         if yearly_income < 0:
              raise ValueError("Income can't be negative.")
         break  # if the number is valid with the 'break' we exit the while loop 
     except ValueError as e:
          print("Give a valid number please.", e)  # I used ValueError because the conversion to float in line 4 can only raise ValueError

if yearly_income <= 10000:  # This is the main program that canculates the tax and prints the results
    tax = 0
elif yearly_income <= 20000:
     tax = (yearly_income - 10000) * 10/100
elif yearly_income <= 40000:
     tax = (yearly_income - 20000) * 20/100 + 10000 * 10/100
else:
    tax = (yearly_income - 40000) * 30/100 + 20000 * 20/100 + 10000 * 10/100

net_income = yearly_income - tax
print(f"Your tax based on your yearly income ({yearly_income:.2f}) is {tax:.2f}. Your net income after taxes comes to {net_income:.2f}.")  # The ":.2f" format shows the value with two decimal places


'''
Create a program that calculates income tax for individuals.
The program should ask the user to enter their annual income, and then calculate the tax based on the following tax scale:

Income up to €10,000: 0% tax

Income from €10,001 to €20,000: 10% tax on the amount over €10,000

Income from €20,001 to €40,000: 20% tax on the amount over €20,000

Income over €40,000: 30% tax on the amount over €40,000

The program should then display:

the total tax amount the user must pay, and

the net income after subtracting the tax.

Make sure to use error handling with try-except blocks to check for valid user input (e.g., if the user enters something that is not a number).
'''

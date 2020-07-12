# Task Number : 1
# File Name : finance_calculators.py
# Written by : Shaakir Caroto
# Date Written : 11/02/2020
# The function of this program : This program is a finance calculator

# Importing the math libary to help with the calculations
import math

# Displaying so information for the user to help with the picking of function
print("Choose either \'investment\' or \'bond\' from the menu below to proceed :")
print("investment \t \t - to calculate the amount of interest you'll earn on interest")
print("bond \t \t \t - to calculate the amount you'll have to pay on a home loan")

# Requesting input from the user to see which method they would like to use 
investment_or_bond = input("Which calculate would you like to do a investment or a bond calculation ? ").lower()

# Use an if else statement and elif to see which methods to call on 
if investment_or_bond == "investment":
    # If the users inputs investment the program will use this method
    # Requesting the information for the user to help in the calculation and casting them into flaot varibles
    dep_amount = float(input("What is the amount you are depositing ? "))
    interest_rate = float(input("What is your interest rate (please enter the number only e.g 8 and not 8%) ? "))
    no_of_years = float(input("What is the number of years you are investing for ? "))
    # Requesting input to see which methond the user would like to use
    interest = input("Choose either simple or compound for the interest formula being used ? ").lower()
    if interest == "simple":
        # If the user inputs "simple" the program will call this method
        # interest is divide by 100 to change into a decimal to be used in the calculation
        interest_rate = interest_rate / 100
        # Calculating the total amount of the investment 
        total_amount = dep_amount * (1 + interest_rate * no_of_years)
        # Displays the total amount with two decimals
        print(f"The total amount including interest : R{total_amount:.2f}")
    elif interest == "compound" :
        # If the user inputs "compound" the program will call this method
        # interest is divide by 100 to change into a decimal to be used in the calculation
        interest_rate = interest_rate / 100
        # calculating the first part of the calculation to make the math easier
        # Using the pow function from the math libary 
        interest_amount =  math.pow((1 + interest_rate), no_of_years)
        # Times the calculated amount "interest_amount" and the inputted amount "dep_amount"
        total_amount = dep_amount * interest_amount
        # Displaying the total amount with two decimals 
        print(f"The total amount including interest : R{total_amount:.2f}")
    else:
        # if the input is not investment or bond the program will display the following statement
        print("Please enter invesment or bond")
elif investment_or_bond == "bond" :
    # If the user inputs "bond" the program will call on this method
    # Requesting information from the user to help in the calculation and casting them into float varibles
  present_values = float(input("What is the present of your property ? "))
  interest_rate = float(input("What is your interest rate (please enter the number only e.g 8 and not 8%) ? "))
  no_of_months = float(input("What is the number of months you need to complete payment ? "))\
    # Dividing interest rate by 100 and by 12 to get the monthly interest rate
  interest_rate = interest_rate / 100
  interest_rate = interest_rate / 12
  # 0 - no_of_months to get the value to be a negitive float varible 
  no_of_months = 0 - no_of_months
  # The Calculation is broken up into three parts
  # timesing interest_rate and present_values to get the total amount 
  total_amount = (interest_rate * present_values )
  # Calculating the interest_amount by using the pow from the math libary and inputted values from the user
  interest_amount = 1 - math.pow((1 + interest_rate), no_of_months)
  # dividing the total_amount by interest_amount to the final total_amount
  total_amount = total_amount / interest_amount
  # Displaying the total_amount with two decimals
  print(f"The repayment amount : R{total_amount:.2f}")
else:
    # if the inputs are not investment or bond this message will display
    print ("Please input the correct answers please as we does not know function you would like to use")
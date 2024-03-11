import math

# PSEUDOCODE:

# print the investment string using variable investment
# print the bond string using the variable bnd
# ask user to choose between investment and bond from the above menu
# if user inputs investment:
    # ask user to input deposit
    # ask user to input rate and divide the rate by 100
    # ask user how many years to invest
    # ask user to choose between simple or compound interest
    # if user inputs simple:
        # calculate using the 'simple' formula provided and print the total amount
    # else if user inputs compound:
        # calculate using the 'compound' formula provided and print the total amount
# else if user inputs bond:
    # ask user to enter the value of the house
    # ask user to enter the interest rate, divide the rate by 100 and again by 12
    # ask the user how many months their planning to repay the house
    # calculate using the 'bond' formula provided and print the total amount
# else:
    # print an error message if user's enter a wrong input



print("investment - to calculate the amount of interest you'll ear on your investment")
print("bond \t - to calculate the amount you'll have to pay on a home loan")
print()

investment = input("Please enter 'investment' or 'bond' from the menu above: ")
investment = investment.lower()

print()

# This is the if statement asking the details from the user

if investment == "investment":
    deposit = int(input("How much would you like to deposit?\t"))

    print()

    rate = int(input("Please enter the interest rate: ")) / 100

    print()

    years_plan = int(input("How many years are you planning to invest?\t"))
    print()

    interest = input("Please choose between 'simple' or 'compound' interest:\t")
    interest = interest.lower()
    print()

# This is the if statement between simple and compound interest

    if interest == "simple":    
        s_interest = int(deposit * (1 + rate * years_plan))
        print(f"Your 'simple' interest calculaton is: {s_interest}")

    elif interest == "compound":
        c_interest = int(deposit * math.pow((1 + rate),years_plan))
        print(f"Your 'compound' interest calculation is: {c_interest}")

# this is the else if statement for the bond calculator

elif investment == "bond":
    house_value = int(input("Please enter the present value of the property:\t"))

    print()

    rate = (int(input("Please enter the interest rate:\t")) / 100) / 12

    print()

    months_plan = int(input("Please specify how many months you are planning to repay:\t"))

    print()

    monthly_rpmnt = int((rate * house_value) / (1 - (1 + rate)**(- months_plan)))
    print(f"This is the amount you have to repay each months: {monthly_rpmnt}")

# This is the error message in case of invalid inpup

else:
    print("Sorry this is an invalid input!")

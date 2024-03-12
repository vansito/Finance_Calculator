import math

# Functions

def inv_calculations():
    """
    a function that calculates two diffrent interest
    simple and compound
    """
    deposit = int(input("\nHow much would you like to deposit?\t"))

    rate = int(input("\nPlease enter the interest rate:\t")) / 100

    years_plan = int(input("\nHow many years are you planning to invest?\t"))

    answer = True
    while answer:

        interest = input("\nPlease choose between 'simple' or 'compound' interest:\t").lower()

        if interest == "simple":
            s_interest = int(deposit * (1 + rate * years_plan)) # Formula
            print(f"\nYour 'simple' interest calculaton is: {s_interest}")
            answer = False

        elif interest == "compound":
            c_interest = int(deposit * math.pow((1 + rate),years_plan)) # Formula
            print(f"\nYour 'compound' interest calculation is: {c_interest}")
            answer = False
        
        else:
            print("Input not recognized, please try again.")


def bond_calculations():
    """
    a function for calculatin the
    repayment bond of a house
    """
    house_value = int(input("\nPlease enter the present value of the property:\t"))

    rate = (int(input("\nPlease enter the interest rate:\t")) / 100) / 12

    months_plan = int(input("\nPlease specify how many months you are planning to repay:\t"))

    monthly_rpmnt = int((rate * house_value) / (1 - (1 + rate)**(- months_plan)))

    print(f"\nThis is the amount you have to repay each months: {monthly_rpmnt}")


print("\nINVESTMENT - to calculate the amount of interest you'll ear on your investment")
print("BOND \t   - to calculate the amount you'll have to pay on a home loan")
print()

while True:

    investment = input("Please enter 'investment' or 'bond' from the menu above: ").lower()

    if investment == "investment":

        inv_calculations()
        break


    elif investment == "bond":

        bond_calculations()
        break

    else:
        print("Invalid input, please enter 'investment' or 'bond'")

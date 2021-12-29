# coding: utf-8
import pandas as pd




"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
print("Number of loans in list")
loan_costs = [500, 600, 200, 1000, 450]
number_of_loans = len(loan_costs)
print(number_of_loans)
# YOUR CODE HERE!
# print("Number of loans in list")
# loan_costs = [500, 600, 200, 1000, 450]
# number_of_loans = len(loan_costs)
# print(number_of_loans)

print()

# sum of loans
print("Sum of loans in list")
loanlist_sum_total = sum(loan_costs)
print(loanlist_sum_total)
# YOUR CODE HERE!
# print("Sum of loans in list")
# loanlist_sum_total = sum(loan_costs)
# print(loanlist_sum_total)

print()

# Average loan amount
print("Average loan amount")
loan_avg = loanlist_sum_total / number_of_loans
print(loan_avg)
# YOUR CODE HERE!
# print("Average loan amount")
# loan_avg = loanlist_sum_total / number_of_loans
# print(loan_avg)

print()

# Printed Answers
print(f"The number of loans is: {number_of_loans}")
print(f"The sum total of the loans in this list is: ${loanlist_sum_total}")
print(f"The average loan amount is: ${loan_avg}")
# Code for printed answers
# print(f"The number of loans is: {number_of_loans}")
# print(f"The sum total of the loans in this list is: ${loanlist_sum_total}")
# print(f"The average loan amount is: ${loan_avg}")

print()
print("end part 1")


"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
print()
print("Extract future value and remaining months from dictionary")
print(loan.get("future_value"))

future_value = loan["future_value"]
print(f"the future value is: ${future_value}")

print(loan.get("remaining_months"))
remaining_months = loan["remaining_months"]
print(f"remaining months is: {remaining_months}")

# Code
# print(loan.get("future_value"))

# future_value = loan["future_value"]
# print(f"the future value is: ${future_value}")

# print(loan.get("remaining_months"))
# remaining_months = loan["remaining_months"]
# print(f"remaining months is: {remaining_months}")

print()
print("present value part 2")

# Present value resent Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
present_value = future_value / (1 + .2/12) ** remaining_months
print(f"the present value is: ${present_value}")
## Code for PV
# present_value = future_value / (1 + .2/12) ** remaining_months
# print(f"the present value is: ${present_value}")
# print()
print("Part 2 Conditional Statement")
# Define loan price as loan cost
loan_cost = loan["loan_price"]
# code
# loan_cost = loan["loan_price"]
print()

# Part 2 Conditional Statement
if present_value >= loan_cost:
    print("this loan is worth at least its cost")
else:
    print("this loan is too expensive and not worth the price")
print()
print("Conditional statement variables")
print()
# Code for conditional statement
# if present_value >= loan_cost:
#   print("this loan is worth at least its cost")
#else:
#    print("this loan is too expensive and not worth the price")
#print()


print ()

print("end part 2")

print()


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""
print()

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
print("define new loan variables")
# Define New Loan Variables
interest_rate_new_loan = .2
remaining_months_new_loan = new_loan["remaining_months"]
future_value_new_loan = new_loan["future_value"]
print()
print("calculate present value")
# New Loan Present Value
present_value_new_loan = future_value_new_loan / ((1 + (interest_rate_new_loan/12)) ** remaining_months_new_loan)
print(f"the present value of the new loan is: ${present_value_new_loan}")

print()
# code for part 3
# print("define new loan variables")
# Define New Loan Variables
# interest_rate_new_loan = .2
# remaining_months_new_loan = new_loan["remaining_months"]
# future_value_new_loan = new_loan["future_value"]
# print()
# print("calculate present value")
# New Loan Present Value
# present_value_new_loan = future_value_new_loan / ((1 + (interest_rate_new_loan/12)) ** remaining_months_new_loan)
# print(f"the present value of the new loan is: ${present_value_new_loan}")


print("end part 3")
print()
"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

print()
# Part 4 Creation of new Inexpensive Loan List"
Inexpensive_Loans = []
print()

print("For Loop through loans list for loan prices")
for dic in loans:
    print(dic.get("loan_price"))
print()

print("Conditional loop through Part 4 loans list to append loans less than or equal to $500 to Inexpensive Loans List")
for dic in loans:
    if dic.get("loan_price") <= 500:
        Inexpensive_Loans.append(dic["loan_price"])
print()

print()
print("Loans Less than or equal to $500 appended to Inexpenive Loans List")
print(Inexpensive_Loans)
print()
print("end part 4")
print()

# Code for part 4
# print()
# Part 4 Creation of new Inexpensive Loan List"
# Inexpensive_Loans = []
# print()

# print("For Loop through loans list for loan prices")
# for dic in loans:
 #    print(dic.get("loan_price"))
# print()

# print("Conditional loop through Part 4 loans list to append loans less than or equal to $500 to Inexpensive Loans List")
# for dic in loans:
#    if dic.get("loan_price") <= 500:
#        Inexpensive_Loans.append(dic["loan_price"])
#print()

# print()
# print("Loans Less than or equal to $500 appended to Inexpenive Loans List")
# print(Inexpensive_Loans)
# print()


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file


"""
print("I was unable to write the inexpensive loans list to a csv!! I tried, but ran out of time.")
print()
print("end part 5")



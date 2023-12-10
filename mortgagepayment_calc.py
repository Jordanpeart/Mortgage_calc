

# inputs for Calc

loan_amount = float(input("Enter the loan amount: $"))
interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
loan_term_years = int(input("Enter loan terms in years: "))

# convert the annual interest rate into monthly rate
# convert loan terms to months

monthly_interest_rate = interest_rate / 12
loan_term_months = loan_term_years * 12

# the actual Calc

monthly_payments = (loan_amount * monthly_interest_rate) / (1-(1+ monthly_interest_rate) ** -loan_term_months)

# display Value

print(f"The monthly mortgage payment is: ${monthly_payments:.4f}") # to the 4 decimal place
print(f"The monthly mortgage payment is: ${monthly_payments}")
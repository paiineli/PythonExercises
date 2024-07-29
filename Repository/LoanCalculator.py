from datetime import datetime

# Dictionary to map month numbers to names in English
months = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
}

def calculate_final_amount(loan, monthly_interest, num_installments):
    # Convert monthly interest rate to decimal
    monthly_interest_decimal = monthly_interest / 100

    # Initialize the balance with the loan amount
    balance = loan

    # Initialize variables for interest calculation
    original_balance = loan
    total_interest = 0

    # Get the current month and year
    today = datetime.now()
    current_month = today.month
    current_year = today.year

    # Calculate the accumulated amount month by month
    for month in range(1, num_installments + 1):
        accumulated_balance = balance * monthly_interest_decimal
        balance += accumulated_balance
        total_interest += accumulated_balance

        # Calculate the month and year name for the balance
        month_name = f"{months[current_month]} {current_year}"
        print(f"Balance after {month_name}: ${balance:.2f}")

        # Move to the next month
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1

    # Calculate the monthly installment amount
    monthly_installment = balance / num_installments
    total_paid = monthly_installment * num_installments

    return balance, monthly_installment, total_paid, total_interest

# User input
loan = float(input("Enter the loan amount: "))
monthly_interest = float(input("Enter the monthly interest rate (in %): "))
num_installments = int(input("Enter the number of installments: "))
print(30 * '-')

# Calculate the final amount and monthly installment
final_amount, monthly_installment, total_paid, total_interest = calculate_final_amount(loan, monthly_interest, num_installments)

# Display results
print(30 * '-')
print(f"The final amount to be paid after {num_installments} installments is: ${final_amount:.2f}")
print(f"Total interest paid: ${total_interest:.2f}")
print(30 * '-')
print(f"The monthly installment amount is: ${monthly_installment:.2f}")
print(30 * '-')

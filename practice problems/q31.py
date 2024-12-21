income = float(input("Enter your annual income: "))

if income > 50000:
    credit_score = int(input("Enter your credit score: "))
    if credit_score > 700:
        print("Loan approved at a standard interest rate.")
    elif 600 <= credit_score <= 700:
        print("Loan approved at a higher interest rate.")
    else:  # credit_score < 600
        print("Loan rejected due to low credit score.")
else:
    print("Loan rejected due to low income.")



def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    if str(account_number)[0] != '1' or len(str(account_number)) != 4:
        print("Invalid account number")
        return

    if account_balance < 100000:
        print("Insufficient account balance")
        return

    if(loan_type == "Car"):
        if(salary > 25000):
            if(loan_amount_expected < 500000 and customer_emi_expected < 36):
                eligible_loan_amount = 500000
                bank_emi_expected = 36
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
            else:
                print("The customer is not eligible for the loan")
        else:
            print("Invalid loan type or salary")
    elif(loan_type == "House"):
        if(salary > 50000):
            if(loan_amount_expected < 6000000 and customer_emi_expected < 60):
                eligible_loan_amount = 6000000
                bank_emi_expected = 60
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
            else:
                print("The customer is not eligible for the loan")
        else:
            print("Invalid loan type or salary")
    elif(loan_type == "Business"):
        if(salary > 75000):
            if(loan_amount_expected < 7500000 and customer_emi_expected < 84):
                eligible_loan_amount = 7500000
                bank_emi_expected = 84
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
            else:
                print("The customer is not eligible for the loan")
        else:
            print("Invalid loan type or salary")
    else:
            print("Invalid loan type or salary")


#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)
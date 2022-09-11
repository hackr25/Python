#accept amount from user and display discount
amt=int(input("Enter the bill amount"))
if amt>5000:
    b=(amt/100)*10
    bill_amt=amt-b
    print("Discount=",b,"bill amount=",bill_amt)
else:
    print("Bill amount=",amt)

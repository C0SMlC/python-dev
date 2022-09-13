print("Welcome to ATM")
balance: float = 1500
amountwithdraw: float = float(input("Enter the amount to witdraw : "))
if amountwithdraw % 5 == 0:
    balance = (balance-amountwithdraw) - 0.50
    print("Your balance is : ", balance)
else:
    print("Enter a valid amount")

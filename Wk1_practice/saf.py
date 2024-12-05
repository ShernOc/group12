#Safaricom CLI project that displays menus dynamically based on user input. 

print("""
    SIM 2
1. Safaricom+
2. M-PESA 
Enter your choice: ________
""")

def m_pesa(): 
    #user input 
    choice1 = int(input("Enter your code:"))
    if choice1 == 1:
        print("Safaricom function called")
    elif choice1 == 2:
        print("M-Pesa function called")

m_pesa() 
    
#SAFARICOM SERVICES
print("""
SIM 2
1. M-Banking services
2. My Account
""")

def m_banking():
    #user input 2 
    # choice2 = input("Enter your code: ")
    print("M-Banking function called")
    print("My Account function called")
    
m_banking()

#SAFARICOM OPTIONS
# if choice2 == 1:
# m_banking()
# elif choice2 == 2:
# my_account()
# END OF SAFARICOM SERVICES
# M-PESA SERVICES

print("""
SIM 2
1. Send Money
2. Withdraw Cash
3. Buy Airtime
4. Loans and Savings
5. Lipa na M-PESA
6. My Account
""")

# SEND MONEY OPTION
def send_Money():
    #User input 3 
    choice3 = input("Enter your code: ")

    if choice3 == 1: 
        print("Send Money") 
        
send_Money()

# ENTER PHONE NUMBER
def phone_No():
    choice5 = input("Enter Phone No: (Digits 0-9, *, #, +) 10-13 characters: ")    
    phone_number = choice5
    if phone_number == phone_number.isascii() or phone_number.isdigit(): 
        print("Phone Number")
        return phone_number
phone_No()

# ENTER AMOUNT
def Amount(): 
    choice6 = int(input("Enter Amount: "))  
    amount = choice6 
    if 0 < choice6 < 200000 :
        print(amount)

print(Amount())

# ENTER PIN NUMBER
def pin_Number(): 
    choice7 = int(input("Enter M-PESA Pin: "))
    pin = choice7
    # Since length doesn't work with integers, we converted it into a string.
    if len(str(pin)) == 4: 
        return pin
    else:
        print("Incorrect Pin number")
pin_Number()

# CONFIRMATION
print("""
Send money to ...
1.Cancel
2. Accept
""")

def confirm_Transaction():
    choice8 = int(input("Enter your code: "))
    
    if choice8 == 1 or 2 : 
        print("Transaction Confirmed")

confirm_Transaction()

# SECOND CONFIRMATION
print("""
Are you sure?
1. Cancel
2. Accept
""")

def second_Confirmation():
    choice9 = int(input("Enter your code: "))
    if choice9 == 1: 
        print("Thank you for using M-PESA Services")
    elif choice9 == 2:
         print("Transaction confirmed")
         
second_Confirmation()

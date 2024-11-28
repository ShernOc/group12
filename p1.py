#Function that takes list of numbers returns new list(copy)
numbers = [12,34,14,2,4,45,56,78]
def list_no(numbers):
    numbers = sorted(numbers)
    return numbers
    
print(list_no(numbers))
 
#2.Function takes a list and return true if list is sorted in ascending order 

def list_ascending(numbers):
    if numbers == sorted(numbers):
        return True
    else: return False
   
print(list_ascending(numbers))


#3 Function that prints numbers not divisible by 7. Using the for in range method
def print_No():
    for numbers in range(0,31):
        if numbers % 7 != 0: 
            print(numbers)
                  
# print_No()


#4. Function that find the maximum value among 5 numbers entered by the user

# Prompt the user to enter 5 numbers one by one through the terminal.
def max_no_user():
    #creating an empty list, 
    numbers = []; 
    #use the for in range method 
    for i in range(5):
        while True: 
            #prompt the user to enter 5 numbers 
            new_numbers = (input("Enter number: "))
            try: # interceptor for when a non numeric valued is entered  
                number_input = int(new_numbers)
                numbers.append(number_input) # append the numbers entered 
                break
            except ValueError:
                print("Please enter numbers only!")

    print(f"The Maximum value is {max(numbers)}")

max_no_user()



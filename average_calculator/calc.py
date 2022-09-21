from math import floor


def calculator():
    print("This calculator will help you find a rounded-down average!")
    print("Enter integers one at a time.")
    print("When you're ready to compute an average, type 'compute'")
    
    finished = False
    numbers = []
    while not finished:
        user_input = input("Enter an integer or 'compute': ")
        
        if user_input == "compute":
            try:    
                print_average(numbers)
                finished = True
            except ValueError: #if no number input
                print("You must enter at least one number before calculating an average")
           
        else:
            try:
                number = int(user_input)
            except ValueError:
                print("Invalid input. Input must be an integer or 'compute'")
                continue

            numbers.append(number)


def print_average(numbers):
    average_value = rounded_average(numbers)
    print(f"The rounded-down average of the numbers you entered is {average_value}")


def rounded_average(numbers):
    
    if not numbers:
        raise ValueError("cannot compute average of an empty collection")   
    avg = sum(numbers) / len(numbers)
    return floor(avg)
   
    
        

#write a python script that takes 2 numbers and does the maths operation like addition and the results are displayed after 5secods

import time
def add_numbers(num1, num2):
    result = num1 + num2
    return result

def sub_numbers(num1, num2):
  result = num1 -num2
  return result

def div_numbers(num1, num2):
  result = num1 / num2
  return result

def mut_numbers(num1, num2):
  result = num1 * num2
  return result

def main():
    print("Welcome to the Math Operations App!")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return
    
    operation_result1 = add_numbers(num1, num2)
    operation_result2 = sub_numbers(num1, num2)
    operation_result3 = div_numbers(num1, num2)
    operation_result4 = mut_numbers(num1, num2)
    
    print("Performing the addition operation...")
    time.sleep(0)  # Delay for 5 seconds
    
    print(f"The result of {num1} + {num2} is: {operation_result1}")

    print("\nPerforming the subtraction operation...")
    time.sleep(5)  # Delay for 5 seconds
    
    print(f"The result of {num1} - {num2} is: {operation_result2}")

    print("\nPerforming the division operation...\n")
    time.sleep(10)  # Delay for 5 seconds
    
    print(f"The result of {num1} / {num2} is: {operation_result3}")

    print("\nPerforming the multiplication operation...")
    time.sleep(15)  # Delay for 5 seconds
    
    print(f"The result of {num1} X {num2} is: {operation_result4}")


if __name__=="__main__":
    main()
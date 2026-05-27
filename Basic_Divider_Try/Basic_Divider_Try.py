# Basic_Divider_Try
# Safely divide two numbers handling ZeroDivision and Value Errors.

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"Result of Division: {result}")
    except ZeroDivisionError:
        print(f"{num1} Cannot divide by zero")
    except ValueError:
        print("Invalid data type detected.")
if __name__ == '__main__':
    try:

        num1 = int(input("Enter 1st Number: "))
        num2 = int(input("Enter 2nd Number: "))
        divide_numbers(num1, num2)
    except ValueError:
        print("Please enter integers only (numbers)!")
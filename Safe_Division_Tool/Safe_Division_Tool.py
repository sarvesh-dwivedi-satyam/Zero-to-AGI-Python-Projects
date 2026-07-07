def safe_divide(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is mathematically undefined!")
    except TypeError:
        print("Error: Unsupported operand types! Both arguments must be mumeric values.")
    return None
if __name__ == '__main__':
    safe_divide(10,2)
    safe_divide(10,0)
    safe_divide(10,"AGI")
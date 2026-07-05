def get_valid_float():
    while True:
        try:
            value = float(input("Enter Number: "))
            return value
        except ValueError:
            print("❌ Invalid Decimal Number, try again!\n")
if __name__ == '__main__':
    validated_metric = get_valid_float()
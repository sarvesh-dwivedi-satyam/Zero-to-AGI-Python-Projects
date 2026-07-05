def compute_cumulative_sum():
    total_sum = 0.0
    user_input = float(input("Enter number:"))
    while user_input != 0:
        total_sum += user_input
        user_input = float(input("Enter next number:"))
        print(f"Cumulative Total Sum: {total_sum}")
if __name__ == '__main__':
    compute_cumulative_sum()
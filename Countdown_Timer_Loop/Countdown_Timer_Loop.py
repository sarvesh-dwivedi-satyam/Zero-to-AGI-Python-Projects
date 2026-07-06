def execute_countdown():
    countdown_start = int(input("Enter countdown initiation token: "))
    while countdown_start > 0:
        print(f"{countdown_start}")
        countdown_start -= 1
        print("\n Blast off! System Successfully Launched into orbit.")
if __name__ == '__main__':
    execute_countdown()
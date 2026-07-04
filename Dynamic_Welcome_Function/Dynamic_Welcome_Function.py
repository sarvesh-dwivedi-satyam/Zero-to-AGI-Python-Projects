def welcome_user(name, role = "Student"):
    print(f"Hello {name}, Welcome as a {role}")
if __name__ == '__main__':
    user = input("Enter your name: ")
    welcome_user(user,"CEO")


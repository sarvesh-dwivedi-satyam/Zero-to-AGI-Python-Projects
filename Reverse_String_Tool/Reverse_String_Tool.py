# PROJECT: Reverse String Tool

def reverse_string():
    print("--- Reverse String Tool ---")
    user_input = input("Enter a string to reverse: ").strip()
    
    if user_input == "":
        print("Error: You entered an empty string.")
    else:
        reversed_text = user_input[::-1]
        print(f"\nOriginal: {user_input}")
        print(f"Reversed: {reversed_text}")

if __name__ == "__main__":
    reverse_string()

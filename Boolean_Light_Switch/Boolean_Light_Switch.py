def toggle_light_switch():
    light_on = False
    while True:
        user_choice = input("Type 'switch' to toggle light (or 'exit' to quit):").strip().lower()
        if user_choice == 'switch':
            light_on = not light_on
            print(f"Light Status: {'on'if light_on else 'OFF'}")
        elif user_choice == 'exit':
            break
if __name__ == '__main__':
    toggle_light_switch()
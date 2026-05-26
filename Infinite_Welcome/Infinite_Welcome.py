while True:
    print(f"{"-"*5} Welcome {"-"*5}")
    stop = input(f"{"-"*5}Press Enter to continue (or type 'stop'){"-"*5}\n: ").capitalize(). strip()
    if stop == "Stop":
        break
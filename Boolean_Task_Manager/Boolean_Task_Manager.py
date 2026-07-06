def evaluate_daily_perforance():
    is_coding_done = True
    is_exercise_done = False
    if is_coding_done and is_exercise_done:
        print("Absolute Win!")
    elif is_coding_done or is_exercise_done:
        print("Good Progress!")
    else:
        print("System Rest Required : Productivity targets missed.")

if __name__ == '__main__':
    evaluate_daily_perforance()
tasks = []
while  True :
    task_input = input(f"Enter Task {len(tasks) + 1}: ").strip().capitalize()

    if task_input == "":
        break

    tasks.append(task_input)
    

if len(tasks)> 0:
    print ("\nHear is your TO-Do List for today,")
    for index , task in enumerate(tasks, 1):
        print(f"{index}. {task}")
else:
    print("Error! Enter Task")
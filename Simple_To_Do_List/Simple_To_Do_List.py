#  PROJECT: To-DO

tasks = []

for i in range (3):
    task_input = input(f"Enter Task {i + 1}: ").strip() . capitalize()
    tasks.append (task_input)
print ("\n Hear is your TO-Do List for today,")

for index, task in enumerate(tasks, 1):
    print(f"{index}.  {task}")



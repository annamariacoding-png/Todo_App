incomplete_tasks = []
complete_task_history = []
def to_be_completed():
    number = 0
    for i in incomplete_tasks:
        number+=1
        print(number,". ",i)
    to_complete = int(input("Enter the value of task you want to complete"))
    completed_task = incomplete_tasks.pop(to_complete - 1)
    complete_task_history.append(completed_task)
def task_history():
    number = 0
    for i in complete_task_history:
        number+=1
        print(number,". ",i)
def add_task():
    new_task = input("Enter your new task: ")
    incomplete_tasks.append(new_task)
def remove_task():
    number = 0
    for i in incomplete_tasks:
        number+=1
        print(number,". ",i)
    number_to_remove = int(input("Enter the number of the task to be removed: "))
    incomplete_tasks.pop(number_to_remove-1)

print("==TODO LIST==")
print("1.Tasks to be completed")
print("2.Show task history")
print("3.Add a task")
print("4.Remove a task")
print("5.Quit")
choice = int(input("Choose an option: "))
while True:
    if choice == 1:
        to_be_completed()
    elif choice == 2:
        task_history()
    elif choice == 3:
        add_task()
    elif choice == 4:
        remove_task()
    elif choice == 5:
        print("Thank you for using the app!")
        break
    else:
        print("Invalid entry")
    print("==TODO LIST==")
    print("1.Tasks to be completed")
    print("2.Show task history")
    print("3.Add a task")
    print("4.Remove a task")
    print("5.Quit")
    choice = int(input("Choose an option: "))
    




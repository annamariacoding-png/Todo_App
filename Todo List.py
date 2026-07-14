import mysql.connector as con
mycon = con.connect(host ="Localhost",user = "root",passwd = "Bangtanarmy171",database = "Todo_App")
mycursor = mycon.cursor()

def to_be_completed():
    mycursor.execute("Select * from Incomplete_Tasks")
    data = mycursor.fetchall()
    for i in data:
         print(i[0],"."," ",i[1])
    print()

def complete_task():
    mycursor.execute("Select * from Incomplete_Tasks")
    data = mycursor.fetchall()
    for i in data:
         print(i[0],"."," ",i[1])
    to_complete = int(input("Enter the value of task you want to complete"))
    mycursor.execute("Select Task from Incomplete_Tasks where SrNo = (%s)",(to_complete,))
    data = mycursor.fetchone()
    mycursor.execute("Insert into History (Task) Values (%s)",(data[0],))
    mycursor.execute("Delete from Incomplete_Tasks where SrNo = (%s)",(to_complete,))
    mycon.commit()
    print("Task Completed!")
    print("Great Work! Keep Going")
    print()

def task_history():
    mycursor.execute("Select * from History")
    data = mycursor.fetchall()
    for i in data:
         print(i[0],"."," ",i[1])
    print("You've come a long way! Keep Going!")
    print()

def add_task():
    new_task = input("Enter your new task: ")
    mycursor.execute("Insert into Incomplete_Tasks (Task) Values (%s)",(new_task,))
    mycon.commit()
    print("Task Added Successfully!")
    print()

def remove_task():
    mycursor.execute("Select * from Incomplete_Tasks")
    data = mycursor.fetchall()
    for i in data:
         print(i[0],"."," ",i[1])
    task_to_remove = int(input("Enter value of the task to be removed: "))
    mycursor.execute("Delete from Incomplete_Tasks where SrNo = (%s)",(task_to_remove,))
    mycon.commit()
    print("Task Removed Successfully!")
    print()


print("==TODO LIST==")
print("1.Tasks to be done")
print("2.Complete a task")
print("3.Show task history")
print("4.Add a task")
print("5.Remove a task")
print("6.Quit")
choice = int(input("Choose an option: "))
while True:
    if choice == 1:
        to_be_completed()
    elif choice == 2:
        complete_task()
    elif choice == 3:
        task_history()
    elif choice == 4:
        add_task()
    elif choice == 5:
        remove_task()
    elif choice == 6:
        print("Thank you for using the app!")
        break
    else:
        print("Invalid entry")
    print("==TODO LIST==")
    print("1.Tasks to be done")
    print("2.Complete a task")
    print("3.Show task history")
    print("4.Add a task")
    print("5.Remove a task")
    print("6.Quit")
    choice = int(input("Choose an option: "))
    




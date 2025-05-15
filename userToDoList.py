import ToDoListClass
with open("tasks.txt","a") as file:
    pass
while True:
    print("""What do you want to do ?:
          1-add a task
          2-search about the status for the task 
          3-remove a task
          4-complete the task
          5-See all the tasks
          6-exit""")
    try:
        choose = int(input("Enter your choose (1,2,3,4,5): "))
        if choose == 6:
            break
        elif choose == 1:
            Task = input("Enter the task: ")
            print(ToDoListClass.ToDoList(Task).add())
        elif choose == 2:
            Task = input("Enter the task: ")
            print(ToDoListClass.ToDoList(Task).Sstatus())
        elif choose == 3:
            Task = input("Enter the task: ")
            print(ToDoListClass.ToDoList(Task).remove())
        elif choose == 4:
            Task = input("Enter the task: ")
            print(ToDoListClass.ToDoList(Task).complete())
        elif choose == 5:
            print(ToDoListClass.ToDoList(None).SeeAll())
        else:
            print("Invalid input,please enter (1,2,3,4,5,6)")
    except ValueError:
        print("Error please enter a correct value")
    finally:
        print("-----------------------------------------------------")
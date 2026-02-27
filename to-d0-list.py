def add_task():
    task=input("Add your task: ")
    print("your task",task, "added successfully")
    f=open("file.txt",'a')
    f.write(task+"\n")
    f.close()

def view_task():
    with open("file.txt",'r')as f:
                tasks=f.readlines()
                for i, task in enumerate(tasks,start=1):
                    print(f"{i}. {task.strip()}")
def del_task():
      
    with open('file.txt','r')as f:
        tasks=f.readlines()
    if len(tasks)==0:
         print("no tasks to delete")
         return
    view_task()
    delete=int(input("enter the task number to delete :"))
    if delete>=1 and delete<=len(tasks):
        del tasks[delete-1]
        print("The task deleted successfully")
        with open('file.txt','w')as f:
                for task in tasks:
                    f.write(task)
    else:
        print("task does not exists")

while True:
    print("\nTO-DO-LIST MENU")
    print("1.Add Task \n2.View Tasks \n3.Delete Task \n4.Exit")
    ipt=int(input("Enter the operation:"))
    match ipt:
        case 1:
              add_task()
        case 2:
            view_task()
        case 3:
            del_task()
        case 4:
            break
        case __:
            print("enter a valid input")



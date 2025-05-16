class ToDoList:
    def __init__(self,task):
        self.task = task
    def __str__(self):
        return f"task:{self.task}"
    def add(self):
        with open("tasks.txt","r") as file:
            data = file.readlines()
            for i in data:
                if self.task in i :
                    return "the task is already exist"
        
        with open("tasks.txt","a") as file:
            file.write(f"{self.task} (incomplete)\n")
            return "complete"
    def search(self):
        
        with open("tasks.txt","r") as file:
            data = file.readlines()
            for i in data:
                if self.task in i :
                     return i
    def remove(self):
        
        with open("tasks.txt","r") as file:
            data = file.readlines()
            n = 0
            for i in data:
                if self.task in i :
                    n =1
                    data.remove(i)
                    break
            if n ==0:
                return f"{self.task} not a task in the file"
        with open("tasks.txt","w") as file:
            file.writelines(data)
            return "complete"
    def Sstatus(self):
        with open("tasks.txt","r") as file:
            data = file.readlines()
            n = 0
            for i in data:
                if self.task in i:
                    n = 1
                    return "complete" if "incomplete" not in i else "incomplete"

            return f"{self.task} not found"
    def complete(self):
        with open("tasks.txt","r")as file:
            data = file.readlines()
            n = 0
            for i in data:
                if self.task in i:
                    n = 1
                    s = data.index(i)
                    data[s] = data[s].replace("incomplete","complete")
            if n ==0 :
                return f"{self.task} not found"
        with open("tasks.txt","w") as file:
            file.writelines(data)
            return "complete"
    def SeeAll(self):
        with open("tasks.txt","r")as file:
         data = file.readlines()
         return "".join([x for x in data])
       

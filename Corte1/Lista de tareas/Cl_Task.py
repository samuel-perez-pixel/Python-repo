class Task:
    def __init__(self,id,description,priority,status,internalState):
        self.id=id
        self.description=description
        self.priority=priority
        self.status=status
        self.internalState='A'

    def showTask(self):
        print("")
        print("*********Task Data*********")
        print("")
        print(f"Id: {self.id} \n Description: {self.description}\n Priority: {self.priority}\n Status: {self.status}")
        print("")
        print("*******************************")
        print("")
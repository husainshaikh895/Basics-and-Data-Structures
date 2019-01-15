#Stack

class Stack:
    def __init__(self):
        self.lstack = list()

    def push(self,element):
        self.lstack.insert(0,element)

    def pop(self):
        if(len(self.lstack)>=1):
            self.lstack.pop(0)
        else:
            print("No elements to pop.")

    def display(self):
        print(self.lstack)
        if(len(self.lstack)<1):
            print("Stack is empty.")

obj = Stack()
obj.push(1)
obj.push(2)
obj.display()
obj.pop()
obj.display()
obj.pop()
obj.pop()

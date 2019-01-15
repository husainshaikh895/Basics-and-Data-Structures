#Queue Data Structure

class Queue:
	def __init__(self):
		self.lqueue = list()

	def push(self,element):
			self.lqueue.insert(0,element)

	def pop(self):
		if(len(self.lqueue)>=1)
			self.lqueue.pop(-1)
		else:
			print("No elements to pop.")

	def display(self):
		print(self.lqueue)
		if(len(self.lqueue)<1):
			print("Queue is empty.")


obj = Queue()
obj.display()
obj.push(3)
obj.display()
obj.push(2)
obj.display()
obj.pop()
obj.display()

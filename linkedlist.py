#linked list
class slist:
	def __init__(self):
		self.slist = list()

	def insert(self, element):
		self.slist.insert(0,element)

	def remove(self):
		self.slist.pop(-1)

obj = slist()
obj.insert(1)
obj.insert(2)
print(obj.slist)
obj.insert(3)
print(obj.slist)
obj.remove()
print(obj.slist)
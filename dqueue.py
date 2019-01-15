class dqueue:
	def __init__(self):
		self.elms = list()

	def insertf(self, element):
		self.elms.insert(0, element)
		print(element," inserted.")

	def insertd(self, element):
		self.elms.append(element)
		print(element," inserted.")

	def removef(self):
		popped = self.elms.pop(0)
		print(popped, " has been popped.")

	def removed(self):
		popped = self.elms.pop(-1)
		print(popped, " has been popped.")
#Testing DTC for AND/OR gate
#
#Husain Shaikh


from sklearn import tree
import random

model = tree.DecisionTreeClassifier()

print("AND logic")
features = []
label = []
count = 1000
while(count>0):
	num1 = random.randint(-9,9)
	num2 = random.randint(-9,9)
	num = [num1,num2]
	features.append(num)
	if(num1==0 or num2==0):
		label.append(0)
	else:
		label.append(1)
	count-=1

model = model.fit(features,label)
test = [[1,1],[0,1],[1,0],[0,9],[9,0],[2,7],[-1,0],[0,-1],[-1,-8],[4,-5]]
test_label = [1,0,0,0,0,1,0,0,1,1]
result = model.predict(test)
for i in range(len(test)):
	print("{} and {}".format(*test[i]), " : ",result[i],end="")
	if(test_label[i]==result[i]):
		print("")
	else:
		print("\tX")

#OR Logic
print("OR Logic")
count=1000
features.clear()
label.clear()

while(count>0):
	num1 = random.randint(-9,9)
	num2 = random.randint(-9,9)
	num = [num1,num2]
	features.append(num)
	if(num1==0 and num2==0):
		label.append(0)
	else:
		label.append(1)
	count-=1

model = model.fit(features,label)
test = [[1,1],[0,1],[1,0],[0,9],[9,0],[2,7],[-1,0],[0,-1],[0,0],[-1,-8],[4,-5]]
test_label = [1,1,1,1,1,1,1,1,0,1,1]
result = model.predict(test)
for i in range(len(test)):
	print("{} or {}".format(*test[i]), " : ",result[i],end="")
	if(test_label[i]==result[i]):
		print("")
	else:
		print("\tX")

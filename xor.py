# Classifying outputs of and, or and xor logic

# Husain Shaikh
# 25 Mar 19



from sklearn import tree
import random
model = tree.DecisionTreeClassifier()

features = []
labels = []

# third feature and meaning 
# 1 ---- and
# 2 ---- or
# 3 ---- xor


# Collecting data
for i in range(100):
	a = random.randint(0,1)
	b = random.randint(0,1)
	c = random.randint(1,3)
	flist = [a, b, c]
	features.append(flist)


	# AND logic
	if(c==1):
		if(a==1 and b==1):
			labels.append([1])
		else:
			labels.append([0])

	elif(c==2):
		#or logic
		if(a==0 and b==0):
			labels.append([0])
		else:
			labels.append([1])

	elif(c==3):
		#xor logic
		if(a==b):
			labels.append([0])
		else:
			labels.append([1])


# Training the model
model.fit(features, labels)


test = []
# generating test data
for j in range(20):
	a = random.randint(0,1)
	b = random.randint(0,1)
	c = random.randint(1,3)
	test.append([a, b ,c])

# making predictions
predictions = model.predict(test)

for k in range(len(test)-1):
	print(test[k], " : ", predictions[k])

















# Binary Search

sorted = [1, 2, 3, 4, 5, 6, 7, 8, 12, 12, 22, 32, 43, 54, 65, 78, 79, 87, 90, 98]
low = 0
flag = 1
high = len(sorted)-1

element = 99

mid = (len(sorted))//2
print("Mid - ",mid)
while flag:
	if(sorted[mid]<element):
		low = mid
		mid = (high+low)//2
		if((high-low)<=1):
			if(sorted[high]==element):
				print("Element Found at ",high)
				break
			elif(sorted[low]==element):
				print("Element Found at ",low)
				break
			else:
				print("Not Found")
				break
	elif(sorted[mid]>element):
		high = mid
		mid = (high+low)//2
		if((high-low)<=1):
			if(sorted[high]==element):
				print("Element Found at ",high)
				break
			elif(sorted[low]==element):
				print("Element Found at ",low)
				break
			else:
				print("Not Found")
				break
	else:
		print("Element Found at ",mid)
		flag =0
	print("High : {}\nLow : {}\nMid : {} \n\n".format(high,low,mid))

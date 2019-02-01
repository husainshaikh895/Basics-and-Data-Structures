# insertion sort

# Holding onto each element (and moving others) and then trying
# to find it's position in the list according to those positions
# iterating over each element till it is completely sorted is called insertion sort

unsorted = [3,2,5,4,1,6,7,8,22,32,43,12,54,65,87,98,78,79,90,12]

for i in range(len(unsorted)-1):
	current = unsorted[i]
	j = i - 1

	while(j >= 0 and unsorted[j] > current):
		unsorted[j+1] = unsorted[j]
		j-=1
	unsorted[j+1] = current

print(unsorted)
#Bubble sort
'''
comparing every couple as it iterates, it swaps the two elements if the latter one is smaller,
so the largest element is placed in the end after completion of each iteration
that is why the range of inner loop is upto the end-i , as the last i elements will be sorted
'''
unsorted = [3,2,5,4,1,6,7,8,22,32,43,12,54,65,87,98,78,79,90,12]
swap = 0
for i in range(len(unsorted)-1):
        for j in range(len(unsorted)-1-i):
                if(unsorted[j]>unsorted[j+1]):
                        unsorted[j],unsorted[j+1] = unsorted[j+1],unsorted[j]
                        swap+=1

print(unsorted)
print("elements : {} , swaps : {}".format(len(unsorted),swap))

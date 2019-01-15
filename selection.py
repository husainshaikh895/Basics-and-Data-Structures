#Selection sort
'''
increments i in every iteration
finds minimum element's position in inner loop
swaps the i'th index with minimum element so that a part of list is sorted
'''
unsorted = [3,2,5,4,1,6,7,8,22,32,43,12,54,65,87,98,78,79,90,12]

swap = 0

for i in range(len(unsorted)):
    minpos = i
    #To find the index at which the minimum element is present
    for j in range(i+1,len(unsorted)):
        if(unsorted[minpos]>unsorted[j]):
            minpos = j
            swap+=1
    unsorted[minpos], unsorted[i] = unsorted[i], unsorted[minpos]


print(unsorted)
print(swap)
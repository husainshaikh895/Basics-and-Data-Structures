#Husain Shaikh

#inspired by this concept 
#DONG - Michael (https://www.youtube.com/watch?v=pBYPXsGka74)

#Leaning tower of Lire problem

#Given the length of each uniform stable shape and an end goal to reach in metres, calculate number of blocks required 
#To reach the target
'''

___
 ___
  ___

they are a structure like above


The upper one can go half its length without falling and others follow arithmetic sequence
1/(2*n)
'''

no_of_blocks=0
length=float(input("Please enter the length of each block precisely : "))
target_length = float(input("Please enter the target length : "))
curr_length=0.0
n=1
while(curr_length<target_length):
	no_of_blocks+=1
	curr_length = curr_length + (length*(1/(2*n)))
	n+=1

print("No of blocks required are : ",no_of_blocks)


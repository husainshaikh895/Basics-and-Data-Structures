#Husain Shaikh
# Brilliant.com challenge
# Find total numbers between 0-200 having exactly three divisors
# modified for all the numbers with n divisors

total_nums_dict = {}

count = 0

for i in range(int(input("Enter the higher limit : ")), 2, -1):
	for j in range(2, i):
		if(i%j==0 and (not(i==j))):
			count+=1


	total_nums_dict[i] = count
	count=0

for k,v in total_nums_dict.items():
	print(k," has ",v," divisors")

print("Number of divisors are less than 2 because 1 and the number itself is not considered\nSo prime numbers will show 0 divisors.\n Add 2 to the number of divisors to get an exact figure or modify the code (change 2 to 1 in the for loop and remove ```not(j==i)```")

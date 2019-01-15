# Primality test - Check if a number is prime or not

from math import sqrt, ceil
marked = []
try:
	num = int(input("Enter the number to check if it is prime : "))
except(ValueError):
	print("Please Enter a real number greater than 1 or less than -1")
	quit()


num_sq = ceil(sqrt(abs(num)))

flag = False

for i in range(2, num_sq + 1):
	if(num % i == 0):
		flag = True
		break

if(flag == True or num == 1 or num == 0):
	print("Not a prime")
else:
	print("It is a prime number")
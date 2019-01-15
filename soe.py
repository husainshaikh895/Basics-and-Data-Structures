#Find prime numbers less than a given number

primes = []

for i in range(2, int(input("Enter a number : "))):
	if(not (i % 3 == 0 or i % 5 == 0 or i % 2 == 0 or i % 7 == 0) or i == 2 or i == 3 or i == 7 or i == 5):
		primes.append(i)

print(primes)
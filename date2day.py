print("Date to Day for 2019")

months = [5,1,1,4,6,2,4,0,3,0,1,3,]
days = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

date = int(input("Enter the date : "))
day = date%7



month = int(input("Enter the month : "))

less = [2,4,6,9,11]

if((month in less and date>=31) or date>31 or month>12):
	print("Please recheck the figures.")
	if(month == 2):
		print("February has 28 days this year.")
	day = "Error"
	quit()

day = day + months[month-1]
day = day%7

day = day + 3
day = day % 7
day = days[day]



print(day,"  ", date, "/",month, "/", "2019")
number = int(input("enter a number:"))
if(number < 0):
	print("this:", number, "is a negative")
elif number %2 == 0:
	print("this", number, "is an even number")
elif number %2 != 0:	
	print("this", number, "is an odd number")
else:
	print("this:", number, "is a positive number")

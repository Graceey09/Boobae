num1 = int(input("Enter a digit: "))
num2 = int(input("Enter a digit: "))
num3 = int(input("Enter a digit: "))
answer = num1 + num2 + num3
average = (num1 + num2 + num3)/3
smallestNumber = num1
if (num2 < num1):
	smallestNumber = num2
if (num3 < num2):
	smallestNumber = num3
largestNumber = num1
if (num2 > num1):
	largestNumber = num2
if (num3 > num2):
	largestNumber = num3
print("the sum", "is", answer)
print("the average", "is", average)
print("smallest number", "is", smallestNumber)
print("Largest number", "is", largestNumber) 

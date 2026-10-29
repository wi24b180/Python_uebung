#!/usr/bin/env python3
print("Please enter 2 number to multiply: ")
print("Please enter the 1st number: ")
num1 = int(input())
print("Please enter the 2nd number: ")
num2 = int(input())

result = num1 * num2
if result > 0:
	print("Here is your result: ")
	print(num1,"x",num2,"=",result)
elif result == 0:
        print("Your result ist positive and negative: ")
        print(num1,"x",num2,"=",result)
else:
	print("Your result is negative: ")
	print(num1,"x",num2,"=",result)


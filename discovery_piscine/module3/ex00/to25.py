#!/usr/bin/env python3
print("Enter a number less than 25: ")

user_input = int(input())

if user_input < 25:
	i = user_input
	while i <= 25:
		print("Inside the loop, my variable is", i)
		i += 1
else:
	print("Error")

	
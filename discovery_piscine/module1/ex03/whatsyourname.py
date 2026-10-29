#!/usr/bin/env python3
q1 = "What is your first name? "
print (q1)
name = input()

q2 = "And your last name ?"
print(q2)
lastname = input() 


greeting = "Hello {} {}, I welcome you to 42 Vienna :) "
print (greeting.format(name,lastname))



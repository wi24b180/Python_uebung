#!/usr/bin/env python3
user_age = input("Please tell me your age: " )

rnge = 10
while rnge <= 30:
    result = int(user_age) + rnge
    print(f"In {rnge} years, you'll be {result} years old.")
    rnge += 10



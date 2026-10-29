#!/usr/bin/env python3
x = [ 2, 8, 9, 48, 8, 22, -12, 2]
new = [i +2 for i in x ]

mod = [i+2 for i in x if i > 5 ]



print("Original list:", x ,"\n","New List:", new)

print(set(mod))




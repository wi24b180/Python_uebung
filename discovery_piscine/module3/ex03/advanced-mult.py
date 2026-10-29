#!/usr/bin/env python3
table = 0
while table <=10:
    print("\nTable of ",table,": ", end =" ")
    column = 0
    while column <=10:
       result = table * column
       print(f" {result} ", end= "")

       column += 1

    table +=1

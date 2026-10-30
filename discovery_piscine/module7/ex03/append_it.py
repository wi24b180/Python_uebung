#!/usr/bin/env python3
import sys 
st = sys.argv[1:]

if len(st) == 0:
    print("none")
else:
    for param in st:
        if len(st) >= 3 and param.find("ism", len(param) - 3) != -1:
            continue
        print(param + "ism")

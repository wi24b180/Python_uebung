#!/usr/bin/env python3
import sys

st = sys.argv[1:]

if len(st) == 0:
    print("none")
else: 
    print(f"parameters: {len(st)}") 
    for x in st: 
        print(f"{x}:{len(x)}")

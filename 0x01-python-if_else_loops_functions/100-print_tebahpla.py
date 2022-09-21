#!/usr/bin/python3
index = 122

while index > 96:
    if index % 2 == 0:
        a = 0
    else:
        a = 32
        
    print("{}".format(chr(index - a)), end='')
    index -= 1


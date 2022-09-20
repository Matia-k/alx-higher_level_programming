#!/usr/bin/python3
for n in range(0, 99):
    if n < 10:
        n = '0' + str(n)
    print("{}".format(n), end=", ")
print("99")

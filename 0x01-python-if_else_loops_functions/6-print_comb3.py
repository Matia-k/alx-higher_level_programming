#!/usr/bin/python3
for n in range(0, 89):
    if n < 10:
        n = '0' + str(n)
    else:
        n = str(n)
    m = n[1] + n[0]
    if n[0] == n[1]:
        continue
    if int(m) < int(n):
        continue
    print("{}".format(n), end=", ")

print(f"{89}")

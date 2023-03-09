#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no_of_arg = len(sys.argv) - 1
    sum_of_args = 0
    index = 1
    while (index <= no_of_arg):
        sum_of_args += int(sys.argv[index])
        index += 1

    print(f"{sum_of_args}")

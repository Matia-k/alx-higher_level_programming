#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no_of_arg = len(sys.argv) - 1
    if no_of_arg == 0:
        print(f"{no_of_arg} arguments.")
    elif no_of_arg == 1:
        print(f"{no_of_arg} argument:")
        print(f"{no_of_arg}: {sys.argv[1]}")
    elif no_of_arg > 1:
        print(f"{no_of_arg} arguments:")
        for arg in range(no_of_arg):
            print(f"{arg + 1}: {sys.argv[arg + 1]}")

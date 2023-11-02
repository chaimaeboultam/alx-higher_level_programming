#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]  # Excluding the script name from the arguments
    num = len(arguments)
    if num == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num, 's' if num != 1 else ''))
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))

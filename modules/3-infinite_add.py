#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n = len(argv)
    if n >= 1:
        numbers = [int(arg) for arg in argv[1:]]
        # Calculate the sum of the numbers
        result = sum(numbers)
        print("Sum of arguments:", result)
   # else:
       # result = 0
       # print(result)

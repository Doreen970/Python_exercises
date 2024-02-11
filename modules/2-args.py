#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n = len(argv)

    if n <= 1:
        print("0 arguments.")
    elif n == 2:
        print("1 argument:")
        print(f"1 {argv[1]}")
    else:
        print(f"{n-1} arguments:")
        for i in range(n):
            if i > 0:
                print(f"{i}: {argv[i]}")

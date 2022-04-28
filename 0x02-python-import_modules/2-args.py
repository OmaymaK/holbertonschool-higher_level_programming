#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"{len(sys.argv) - 1} arguments.")
    elif len(sys.argv) == 2:
        print(f"{len(sys.argv) - 1} argument:")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
    for i, arg in enumerate(sys.argv[1:]):
        print(f"{i+1:}: {arg}")

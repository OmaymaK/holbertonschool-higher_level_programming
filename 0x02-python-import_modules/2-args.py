#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"{len(sys.argv) - 1} arguments.")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
    for i, arg in enumerate(sys.argv[1:]):
        print(f"{i + 1:>6}: {arg}")

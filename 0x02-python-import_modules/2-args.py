#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1
    if not argc:
        print("0 arguments.")
    else:
        print("{} argument:".format(argc))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))

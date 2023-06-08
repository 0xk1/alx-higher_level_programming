#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1
    print("{} argument:".format(argc) if argc == 1 else
          "{} arguments.".format(argc) if not argc else
          "{} arguments:".format(argc))
    if argc:
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))

import sys
if len(sys.argv) == 3:
    first = int(sys.argv[1])
    last = int(sys.argv[2])
    lst = []
    for i in range(first, last+1):
        lst.append(i)
    print(lst)
else:
    print("none")
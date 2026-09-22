import sys
if len(sys.argv) < 2:
    print("none")
else:
    for i in range(1,len(sys.argv)):
        if  sys.argv[i].endswith("ism"):
            continue
        print(sys.argv[i]+ "ism")

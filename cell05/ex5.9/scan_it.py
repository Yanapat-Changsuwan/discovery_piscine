import sys
keyword = sys.argv[1:2]
txt = sys.argv[2:3]
count = 0
if len(txt) < 1 or len(keyword) < 1:
    print("none")
else:
    for i in range(len(txt)):
        if txt[i] == keyword:
            count += 1
    print(count)
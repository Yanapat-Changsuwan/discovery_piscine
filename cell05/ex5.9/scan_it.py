keyword,txt = input().split()
count = 0
if len(txt) <= 1:
    print("none")
else:
    for i in range(len(txt)):
        if txt[i] == keyword:
            count += 1
    print(count)

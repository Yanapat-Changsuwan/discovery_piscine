inp = list(input().split())

if len(inp)  <=1:
    print("none")
else:
    for i in range(len(inp)):
        print(inp[::-1])
        print(inp[::-1][i])
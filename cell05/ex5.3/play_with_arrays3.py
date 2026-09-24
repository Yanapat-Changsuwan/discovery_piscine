arr =  [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
print(arr)
for i in arr:
    if i > 5:
        i = i +2
        new_arr.append(i)
        new_set = set(new_arr)
print(new_set)
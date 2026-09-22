arr =  [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
print(f"Original array: {arr}")
for i in range(len(arr)):
    arr[i] = arr[i] +2
    if arr[i] > 5:
        new_arr.append(arr[i])
        last = set(new_arr)
print(f"New array with values > 5: {last}")
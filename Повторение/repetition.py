number = input().split()
arr_1 = []
arr_2 = []
result_arr = []
for i in range(0, len(number), 2):
    arr_1.append(number[i])
for i in range(1, len(number), 2):
    arr_2.append(number[i])
count = len(arr_1) + len(arr_2)
for i in range(count):
    if i + 1 <= len(arr_2):
        result_arr.append(arr_2[i])
    if i + 1 <= len(arr_1):
        result_arr.append(arr_1[i])
print(*result_arr)

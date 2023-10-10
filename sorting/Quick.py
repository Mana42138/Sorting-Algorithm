# Quick Sort

array = [2, 1, -3, 5]

for i in range(0, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and array[i] < array[j]:
        array[i] = array[j + 1] 
        j -= 1
    array[j] = key

print(array)
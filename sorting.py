numbers = [33,22,44,55,66,12,42,99]
print(numbers)
def selection_sort(arr):
    sorted_arr = arr[:]
    n = len(sorted_arr)
    for i in range (n):
        min_idx = i
        for j in range(i+1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j 
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    return sorted_arr
sorted_numbers = selection_sort(numbers)

print(f'сортировка {sorted_numbers}')

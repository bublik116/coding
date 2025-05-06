def selection_sort(arr):
    n = len(arr)  
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array_selection = [33,22,44,55,66,12,42,99]
sorted_array_selection = selection_sort(array_selection)
print(f"сортировка (Selection Sort): {sorted_array_selection}")

array_bubble = [33,22,44,55,66,12,42,99]
sorted_array_bubble = bubble_sort(array_bubble)
print(f"сортировка (Bubble Sort): {sorted_array_bubble}")

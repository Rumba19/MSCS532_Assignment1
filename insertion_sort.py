#Insertion Sort Algorithm in decreasing order

def insertion_sort_descending(arr):
    length = len(arr)
    for i in range(1, length):
        key = arr[i]   
        j = i - 1   
        # Move elements less than key one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

 
array = [1, 10, 53, 4, 7]
print("Original Array 1:", array)
insertion_sort_descending(array)
print("Sorted Array in Decreasing Order: 1", array)
 
array = [1, 3, 5, 4, 7]
print("Original Array 2:", array)
insertion_sort_descending(array)
print("Sorted Array in Decreasing Order 2:", array)

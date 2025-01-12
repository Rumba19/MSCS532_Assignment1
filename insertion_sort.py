#Insertion Sort Algorithm in decreasing order

def insertion_sort_descending(arr):
    length = len(arr) # length of the list
    for i in range(1, length):
        key = arr[i]   #Current element to be placed
        j = i - 1   # start with last element 
        # Move elements less than key one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
             # Place the key in its correct position
        arr[j + 1] = key

 


if __name__ == "__main__":
    try:
        # Example array
        array = [1, 3, 5, 4, 7]
        print("Original Array:", array)

        # Sort the array in decreasing order
        insertion_sort_descending(array)
        print("Sorted Array in Decreasing Order:", array)

    except TypeError as e:
        print("TypeError: Please provide a valid list of numbers. Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

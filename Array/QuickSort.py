def partition(array, low, high):
    pivot = array[high]  # Choose last element as pivot
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]  # Swap
            
    array[i+1], array[high] = array[high], array[i+1]  # Place pivot in correct position
    return i+1  # Return pivot index

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1  # Initialize high on first call
    
    if low < high:  # Base case: subarray of 0 or 1 elements
        pivot_index = partition(array, low, high)  # Partition the array
        quicksort(array, low, pivot_index-1)  # Sort left subarray
        quicksort(array, pivot_index+1, high)  # Sort right subarray


my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)
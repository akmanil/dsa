# arr = [64, 34, 25, 12, 22, 11, 90, 5];
# n =  len(arr);
# # for i in range(1,n):
# #     insertIndex = i;
# #     insertValue = array.pop(i);
# #     for j in range(i-1,-1,-1):
# #         if array[j] > insertValue:
# #             insertIndex = j;
# #     array.insert(insertIndex , insertValue);

# # print(array); 
# # improve the insertioon method
# for i in range(1,n):
#     insertIndex = i ;
#     currentValue = arr.pop(i);
#     for j in range(i-1 ,-1 ,-1):
#         if arr[j] > currentValue:
#             arr[j+1] = arr[j];
#             insertIndex = j;
#         else :
#             break;
#     sortedArr = arr[insertIndex];

# print(sortedArr);

# arr = [64, 34, 25, 12, 22, 11, 90, 5]
# n = len(arr)

# for i in range(1, n):
#     currentValue = arr.pop(i)  # Remove current element
#     insertIndex = i  # Default insertion position (if no shifts needed)
    
#     # Traverse backwards to find the correct insertion point
#     for j in range(i-1, -1, -1):
#         if arr[j] > currentValue:
#             arr[j+1] = arr[j]  # Shift larger elements right
#             insertIndex = j      # Update insertion index
#         else:
#             break  # Stop if correct position found
    
#     arr.insert(insertIndex, currentValue)  # Insert at the correct position

# print("Sorted array:", arr)  # Output: [5, 11, 12, 22, 25, 34, 64, 90]

arr = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(arr)

for i in range(1, n):
    currentValue = arr[i]  # Don't pop, just get the value
    j = i - 1
    while j >= 0 and arr[j] > currentValue:
        arr[j + 1] = arr[j]  # Shift elements right
        j -= 1
    arr[j + 1] = currentValue  # Insert in correct position

print("Sorted array:", arr)  # [5, 11, 12, 22, 25, 34, 64, 90]
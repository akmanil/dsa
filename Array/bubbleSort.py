arr = [34,5,67,6,21,3];
n = len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] < arr[j+1]:
            arr[j+1] ,arr[j] = arr[j] ,arr[j+1];
print(arr);

#Above this using for BubbleSort method

#using buildin Sorted method
sortedArr = sorted(arr);
print(sortedArr);

sorted_desc = sorted(arr, reverse=True)
print(sorted_desc)  # [67, 34, 21, 6, 5, 3]

#In this case, the array will be sorted after the first run, but the Bubble Sort algorithm will continue to run, without swapping elements, and that is not necessary.
my_array = [7, 3, 9, 12, 11];
n = len(my_array);
for i in range(n-1):
    swaped =False;
    for j in range(n-i -1):
        if my_array[j] > my_array[j+1]:
            my_array[j] , my_array[j+1] =my_array[j+1] ,my_array[j];
            swaped =True;
    if not swaped:
        break;

print(my_array);


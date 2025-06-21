arr = [1,7,6,2,3,5];
n = len(arr);

for i in range(n-1):
    minIndex = i;
    for j in range(i+1, n):
        if arr[j]< arr[minIndex]:
            minIndex = j;
    arrValue = arr.pop(minIndex);
    arr.insert(i , arrValue);
           

print(arr);
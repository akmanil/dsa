def searchElem (arr ,value):
    left = 0;
    right = len(arr)-1
    while left <= right:
        mid =(left +right) // 2

        if arr[mid] == value:
            return mid;
        
        if arr[mid] < value:
             left = mid+1;
        
        else:
          right = mid -1;
    return -1

arr = [1,2,3,4,5,6,7];
value = 7;
result = searchElem(arr , value);

if result != -1:
    print(value , result)
if result == -1 :
    print("NOt found");


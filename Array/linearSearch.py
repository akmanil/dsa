# def searchArrayIndex(array , value) :
#     for i in range(len(array)):
#        if array[i] == value:
#         return i

#     return -1;
# array = [1,2,3,4];
# value = 3;
# result = searchArrayIndex(array , 3);
# if result != -1:
#    print("value is",value,"found at index",result)

# if result == -1:
#    print("the searched value" , value,"Not Found");
arr =[1,2,3,4,5];
value = 4;
def foundIndex(arr ,value):
    for i in range(len(arr)):
        if arr[i] == value:
            return print("The value : ",value,"found at " ,i ,"Index no.");
    
    return print("value" , value ,"Not Found");

foundIndex(arr ,value);


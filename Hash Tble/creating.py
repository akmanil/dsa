# myArray = ["papu",'papu','anil','sunil' , 'lipu', 'sipu' , 'baba' , 'mummy'];

# myHashSet = [[[None]*3]]*15
# # storing names using hash function

# def hash_function(value):
#     sumOfChar = 0;
#     for i in value:               #It is a hassh Function that return a ascii value and                                 its divisible by 10 and get its modulous
#         sumOfChar += ord(i);

#     return sumOfChar% 10;
# print("we has a asicci value" , hash_function(myArray[2]));

# # Insert each name into myHashSet using the hash function
# for name in myArray:
#     index = hash_function(name)
#     myHashSet[index] = name  # Store the name at the computed index

# print("Final Hash Set:", myHashSet)

myArray = ["papu",'papu','anil','sunil','lipu','sipu','baba','mummy']

# Initialize hash set with empty lists for chaining
myHashSet = [[] for _ in range(10)]  # 10 slots (matches hash function range)

def hash_function(value):
    sumOfChar = 0
    for char in value:
        sumOfChar += ord(char)
    return sumOfChar % 10  # Returns index 0-9

# Insert names with chaining
for name in myArray:
    index = hash_function(name)
    # Only add if not already present (avoid duplicates)
    if name not in myHashSet[index]:
        myHashSet[index].append(name)

print("Final Hash Set:")
for i, bucket in enumerate(myHashSet):
    print(f"Index {i}: {bucket}")

# Check for 'anil'
print("\n'anil' is at index:", hash_function('anil'))
print("Stored at that index:", myHashSet[hash_function('anil')])
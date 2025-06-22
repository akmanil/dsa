
#Stack are made using  array and linkedlist
#But we make this stack using array
#Its more efficient and Esier to implement and easy to understand


# stack = [];

# stack.append(5);
# stack.append(15);
# stack.append(25);
# stack.append(35);
# stack.append(55);

# print("Stack" , stack);

# popElem = stack.pop()
# print("Pop" , popElem);

# isEmpty = not bool(stack);
# print("Is empty ", isEmpty);

# peek = stack[-1];
# print('Peek',peek);

#creating using the linkedlist 

# def Stack():
#     def __init__(self):
#         self.stack = []

#     def pop(self):
#         if self.isEmpty():
#             return print('stack is empty');
        
#         return  self.stack.pop();
    
#     def push(self,element):
#        self.stack.append(element);
    
#     def peek(self):
    
#         if self.isEmpty():
#             return print('stack is empty');
        
#         return  self.stack[-1];
   
#     def isEmpty(self):
#         return len(self.stack) ==0;
    
#     def size(self):
#         return len(self.stack);

# mystack = Stack(); #creating a stack;p
# mystack.push(5);
# mystack.push(51);
# mystack.push(15); # push the node in the stack ; node because it create using linkedlist
# mystack.push(25);
# mystack.push(35);

# # Now printing all the function we are useed

# print('Stack' , mystack);
# print('Push' , mystack.push(55));
# print('Pop' , mystack.pop);
# print('isEmpty' , mystack.isEmpty);
# print('Size' , mystack.size);
# print('Peek' , mystack.peek);

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def push(self, element):
        self.stack.append(element)
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
   
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

# Testing the Stack
mystack = Stack()
mystack.push(5)
mystack.push(51)
mystack.push(15)
mystack.push(25)
mystack.push(35)

print('Stack:', mystack.stack)  # Print the stack elements
print('Pop:', mystack.pop())    # Pop the last element
print('Is Empty:', mystack.isEmpty())  # Check if empty
print('Size:', mystack.size())  # Get stack size
print('Peek:', mystack.peek())  # Peek the top element




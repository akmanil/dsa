
#Stack are made using  array and linkedlist
#But we make this stack using array
#Its more efficient and Esier to implement and easy to understand


stack = [];

stack.append(5);
stack.append(15);
stack.append(25);
stack.append(35);
stack.append(55);

print("Stack" , stack);

popElem = stack.pop()
print("Pop" , popElem);

isEmpty = not bool(stack);
print("Is empty ", isEmpty);

peek = stack[-1];
print('Peek',peek);
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def insert_at(self, data, index):
        if index < 0 or index > self.size:
            return False
        
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            i = 0
            
            while i < index:
                prev = current
                current = current.next
                i += 1
            
            new_node.next = current
            prev.next = new_node
        
        self.size += 1
        return True
    
    def remove_from(self, index):
        if index < 0 or index >= self.size:
            return None
        
        current = self.head
        
        if index == 0:
            self.head = current.next
        else:
            prev = None
            i = 0
            
            while i < index:
                prev = current
                current = current.next
                i += 1
            
            prev.next = current.next
        
        self.size -= 1
        return current.data
    
    def print_list(self):
        current = self.head
        output = []
        while current:
            output.append(str(current.data))
            current = current.next
        print(" -> ".join(output) + " -> NULL")
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

# Usage example
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.insert_at(15, 1)
    ll.print_list()  # 10 -> 15 -> 20 -> 30 -> NULL
    ll.remove_from(2)
    ll.print_list()  # 10 -> 15 -> 30 -> NULL
    print("Size:", ll.get_size())  # Size: 3
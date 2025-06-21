class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  // Add element to end of list
  append(data) {
    const newNode = new Node(data);
    
    if (!this.head) {
      this.head = newNode;
    } else {
      let current = this.head;
      while (current.next) {
        current = current.next;
      }
      current.next = newNode;
    }
    this.size++;
  }

  // Insert at specific position
  insertAt(data, index) {
    if (index < 0 || index > this.size) return false;
    
    const newNode = new Node(data);
    
    if (index === 0) {
      newNode.next = this.head;
      this.head = newNode;
    } else {
      let current = this.head;
      let prev = null;
      let i = 0;
      
      while (i < index) {
        prev = current;
        current = current.next;
        i++;
      }
      
      newNode.next = current;
      prev.next = newNode;
    }
    
    this.size++;
    return true;
  }

  // Remove from position
  removeFrom(index) {
    if (index < 0 || index >= this.size) return null;
    
    let current = this.head;
    
    if (index === 0) {
      this.head = current.next;
    } else {
      let prev = null;
      let i = 0;
      
      while (i < index) {
        prev = current;
        current = current.next;
        i++;
      }
      
      prev.next = current.next;
    }
    
    this.size--;
    return current.data;
  }

  // Print the list
  print() {
    let current = this.head;
    let str = "";
    while (current) {
      str += current.data + " -> ";
      current = current.next;
    }
    str += "NULL";
    console.log(str);
  }

  // Get size
  getSize() {
    return this.size;
  }

  // Check if empty
  isEmpty() {
    return this.size === 0;
  }
}

// Usage example
const list = new LinkedList();
list.append(10);
list.append(20);
list.append(30);
list.insertAt(15, 1);
list.print(); // 10 -> 15 -> 20 -> 30 -> NULL
list.removeFrom(2);
list.print(); // 10 -> 15 -> 30 -> NULL
console.log("Size:", list.getSize()); // Size: 3
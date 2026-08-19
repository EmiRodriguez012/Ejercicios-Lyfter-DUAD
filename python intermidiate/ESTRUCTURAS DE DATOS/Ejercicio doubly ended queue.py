class Node:
    data: str

    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class LinkedList:
    head: Node
    tail: Node

    def __init__(self, head):
        self.head = head

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        self.tail = current_node

    def print_structure(self):
        current_node = self.head
    
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

class Deque(LinkedList):

    def __init__(self):
        self.head = None
        self.tail = None

    def push_right(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node   
            return
      
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

    def push_left(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node   
            return
        
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def pop_right(self):        
        removed = self.tail

        self.tail = self.tail.previous
        self.tail.next = None

        return removed

    def pop_left(self):
        removed = self.head

        self.head = self.head.next
        self.head.previous = None

        return removed

deque= Deque()

node_1 = Node("Soy el primer Nodo")
node_2 = Node("Soy el segundo Nodo")
node_3 = Node("Soy el tercer Nodo")

deque.push_right(node_1)
deque.push_right(node_2)
deque.push_right(node_3)

deque.pop_right()

print("Quitando un element")

deque.print_structure()


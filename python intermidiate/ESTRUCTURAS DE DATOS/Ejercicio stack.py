class Node:
  data: str

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  head: Node
  
  def __init__(self, head=None):
    self.head = head

  def print_structure(self):
    current_node = self.head

    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next

    
    

class Stack(LinkedList):
  def push(self, new_node):
    new_node.next = self.head
    self.head = new_node


  def pop (self):
    removed_head= self.head
    if self.head is not None:
      self.head = self.head.next
      return removed_head
    else:
      return None

  def is_empty(self):

    return self.head is None 
    

  def peek(self):

    if self.head is not None:
      return self.head.data
    else:
      return None

stack= Stack()

print(stack.is_empty())

stack.print_structure()

node_1 = Node("Soy el primer Nodo")
node_2 = Node("Soy el segundo Nodo")
node_3 = Node("Soy el tercer Nodo")

stack.push(node_1)

stack.print_structure()

stack.push(node_2)
stack.push(node_3)
stack.print_structure()

print(stack.is_empty())

print(stack.peek())








 
    




      


      
  

    
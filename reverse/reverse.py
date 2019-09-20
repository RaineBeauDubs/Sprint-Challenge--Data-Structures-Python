class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # set prev to be none
    prev = None
    # set the current to be self.head
    current = self.head
    #loop while self.head is not none
    while current is not None:
      # set next to be self.head.next_node
      next = current.next_node
      # not 100% sure why I have to put current.next instead of just "next," but it doesn't work without it, so I'll just deem it confusing magic, but this sets the prev from none to self.head.next_node.next.
      current.next = prev
      # do the magical switch dance
      prev = current
      current = next
    # escape loop and set self.head to be the new prev
    self.head = prev
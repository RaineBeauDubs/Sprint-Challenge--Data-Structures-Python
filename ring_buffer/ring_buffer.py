class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if len(self.storage) < self.capacity:
      # if there is enough room, just add the new item to the ring
      self.storage.append(item)
    else:
      # if the ring is full, we set the index of the item to what the current item is,
      self.storage[self.current] = item
      # and using the modulo pops off the oldest one from the list to make room for the new
      self.current = (self.current + 1) % self.capacity

  def get(self):
    ring_list = []
    # this loops through and basically adds everything that isn't a None to a new list...
    for item in self.storage:
      if item is not None:
        ring_list.append(item)
    # ...and then returns the new list.
    return ring_list
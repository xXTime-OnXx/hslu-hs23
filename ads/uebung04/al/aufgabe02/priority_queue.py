
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung04/al/aufgabe02
# Version: Tue Oct 10 09:56:22 CEST 2023

import functools
from full_priority_queue_exception import FullPriorityQueueException


class PriorityQueue:
  """ A heap-based (array-implementation) Priority-Queue with fixed length. """
  
  @functools.total_ordering
  class _PQEntry:
    
    def __init__(self, key, value):
      self._key = key
      self._value = value

    def get_key(self):
      return self._key

    def get_value(self):
      return self._value

    def __lt__(self, other):
      if other == None:
        return False
      return self._key < other._key 
    
    def __eq__(self, other):
      if other == None:
        return False
      return self._key == other._key
    
    def __str__(self):
      return "(" + str(self._key) + "," + str(self._value) +")"
    
    
  def __init__(self, max_size): 
    self._heap_array = [None] * (max_size+1)
    self._last = 0 # Points to the last element in the heap.

  def insert(self, key, value):
    if self._last == (len(self._heap_array) - 1):
      raise FullPriorityQueueException("Maximum reached: " + str(len(self._heap_array)))
    
    # TODO: Implement here...
    
    self._last += 1
    e = PriorityQueue._PQEntry(key, value)
    self._heap_array[self._last] = e
    
    self._upheap(self._last)
    
    return e
  
  def min(self):
    return self._heap_array[1]

  def remove_min(self):
    min_entry = self.min()
    self._heap_array[1] = self._heap_array[self._last]
    self._heap_array[self._last] = None
    self._last -= 1
    if not self.is_empty():
      self._downheap(1)
    return min_entry
  
  def is_empty(self):
    return self.size() == 0
  
  def size(self):
    return self._last
  
  def print(self):
    print(self.__str__())
    
  def __str__(self):
    string = "["
    for i in range(len(self._heap_array)):
      entry= self._heap_array[i]
      if entry != None:
        string += "[" + str(entry) + "," + str(i) + "]"
      else:
        string += "None"
      if i < len(self._heap_array)-1:
        string += ", "
    string += "]"
    return string 

  def _swap(self, parent_index, child_index):
    parent = self._heap_array[parent_index]
    child = self._heap_array[child_index]
    self._heap_array[parent_index] = child
    self._heap_array[child_index] = parent

  def _upheap(self, current_index):
    parent_index = current_index // 2
    parent = self._heap_array[parent_index]
    current = self._heap_array[current_index]
    if current_index > 1 and current.get_key() < parent.get_key():
      self._swap(parent_index, current_index)
      self._upheap(parent_index)

  def _downheap(self, current_index):
    print(self)
    print(f'index: {current_index}')
    print(f'size: {self.size()}')
    if current_index > self.size() // 2:
      return
    left_child_index = current_index * 2
    right_child_index = current_index * 2 + 1
    parent = self._heap_array[current_index]
    left_child = self._heap_array[left_child_index]
    right_child = self._heap_array[right_child_index]
    if right_child == None and parent.get_key() > left_child.get_key():
      self._swap(current_index, left_child_index)
      self._downheap(left_child_index)
    if right_child == None:
      return
    if parent.get_key() <= left_child.get_key() and parent.get_key() <= right_child.get_key():
      return
    if left_child.get_key() <= right_child.get_key():
      self._swap(current_index, left_child_index)
      self._downheap(left_child_index)
    else:
      self._swap(current_index, right_child_index)
      self._downheap(right_child_index)
  
  

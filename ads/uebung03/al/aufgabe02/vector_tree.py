
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung03/al/aufgabe02
# Version: Sun Oct  1 20:01:13 CEST 2023

import enum
from no_such_node_exception import NoSuchNodeException


ROOT_INDEX = 1

class VectorTree:
  
  class _child_side(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()

  def __init__(self):
    self._binary_tree = []
    self._binary_tree.append(None)
    self._binary_tree.append(None)
    self._size = 0
    
  def root(self):
    return self._binary_tree[ROOT_INDEX]
  
  def set_root(self, root):
    current_root = self.root()
    self.remove_left_child(current_root)
    self.remove_right_child(current_root)
    self._binary_tree[ROOT_INDEX] = root
    self._size = 1
    
  def parent(self, child):
    if self.root() == child:
      return None
    index_of_child = self._binary_tree.index(child)
    index_of_parent = index_of_child // 2
    return self._binary_tree[index_of_parent]
    
  def left_child(self, parent):
    index_of_parent = self._binary_tree.index(parent)
    index_of_left_child = index_of_parent * 2
    if self._index_out_of_range(index_of_left_child):
      return None
    return self._binary_tree[index_of_left_child]

  def right_child(self, parent):
    index_of_parent = self._binary_tree.index(parent)
    index_of_right_child = index_of_parent * 2 + 1
    if self._index_out_of_range(index_of_right_child):
      return None
    return self._binary_tree[index_of_right_child]

  def is_internal(self, node):
    has_left_child = self.left_child(node) != None
    print(self.left_child(node))
    has_right_child = self.right_child(node) != None
    return has_left_child or has_right_child

  def is_external(self, node):
    return not self.is_internal(node)
  
  def is_root(self, node):
    return self.root() == node;

  def set_right_child(self, parent, child):
    if not self._node_exists(parent):
      raise NoSuchNodeException('There is no node ' + parent + ' in the tree!')
    self.remove_right_child(parent)
    index_of_parent = self._binary_tree.index(parent)
    index_of_right_child = index_of_parent * 2 + 1
    if self._index_out_of_range(index_of_right_child):
      self._increase_tree_size()
    self._binary_tree[index_of_right_child] = child
    self._size += 1
  
  def set_left_child(self, parent, child):
    if not self._node_exists(parent):
      raise NoSuchNodeException('There is no node ' + parent + ' in the tree!')
    self.remove_left_child(parent)
    index_of_parent = self._binary_tree.index(parent)
    index_of_left_child = index_of_parent * 2
    if self._index_out_of_range(index_of_left_child):
      self._increase_tree_size()
    self._binary_tree[index_of_left_child] = child
    self._size += 1

  def remove_right_child(self, parent):
    right_child = self.right_child(parent)
    if right_child != None:
      self._remove_node(right_child)

  def remove_left_child(self, parent):
    left_child = self.left_child(parent)
    if left_child != None:
      self._remove_node(left_child)
       
  def size(self):
    return self._size

  def print_vector(self, message):
    print("\n" + message)
    print(self._binary_tree)

  def _remove_node(self, node):
    print('start remove ' + node)
    for child_side in VectorTree._child_side:
      child = self._child(node, child_side)
      if child != None:
        self._remove_node(child)
    print('remove ' + node)
    index_of_node = self._binary_tree.index(node);
    self._binary_tree[index_of_node] = None
    self._size -= 1

  def _child(self, parent, child_side):
    if child_side == VectorTree._child_side.LEFT:
      return self.left_child(parent)
    return self.right_child(parent)

  def _index_out_of_range(self, index):
    return len(self._binary_tree) - 1 < index

  def _increase_tree_size(self):
    current_tree_size = len(self._binary_tree)
    tree_buffer = [None for x in range(current_tree_size)]
    self._binary_tree.extend(tree_buffer)

  def _node_exists(self, node):
    return node in self._binary_tree
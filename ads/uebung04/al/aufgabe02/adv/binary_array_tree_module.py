from adv.ad_visualizer import ADV

class BinaryArrayTreeModule:

  def __init__(self, session_name, heap_array):
    self._session_name = session_name
    self._heap_array = heap_array
    self._max_left_height = -1
    self._max_right_height = -1
    self._tree_elements = None  # list
    self._relations = None  # list
    
  def snapshot(self):
    self._tree_elements = []
    self._relations = []
    self._array_elements = []
    self._traverse_preorder(1)
    
  def _traverse_preorder(self, index):
    content = str(self._heap_array[index])
    self._tree_elements.append(ADV.Element(index, content))
    #print(",".join(map(str, self._tree_elements)))
    
    if index > 1: # this is a child, so there is a new relation
      self._relations.append(ADV.Relation(index // 2, index))
      #print(",".join(map(str, self._relations)))
      
    if self._has_left_child(index):
      self._traverse_preorder(2 * index)
    if self._has_right_child(index):
      self._traverse_preorder(2 * index + 1)
  
  def _has_left_child(self, index):   
    left_child_index = 2 * index
    if left_child_index < len(self._heap_array) and self._heap_array[left_child_index] != None:
      return True
    else :
      return False
    
  def _has_right_child(self, index):   
    right_child_index = 2 * index + 1
    if right_child_index < len(self._heap_array) and self._heap_array[right_child_index] != None:
      return True
    else :
      return False

  def get_tree_elements(self):
    return self._tree_elements
  
  def get_relations(self):
    return self._relations
  
  def get_array_elements(self):
    array_elements = []
    for i in range(len(self._heap_array)):
      if self._heap_array[i] == None:
        array_elements.append(ADV.Element(i, "None"))
      else:
        array_elements.append(ADV.Element(i, str(self._heap_array[i])))
    #print(":".join(map(str, array_elements)))
    return array_elements
    
  def set_fixed_tree_height(self, max_left_height, max_right_height):
    self._max_left_height = max_left_height
    self._max_right_height = max_right_height
    
    
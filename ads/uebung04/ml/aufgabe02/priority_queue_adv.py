from uebung04.adv.binary_array_tree_module import BinaryArrayTreeModule
from uebung04.adv.ad_visualizer import ADV
from uebung04.ml.aufgabe02.priority_queue import PriorityQueue

class PriorityQueueADV(PriorityQueue):

  def __init__(self, max_size, session_name, max_left_height = -1, max_right_height = -1):
    super().__init__(max_size)
    self._adv_message = ""
    self._last_tree_content = ""
    self._adv_tree = BinaryArrayTreeModule(session_name, self._heap_array)
    if max_left_height != -1 and max_right_height != -1:
      self._adv_tree.set_fixed_tree_height(max_left_height, max_right_height)
      
  def insert(self, key, value):
    self._adv_message = "insert(" + str(key) + "," + str(value) + ")"
    entry = super().insert(key, value)
    self._display_on_adv()
    return entry
    
  def remove_min(self):
    self._adv_message = "removeMin(): "
    if self._heap_array[1] == None:
      self._adv_message += "None"
    else:
      self._adv_message += str(self._heap_array[1])
    removed_entry = super().remove_min()
    self._display_on_adv()
    return removed_entry
    
  def _swap(self, parent_index, child_index):
    self._display_on_adv()
    super()._swap(parent_index, child_index)
    self._display_on_adv()
      
  def _display_on_adv(self):
    current_tree_content = str(self)
    if current_tree_content != self._last_tree_content:
      ADV.snapshot(self._adv_tree, "\n" + self._adv_message)
    self._last_tree_content = current_tree_content
    
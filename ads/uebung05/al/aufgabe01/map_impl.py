
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung05/al/aufgabe01
# Version: Mon Oct 16 18:32:00 CEST 2023

import enum
from entry import Entry


class MapImpl:
  
  def __init__(self):  
    self._list = list()
  
  def size(self):
    return len(self._list)
  
  def is_empty(self):
    return self.size() == 0
  
  def put(self, key, value):
    entry = self.get(key)
    if entry:
      old_value = entry.get_value()
      entry.set_value(value)
      return old_value
    entry = Entry(key, value)
    self._list.append(entry)
    return None
      
  def get(self, key):
    entries = filter(lambda entry: entry.get_key() == key, self._list)
    if len(entries) > 0:
      return entries[0]
  
  def remove(self, key):
    # TODO: Implement here...
    return None
    
  def values(self):
    # TODO: Implement here...
    return None
  
  def key_set(self):
    # TODO: Implement here...
    return None
  
  def entry_set(self):
    # TODO: Implement here...
    return None
  
  def printMap(self, prefix = ""):
    print(prefix + "Printing map (" + str(self.size()) + " Entries): ")
    for e in self._list:
      print(f"  {e.get_key():3d}: {e.get_value()}")
      

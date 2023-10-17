
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung05/ml/aufgabe01
# Version: Mon Oct 16 18:32:46 CEST 2023

import enum
from uebung05.ml.aufgabe01.entry import Entry


class MapImpl:
  
  def __init__(self):  
    self._list = list()
  
  def size(self):
    return len(self._list)
  
  def is_empty(self):
    if self._list:
      return False
    else:
      return True
  
  def put(self, key, value):
    entry = self._find(key)
    if (entry != None):
      result = entry.set_value(value)
    else:
      self._list.append(Entry(key, value))
      result = None
    return result
      
  def _find(self, key): 
    it = iter(self._list)
    e = next(it, None)
    while e != None:
      this_key = e.get_key()
      if this_key == key:
        return e 
      e = next(it, None)
    return None
  
  def get(self, key):
    return self._get_remove(key, remove = False)
  
  def remove(self, key):
    return self._get_remove(key, remove = True)
    
  def _get_remove(self, key, remove):
    entry = self._find(key)
    if (entry != None):
      result = entry.get_value()
      if remove:
        self._list.remove(entry)
    else:
      result = None
    return result
  
  def values(self):
    values = list()
    for entry in self._list:
      values.append(entry.get_value())
    return values
  
  class _KeyOrEntry(enum.Enum):
    KEY = enum.auto()
    ENTRY = enum.auto()
  
  def key_set(self):
    return self._set_key_entry(MapImpl._KeyOrEntry.KEY)
  
  def entry_set(self):
    return self._set_key_entry(MapImpl._KeyOrEntry.ENTRY)
  
  def _set_key_entry(self, key_or_entry):
    the_set = set()
    for e in self._list:
      if key_or_entry == MapImpl._KeyOrEntry.KEY:
        the_set.add(e.get_key())
      else:
        the_set.add(e)
    return the_set
  
  def printMap(self, prefix = ""):
    print(prefix + "Printing map (" + str(self.size()) + " Entries): ")
    for e in self._list:
      print(f"  {e.get_key():3d}: {e.get_value()}")
      

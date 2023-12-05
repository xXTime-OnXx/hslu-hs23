
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung12/graphs
# Version: Sun Dec  5 12:31:44 CET 2021


class dict_ADV(dict):        
 
  def __init__(self, graph_adv, map_type):
    self._graph_adv = graph_adv
    self._map_type = map_type

  def __setitem__(self, key, value):
    operation = self._map_type + ".put"
    label = str(value).split(".")[1]
    self._graph_adv._send_message(operation + "," + str(key) + "," + label)
    return dict.__setitem__(self, key, value)
  
  def __getitem__(self, key):
    if self._map_type == "edgeMap" and not self._graph_adv._printing_maps:
      operation = self._map_type + ".get"
      self._graph_adv._send_message(operation + "," + str(key))
    return dict.__getitem__(self, key)
  
  

# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung12/al/aufgabe02
# Version: Fri Dec  1 17:48:30 CET 2023

import enum


class DirectedDFS:
  
  class _VertexLabel(enum.Enum):
    UNEXPLORED = enum.auto()
    VISITED = enum.auto()
    
  class _EdgeLabel(enum.Enum):
    UNEXPLORED = enum.auto()
    DISCOVERY = enum.auto()
    BACK = enum.auto()
    FORWARD = enum.auto()
    CROSS = enum.auto()
  
  def __init__(self): 
    self._vertex_map = dict()
    self._edge_map = dict()
    self._parent_map = dict()  
    # The parent-map maps a child to its parent
    self._graph = None
    
  def search(self, graph):
    self._graph = graph
    self._vertex_map = graph.get_vertex_map()
    self._edge_map = graph.get_edge_map()
    
    # TODO: Implement here...


  def _search(self, graph, v):
    print("{:21s}: {}".format("DirectedDFS.search()", str(v)))
    
    # TODO: Implement here...
      
      
  def print_maps(self):        
    self._graph.printing_maps(True)
    print("\nDirectedDFS.print_maps():")
    print("Vertex-Map : {", end = "")
    mappings = list()
    for v in self._vertex_map:
      mappings.append(v.__str__() + "=" + self._get_enum_name(self._vertex_map[v]))
    print(", ".join(mappings), end = "")
    print("}")
    print("Edge-Map   : {", end = "")
    mappings = list()
    for e in self._edge_map:
      mappings.append(e.__str__() + "=" + self._get_enum_name(self._edge_map[e]))
    mappings.sort()
    print(", ".join(mappings), end = "")
    print("}")
    self._graph.printing_maps(False)
    
  def _get_enum_name(self, enum_value):
    return enum_value.__str__().split(".")[1]

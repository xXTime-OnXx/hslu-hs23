
import json
import socket
from time import time

class ADV:
  
  _IP = "127.0.0.1"
  _PORT = 8765
  
  _session_id = int(time())
  _snapshot_id = 0
    
  class Element:
    
    def __init__(self, identifier: int, content: str):
      self._id = identifier
      self._content = content
    
    def __str__(self):
      return "(" + str(self._id) + ":"+ self._content + ")"
    
  class Relation:
    
    def __init__(self, source: int, target: int):
      self._source_element_id = source
      self._target_element_id = target
  
    def __str__(self):
      return "(" + str(self._source_element_id) + "->" + str(self._target_element_id) + ")"

  
  def snapshot(cls, advTree, snapshot_description):
    
    advTree.snapshot()
    
    tree_elements = []
    for e in advTree.get_tree_elements():
      element = {}
      element["id"] = e._id
      element["content"] = e._content
      tree_elements.append(element)

    relations = []
    for r in advTree.get_relations():
      relation = {}
      relation["sourceElementId"] = r._source_element_id
      relation["targetElementId"] = r._target_element_id
      relation["label"] = ""
      relation["directed"] = False
      relations.append(relation)
      
    meta_data = {}
    meta_data["max-right-tree-height"] = str(advTree._max_left_height)
    meta_data["max-left-tree-height"] = str(advTree._max_right_height)
      
    array_elements = []
    for e in advTree.get_array_elements():
      element = {}
      element["id"] = e._id
      element["content"] = e._content
      array_elements.append(element)
      
    tree_binary = {}
    tree_binary["moduleName"] = "tree-binary"
    tree_binary["elements"] = tree_elements
    tree_binary["relations"] = relations
    tree_binary["flags"] = ["show-array-indices"]
    tree_binary["metaData"] = meta_data 
    tree_binary["position"] = "DEFAULT"
    
    array = {}
    array["moduleName"] = "array"
    array["elements"] = array_elements
    array["relations"] = []
    array["flags"] = ["show-array-indices"]
    array["metaData"] = {} 
    array["position"] = "BOTTOM"
    
    module_groups = []
    module_groups.append(tree_binary)
    module_groups.append(array)
    
    snapshot_dict = {}
    ADV._snapshot_id += 1
    snapshot_dict["snapshotId"] = ADV._snapshot_id
    snapshot_dict["snapshotDescription"] = snapshot_description
    snapshot_dict["moduleGroups"] = module_groups
    snapshot_list = []
    snapshot_list.append(snapshot_dict)
    
    snapshot = {}
    snapshot["snapshots"] = snapshot_list
    snapshot["sessionId"] = ADV._session_id
    snapshot["sessionName"] = advTree._session_name
    
    adv_request = {}
    adv_request["command"] = "TRANSMIT"
    adv_request["json"] = json.dumps(snapshot)
    
    ADV.send_snapshot(json.dumps(adv_request))
    
#    adv_request = {}
#    adv_request["command"] = "TRANSMIT"
#    snapshot_dict["snapshotId"]  = 2
#    adv_request["json"] = json.dumps(snapshot)
#    ADV.send_snapshot(json.dumps(adv_request))
    
  snapshot = classmethod(snapshot)
  
  def send_snapshot(cls, adv_request_json_string):
    #print("Request  : ", adv_request_json_string)
    with socket.create_connection((ADV._IP, ADV._PORT)) as s:
      s.send(adv_request_json_string.encode())
      s.send("\n".encode()) # otherwise, the server does not read in the message!
      response = s.recv(1024)
      #print("Response : >{}<".format(response.decode()))
      s.close()
    
  send_snapshot = classmethod(send_snapshot)
  

  

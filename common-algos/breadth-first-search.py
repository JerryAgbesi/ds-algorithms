from collections import deque

graph = {}

graph["Me"] = ["Liliana", "Gideon", "Chandra","Sam"]
graph["Liliana"] = ["Cheeto","Bob"]
graph["Cheeto"] = ["Sam"]
graph["Gideon"] = []
graph["Chandra"] = ["Carmy","Levon","Sam","Ama"]
graph["Carmy"] = ["Sam"]
graph["Mike"] = []
graph["Cheeto"] = []
graph["Bob"] = []
graph["Sam"] = ["Carmy","Kwame"]
graph["Levon"] = ["Deveon"]

def isGhanaian(name: str)-> bool:
  return name in ["Ama","Yaw","Kwame"]

def bfs(name):
  search_queue = deque()
  seen = set()
  search_queue += graph[name]

  while search_queue:
    person = search_queue.popleft()
    if not person in seen:
      seen.add(person)
      if isGhanaian(person):
        print(person)
        return True
      else:
        search_queue += graph[person]
        
  return False

bfs("Me")

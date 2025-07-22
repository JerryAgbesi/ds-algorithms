from collections import deque


graph = {}

degrees = 0

graph["Jace"] = ["Liliana", "Gideon", "Chandra","Sam"]
graph["Liliana"] = ["Cheeto","Bob"]
graph["Cheeto"] = ["Sam"]
graph["Gideon"] = []
graph["Chandra"] = ["Carmy","Levon","Sam"]
graph["Carmy"] = ["Sam"]
graph["Mike"] = []
graph["Cheeto"] = []
graph["Bob"] = []
graph["Sam"] = ["Carmy","Chandra"]
graph["Levon"] = ["Deveon"]



def is_developer(name):
    return name[0] == "D"

def bfs(search_queue,seen):
    if not search_queue:
         return False
    
    person = search_queue.popleft()
    if not person in seen:
        if is_developer(person):
            print(f"{person} is a developer")
            return True
        else:
            search_queue += graph[person]
            seen.add(person)
    
    return bfs(search_queue,seen)

def run():
     search_queue = deque()
     seen = set()
     search_queue += graph["Jace"]

     return bfs(search_queue,seen)

            
print(run())




            
from collections import deque,defaultdict
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        queue = deque()
        nodes = defaultdict(list)

        for u,v in edges:
            nodes[u].append(v)
            nodes[v].append(u)
        
        queue.append(source)

        while queue:
            current = queue.popleft()
            if current in visited:
                continue

            visited.add(current)

            if current == destination:
                return True

            for i in nodes[current]:
                queue.append(i)    

        return False        

        


            
new = Solution()

print(new.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))
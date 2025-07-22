from typing import List

def countStableSegments(capacity: List[int]) -> int:
      stable = 0

      l,r = 0,2

      while r <= len(capacity)-1:
          if capacity[l] == capacity[r] and capacity[r] == sum(capacity[l+1:r]):
              stable +=1
          r += 1
          l=+1
         
      l-=1
      while l >= 0:
          if capacity[l] == capacity[-1] and capacity[-1] == sum(capacity[l+1:len(capacity)-1]):
             
              stable +=1
             
          l -= 1

      return stable

print(countStableSegments(capacity = [9,3,3,3,9]))


from typing import List



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        

        for index,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stacki,stackt = stack.pop()
                answer[stacki] = (index-stacki)
            stack.append((index,temp))    
        return answer    

new_solu = Solution()

new_solu.dailyTemperatures([71,72,71])
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        pairs = {'(':')','[':']','{':'}'}
        stack = []
        
        if len(s) <= 1:
            return False
        
        for p in s:
            if p in pairs.keys():
                stack.append(p)
        
            else:
                if len(stack) > 0:
                    if pairs[stack.pop()] == p:
                        continue
                    else:
                        return False
                else:
                    return False
                
        return len(stack) == 0        
    
        
                

         

mine = Solution()

print(mine.isValid("([])[()]{[]}"))

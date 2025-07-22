class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
       #shift all values not equal to val to the left
      
        j = 0
        vals = nums.count(val)
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1   
        
        k = len(nums) - vals        
            
               
        return k        
            
class Solution(object):
    def removeElement(self, nums, val):
        result = []
        for i in nums:
            if val != i:
                result.append(i)
        return result
        

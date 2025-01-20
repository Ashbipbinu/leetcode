class Solution(object):
    def removeElement(self, nums, val):
        # Create an empty list to store the result
        result = []
        
        # Iterate through each element in the input list `nums`
        for i in nums:
            # Check if the current element is not equal to the value to be removed
            if val != i:
                # If not equal, add the element to the result list
                result.append(i)
        
        # Return the result list containing all elements except those equal to `val`
        return result

class Solution(object):
    def twoSum(self, nums, target):
        # Create an empty dictionary to store the difference and its index
        dict = {}
        
        # Iterate through the list with both index and value
        for i, num in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - num

            # Check if the current number is already in the dictionary
            if not num in dict:
                # If not found, store the difference as the key and the index as the value
                dict[diff] = i
            else:
                # If found, return the stored index and the current index
                return (dict[num], i)
        
        # If no such pair is found, return -1
        return -1

# Create an instance of the Solution class
sol = Solution()

# Call the twoSum method with a list and a target and print the result
print(sol.twoSum(nums=[2, 7, 11, 15], target=9))

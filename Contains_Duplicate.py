class Solution(object):
    def containsDuplicate(self, nums):
        # Create an empty set to store unique elements from the list
        setter = set()

        # Iterate through each number in the input list
        for num in nums:
            # Check if the current number is already in the set
            if num in setter:
                # If it is, we found a duplicate, so return True
                return True
            # If not, add the current number to the set
            setter.add(num)

        # If we go through the entire list without finding duplicates, return False
        return False

# Create an instance of the Solution class
sol = Solution()

# Test the method with a list of numbers and print the result
print(sol.containsDuplicate([1, 2, 3]))  # Expected output: False

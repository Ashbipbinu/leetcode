class Solution(object):
    def search(self, nums, target):
        # Get the length of the list
        n = len(nums)
        
        # Initialize the left and right pointers
        l = 0
        r = n - 1
        
        # While the left pointer is less than or equal to the right pointer
        while l <= r:
            # Check if the left pointer points to the target
            if nums[l] == target:
                return l
            
            # Check if the right pointer points to the target
            if nums[r] == target:
                return r
            
            # Calculate the middle index
            mid = (l + r) // 2
            
            # Check if the middle element is the target
            if target == nums[mid]:
                return mid
            
            # If the left part of the array is sorted
            if nums[l] <= nums[mid]:
                # Check if the target is in the left sorted part
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1  # Narrow down to the left half
                else:
                    l = mid + 1  # Otherwise, search the right half
            else:
                # If the right part of the array is sorted
                # Check if the target is in the right sorted part
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1  # Narrow down to the right half
                else:
                    r = mid - 1  # Otherwise, search the left half
        
        # Return -1 if the target is not found
        return -1

# Test the function
sol = Solution()
nums = [1, 2, 3, 4, 5, 6]
target = 4

# Print the index of the target in the list
print(sol.search(nums, target))

class Solution(object):
    # Function to find the minimum element in a rotated sorted array
    def findMin(self, nums):
        # Get the length of the array
        n = len(nums)
        
        # Initialize the pointers for the binary search
        start = 0
        end = n - 1

        # Perform binary search to find the minimum element
        while start <= end:
            # If the start and end pointers converge, return the element at that position
            if start == end:
                return nums[start]
            
            # Calculate the middle index
            mid = (start + end) // 2
            
            # If the middle element is greater than the end element, the minimum is in the right half
            if nums[mid] > nums[end]:
                start = mid + 1
                continue  # Skip to the next iteration of the loop
            
            # Otherwise, the minimum is in the left half (or at the middle)
            end = mid
        
        # Return the element at the middle index (this is a fallback and shouldn't typically execute)
        return nums[mid]

# Create an instance of the Solution class
sol = Solution()

# Define a rotated sorted array
nums = [2, 3, 4, 5, 1]

# Print the result of the findMin function
print(sol.findMin(nums))

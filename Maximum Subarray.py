class Solution:
    def maxSubArray(self, nums):
        # Initialize variables to track the current sum and the maximum sum
        sum = 0
        max_sum = float("-inf")  # Set max_sum to negative infinity as the initial value

        # Handle the edge case where the array contains only one element
        if len(nums) == 1:
            return nums[0]

        # Iterate through the list to calculate the maximum subarray sum
        for num in nums:
            # If the current sum becomes negative, reset it to 0
            if sum < 0:
                sum = 0

            # Add the current number to the sum
            sum += num

            # Update max_sum if the current sum is greater than the previous max_sum
            max_sum = max(sum, max_sum)

        # Return the maximum subarray sum found
        return max_sum


# Create an instance of the Solution class
sol = Solution()

# Test the method with an example array
nums = [-2, -1]  # Example input array
print(sol.maxSubArray(nums))  # Expected output: -1

class Solution(object):
    def maxProduct(self, nums):
        # Initialize variables
        n = len(nums)  # Length of the input array
        mult_start = 1  # Tracks product from the start of the array
        mult_end = 1    # Tracks product from the end of the array
        max_prod = None  # Stores the maximum product found

        # Special case: if the array has only one element, return it
        if len(nums) == 1:
            return nums[0]
        
        # Loop through the array
        for i in range(0, n):
            j = n - i - 1  # Index from the end of the array
            
            # Reset product to 1 if encountering a zero in the forward or backward product
            if mult_start == 0:
                mult_start = 1
            if mult_end == 0:
                mult_end = 1

            # Update the products for the current indices
            mult_start = mult_start * nums[i]  # Forward product
            mult_end = mult_end * nums[j]      # Backward product

            # If max_prod is not initialized, set it to the maximum of the current products
            if max_prod is None:
                max_prod = max(mult_start, mult_end)
                continue
            
            # Update the maximum product so far
            max_prod = max(mult_start, mult_end, max_prod)

        # Return the maximum product found
        return max_prod

# Instantiate the Solution class
sol = Solution()

# Test the function with an example array
print(sol.maxProduct([-3, 0, 1, -2]))  # Output: 1

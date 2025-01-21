class Solution:
    def productExceptSelf(self, nums):
        # Initialize variables for left and right cumulative products
        l_mult = 1  # Left cumulative product
        r_mult = 1  # Right cumulative product
        n = len(nums)  # Length of the input list
        
        # Initialize arrays to store cumulative products
        l_arr = [1] * n  # Left product array initialized to 1
        r_arr = [1] * n  # Right product array initialized to 1

        # Calculate cumulative products from the left and the right
        for i in range(n):
            j = -i - 1  # Index for iterating from the right
            
            # Store the left cumulative product at index i
            l_arr[i] = l_mult
            # Store the right cumulative product at index j
            r_arr[j] = r_mult
            
            # Update the cumulative products
            l_mult *= nums[i]  # Multiply by the current element for the left product
            r_mult *= nums[j]  # Multiply by the current element for the right product

        # Combine left and right products for the final result
        return [l * r for l, r in zip(l_arr, r_arr)]



# Test the function
sol = Solution()
nums = [1, 2, 3, 4]
print(sol.productExceptSelf(nums))

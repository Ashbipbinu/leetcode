class Solution(object):
    def getSum(self, a, b):
        # Define a mask to limit the result to 32 bits (handling negative numbers in Python)
        mask = 0xffffffff  

        # Loop until there is no carry left
        while (mask & b) != 0:
            # Calculate the carry (common set bits of a and b) and shift left
            carry = (a & b) << 1  

            # Perform bitwise XOR to sum bits without carrying
            a = (a ^ b)  

            # Move the carry to b for the next iteration
            b = carry  

        # Return the result, ensuring it fits within 32-bit signed integer limits
        return (mask & a) if b > 0 else a  


# Create an instance of the Solution class
sol = Solution()

# Test the function with inputs 12 and 1
print(sol.getSum(12, 1))  # Output: 13

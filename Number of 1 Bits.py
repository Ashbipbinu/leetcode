class Solution(object):
    def hammingWeight(self, n):
        # Convert the integer 'n' to its binary representation (as a string)
        bit_int = bin(n)  # Example: bin(7) -> '0b111'
        
        # Get the length of the binary string and use it as an index
        n = len(bit_int) - 1  # Last index of the binary string
        
        counter = 0  # Initialize a counter to keep track of '1' bits

        # Loop until we reach the 'b' character in '0b...' (binary notation prefix)
        while bit_int[n] != 'b':  
            # If the current character is '1', increment the counter
            if bit_int[n] == '1':
                counter = counter + 1  # Increase the count of '1' bits
            
            # Move to the previous character in the binary string
            n = n - 1  

        return counter  # Return the count of '1' bits


# Test case
n = 7  # Binary representation: '0b111' (3 ones)
sol = Solution()
print(sol.hammingWeight(n))  # Output: 3

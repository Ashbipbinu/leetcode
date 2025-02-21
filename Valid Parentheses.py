class Solution(object):
    def isValid(self, s):
        # Convert the input string into a list of characters
        paran_arr = list(s)
        
        # Dictionary to store matching pairs of brackets
        symbols = {'(': ')', '{': '}', '[': ']'}
        
        # Stack to keep track of expected closing brackets
        stack = []
        
        # Iterate through each character in the input string
        for c in paran_arr:
            # If it's an opening bracket, push its corresponding closing bracket onto the stack
            if c in symbols:
                stack.append(symbols[c])
                continue

            # If it's a closing bracket, check if it matches the top of the stack
            if len(stack) and c == stack[-1]:  
                stack.pop()  # If it matches, remove the top element from the stack
                continue
            else:
                return False  # If it doesn't match, the string is invalid

        # If the stack is empty, all brackets were properly matched
        return len(stack) == 0  

# Create an instance of the Solution class
sol = Solution()

# Test case: an invalid string containing only closing brackets
symbols = "){"
print(sol.isValid(symbols))  # Output: False

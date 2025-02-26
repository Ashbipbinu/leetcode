class Solution(object):
    def isPalindrome(self, s):
        # Remove all spaces and convert the string to lowercase
        s = s.replace(" ", '').lower()

        # Initialize two pointers: one at the beginning (l) and one at the end (r)
        l = 0
        r = len(s) - 1

        # Iterate while left pointer is less than or equal to the right pointer
        while l <= r:
            
            # Skip non-alphanumeric characters from the left
            if not s[l].isalnum():
                l = l + 1  # Move left pointer forward
                continue  # Skip the rest of the loop and recheck the new character

            # Skip non-alphanumeric characters from the right
            if not s[r].isalnum():
                r = r - 1  # Move right pointer backward
                continue  # Skip the rest of the loop and recheck the new character

            # Compare characters at left and right pointers
            if s[l] != s[r]:
                return False  # If mismatch, it's not a palindrome

            # Move both pointers inward
            l = l + 1
            r = r - 1

        # If the entire string has been checked and no mismatches found, return True
        return True


s = "A man, a plan, a canal: Panama"

sol = Solution()

print(sol.isPalindrome(s))  # Expected output: True

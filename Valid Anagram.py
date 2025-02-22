class Solution(object):
    def isAnagram(self, s, t):
        # Create two dictionaries to store character frequencies
        dict1 = {}
        dict2 = {}

        # Count the occurrences of each character in the first string (s)
        for c in s:
            if c not in dict1:
                dict1[c] = 1  # If character appears for the first time, set count to 1
            else:
                dict1[c] = dict1[c] + 1  # Otherwise, increase the count

        # Count the occurrences of each character in the second string (t)
        for c in t:
            if c not in dict2:
                dict2[c] = 1  # If character appears for the first time, set count to 1
            else:
                dict2[c] = dict2[c] + 1  # Otherwise, increase the count

        # Compare both dictionaries to check if they have the same character frequencies
        return dict1 == dict2

# Create an instance of the Solution class
sol = Solution()

# Define two strings to check if they are anagrams
s, t = "anagram", "nagaram"

# Print the result of the isAnagram function
print(sol.isAnagram(s, t))  # Output: True

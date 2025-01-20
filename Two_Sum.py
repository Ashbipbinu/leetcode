class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        
        for i, num in enumerate(nums):
            diff = target - num

            if not num in dict:
                dict[diff] = i
            else:
                return (dict[num], i)
        return -1
    
sol = Solution()

print(sol.twoSum(nums = [2,7,11,15], target = 9))

        
class Solution(object):

    def search(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1
        
        while l <= r:

            if nums[l] == target:
                return l
            
            if nums[r] == target:
                return r

            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
       
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1


sol = Solution()

nums = [1,2,3,4,5,6]
target = 4
print(sol.search(nums, target))
        
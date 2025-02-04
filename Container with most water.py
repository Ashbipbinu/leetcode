class Solution(object):
    def maxArea(self, height):

        l = 0
        r = len(height) - 1

        maxArea = 0
        
        while l < r:

            area = min(height[l], height[r]) * (r - l)

            maxArea = max(area, maxArea)

            if height[l] < height[r]:
                l = l + 1
                continue
         
            r = r - 1
            continue
    

        return maxArea







sol = Solution()

height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))
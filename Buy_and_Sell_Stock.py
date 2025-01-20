class Solution:
    def maxProfit(self, nums):
        buy = 0
        sell = 1

        max_profit = 0

        while sell < len(nums):
            
            if nums[buy] < nums[sell]:
                profit = nums[sell] - nums[buy]
                max_profit = max(profit, max_profit)
            else:
                buy = sell
            
            sell = sell + 1

        return max_profit

sol = Solution()

arr = [7,1,5,3,6,4]

print(sol.maxProfit(arr))
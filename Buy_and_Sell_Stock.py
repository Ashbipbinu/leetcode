class Solution:
    def maxProfit(self, nums):
        # Initialize pointers for the buy and sell days
        buy = 0
        sell = 1

        # Initialize the variable to store the maximum profit
        max_profit = 0

        # Loop through the list until the sell pointer reaches the end
        while sell < len(nums):
            
            # Check if the current buy price is less than the sell price
            if nums[buy] < nums[sell]:
                # Calculate the profit
                profit = nums[sell] - nums[buy]
                # Update max_profit if the current profit is greater
                max_profit = max(profit, max_profit)
            else:
                # If the sell price is less than or equal to the buy price,
                # move the buy pointer to the current sell pointer
                buy = sell
            
            # Move the sell pointer to the next day
            sell = sell + 1

        # Return the maximum profit found
        return max_profit

# Create an instance of the Solution class
sol = Solution()

# Example input list of stock prices
arr = [7, 1, 5, 3, 6, 4]

# Call the maxProfit method and print the result
print(sol.maxProfit(arr))  # Output: 5

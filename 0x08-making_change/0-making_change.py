#!/usr/bin/python3
def makeChange(coins, total):  
    if total <= 0:  
        return 0  
    
    dp = [float('inf')] * (total + 1)  
    dp[0] = 0  # Base case: 0 coins are needed to make total of 0  
    
    # Iterate over each coin  
    for coin in coins:  
        # For each coin, update the dp array from the coin value to total  
        for t in range(coin, total + 1):  
            dp[t] = min(dp[t], dp[t - coin] + 1)  
    
    # If dp[total] is still infinity, return -1 (not possible to form total)  
    return dp[total] if dp[total] != float('inf') else -1
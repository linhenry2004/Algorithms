def rod(prices, n):
    max_price = 0
    for length in range(1, n+1):
        max_price = max(max_price, prices[length]+rod(prices, n-length))
    return max_price
 
 
def rod(prices, n, lookup=None):
    lookup = {} if lookup is None else lookup
    if n in lookup:
        return lookup[n]
    max_price = 0
    for length in range(1, n+1):
        max_price = max(max_price, prices[length]+rod(prices, n-length, lookup))
    lookup[n] = max_price
    return lookup[n]
 
 
def rod(prices, n):
    dp = [0]*(n+1)
    for i in range(1, n+1):
        for length in range(1, i+1):
            dp[i] = max(dp[i], prices[length]+dp[i-length])
    return dp[n]

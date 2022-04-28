def knapsack(values, weights, k, i=0):
    if i == len(values):
        return 0
    elif weights[i] > k:
        return knapsack(values, weights, k, i+1)
    else:
        return max(values[i]+knapsack(values, weights, k-weights[i], i+1), knapsack(values, weights, k, i+1))
 
 
def knapsack(values, weights, k, i=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if (k, i) in lookup:
        return lookup[(k, i)]
    elif i == len(values):
        return 0
    elif weights[i] > k:
        lookup[(k, i)] = knapsack(values, weights, k, i+1, lookup)
        return lookup[(k, i)]
    else:
        lookup[(k, i)] = max(values[i]+knapsack(values, weights, k-weights[i], i+1, lookup), knapsack(values, weights, k, i+1, lookup))
        return lookup[(k, i)]
 
 
def knapsack(values, weights, k):
    if k == 0:
        return 0
    elif k >= sum(weights):
        return sum(values)
    n = len(values)
    dp = [[0]*(k+1) for i in range(n)]
    for i in range(weights[0], k+1):
        dp[0][i] = values[0]
    for i in range(1, n):
        for j in range(k+1):
            if weights[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(values[i]+dp[i-1][j-weights[i]], dp[i-1][j])
    return dp[n-1][k]
 
 
def knapsack(values, weights, k):
    if k == 0:
        return 0
    elif k >= sum(weights):
        return sum(values)
    n = len(values)
    prev_dp = [0]*(k+1)
    dp = [0]*(k+1)
    for i in range(weights[0], k+1):
        prev_dp[i] = values[0]
    for i in range(1, n):
        for j in range(k+1):
            if weights[i] > j:
                dp[j] = prev_dp[j]
            else:
                dp[j] = max(values[i]+prev_dp[j-weights[i]], prev_dp[j])
        prev_dp = dp
        dp = [0]*(k+1)
    return prev_dp[k]
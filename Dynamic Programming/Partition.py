def partition(arr, i=0, sum1=0, sum2=0):
    if i == len(arr):
        return sum1 == sum2
    else:
        return partition(arr, i+1, sum1+arr[i], sum2) or partition(arr, i+1, sum1, sum2+arr[i])
 
 
def subsets(arr, k):
    n = len(arr)
    if k > sum(arr) or n == 0:
        return 0
    dp = [[0]*(k+1) for i in range(n)]
    dp[0][0] = 1
    if arr[0] <= k:
        dp[0][arr[0]] = 1
    for i in range(1, n):
        for j in range(k + 1):
            dp[i][j] = dp[i-1][j] + (dp[i-1][j-arr[i]] if j-arr[i] >= 0 else 0)
    return dp[n-1][k]
 
 
def partition(arr):
    s = sum(arr)
    if s%2 == 1:
        return False
    else:
        return subsets(arr, s//2) > 0

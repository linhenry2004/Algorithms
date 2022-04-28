def inter(s1, s2, s3, i=0, j=0):
    if len(s1)+len(s2) != len(s3):
        return False
    elif i == len(s1) and j == len(s2):
        return True
    else:
        return (i < len(s1) and s1[i] == s3[i+j] and inter(s1, s2, s3, i+1, j)) or (j < len(s2) and s2[j] == s3[i+j] and inter(s1, s2, s3, i, j+1))
 
 
def inter(s1, s2, s3, i=0, j=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if (i, j) in lookup:
        return lookup[(i, j)]
    if len(s1)+len(s2) != len(s3):
        return False
    elif i == len(s1) and j == len(s2):
        return True
    else:
        lookup[(i, j)] = (i < len(s1) and s1[i] == s3[i+j] and inter(s1, s2, s3, i+1, j, lookup)) or (j < len(s2) and s2[j] == s3[i+j] and inter(s1, s2, s3, i, j+1, lookup))
        return lookup[(i, j)]
 
 
def inter(s1, s2, s3):
    n, m = len(s1), len(s2)
    if n+m != len(s3):
        return False
    dp = [[False]*(m+1) for i in range(n+1)]
    dp[0][0] = True
    for j in range(1, m+1):
        dp[0][j] = s2[j-1] == s3[j-1] and dp[0][j-1]
    for i in range(1, n+1):
        dp[i][0] = s1[i-1] == s3[i-1] and dp[i-1][0]
    for i in range(1, n+1):
        for j in range(1, m+1):
            check_s1 = s1[i-1] == s3[i+j-1] and dp[i-1][j]
            check_s2 = s2[j-1] == s3[i+j-1] and dp[i][j-1]
            dp[i][j] = check_s1 or check_s2
    return dp[n][m]
 
 
def inter(s1, s2, s3):
    n, m = len(s1), len(s2)
    if n+m != len(s3):
        return False
    prev_dp = [False]*(m+1)
    dp = [False]*(m+1)
    prev_dp[0] = True
    for j in range(1, m+1):
        prev_dp[j] = s2[j-1] == s3[j-1] and prev_dp[j-1]
    for i in range(1, n+1):
        dp[0] = s1[i-1] == s3[i-1] and prev_dp[0]
        for j in range(1, m+1):
            check_s1 = s1[i-1] == s3[i+j-1] and prev_dp[j]
            check_s2 = s2[j-1] == s3[i+j-1] and dp[j-1]
            dp[j] = check_s1 or check_s2
        prev_dp = dp
        dp = [False]*(m+1)
    return prev_dp[m]
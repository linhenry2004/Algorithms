def chain(matrices):
    def _chain(matrices, i, j):
        if i == j:
            return 0
        else:
            min_cost = float("inf")
            for k in range(i, j):
                left_cost = _chain(matrices, i, k)
                right_cost = _chain(matrices, k+1, j)
                product_cost = matrices[i][0]*matrices[k][1]*matrices[j][1]
                min_cost = min(min_cost, left_cost+right_cost+product_cost)
            return min_cost
    return _chain(matrices, 0, len(matrices)-1)
 
 
def chain(matrices):
    def _chain(matrices, i, j, lookup=None):
        lookup = {} if lookup is None else lookup
        if (i, j) in lookup:
            return lookup[(i, j)]
        if i == j:
            return 0
        else:
            min_cost = float("inf")
            for k in range(i, j):
                left_cost = _chain(matrices, i, k, lookup)
                right_cost = _chain(matrices, k+1, j, lookup)
                product_cost = matrices[i][0]*matrices[k][1]*matrices[j][1]
                min_cost = min(min_cost, left_cost+right_cost+product_cost)
            lookup[(i, j)] = min_cost
            return lookup[(i, j)]
    return _chain(matrices, 0, len(matrices)-1)
 
 
def chain(matrices):
    n = len(matrices)
    dp = [[0]*n for i in range(n)]
    for d in range(1, n):
        for i in range(n-d):
            j = i+d
            min_cost = float("inf")
            for k in range(i, j):
                left_cost = dp[i][k]
                right_cost = dp[k+1][j]
                product_cost = matrices[i][0]*matrices[k][1]*matrices[j][1]
                min_cost = min(min_cost, left_cost+right_cost+product_cost)
            dp[i][j] = min_cost
    return dp[0][n-1]

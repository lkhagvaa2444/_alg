# Recursive + Memoization (Lookup Table)
def power2n_d(n, memo={}):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    
    memo[n] = 2 * power2n_d(n-1, memo)  # Recursive call with memoization, it is always faster
    #memo[n] = power2n_d(n-1, memo) + power2n_d(n-1, memo)
    return memo[n]

# Test the function
print('power2n(10)=', power2n_d(900))
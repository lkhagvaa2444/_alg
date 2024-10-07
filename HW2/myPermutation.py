def my_permute(n):
    p = []  # This will hold the partial permutations
    permute_next(n, p)

def permute_next(n, p):
    i = len(p)  # Get the current length of the permutation
    if i == n:  # If the permutation is complete, print it
        print(p)
        return
    
    for x in range(n):  # Try all numbers from 0 to n-1
        if x not in p:  # If x is not already in p
            p.append(x)  # Add it to the current permutation
            permute_next(n, p)  # Recursively permute the remaining elements
            p.pop()  # Remove x and backtrack

if __name__ == "__main__":
    my_permute(3)  # Test with n = 3

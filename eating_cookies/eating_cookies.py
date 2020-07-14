'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    CACHE = {1: 1, 2: 2, 3: 4}

    def helper(n):
        counter = 0

        if n < 1:
            return 0
        elif n in CACHE:
            return CACHE.get(n)
        else:
            CACHE[n] = helper(n - 1) + helper(n - 2) + helper(n - 3)
            return CACHE.get(n)
    
    if n == 0:
        return 1
    
    return helper(n)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 999

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

# Rod Cutting Recurive Solution
# Running Time: T(n) = O(2 ** n) - Non-Polynomial RunTime

from math import inf 

def cut_rod(p, n):
    """
    Let p bet the price of each rod at length i
    Let n be the size of the rod from i .. n
    Let q be the maximum profit for the length n
    """
    # Base Case
    if n > len(p):
        return None
    if n < 0:
        return None
    if n == 0:
        return 0
    
    # Recursive Case
    q = -inf

    for i in range(1, n + 1):
        q = max(q,  p[i-1] + cut_rod(p, n-i))
        print(q)
    
    return q



if __name__ == "__main__":
    # Example 1
    ## Problem: Given a steal rod of length n, cut it into pieces to maximize the profit ..
    ## where profit for a piece of length i is given as price subscript i
    rod_length = [1, 2, 3, 4, 5]
    rod_price =  [1, 5, 8, 9, 10]
    n = 6

    print("Maximum Revenue in Example 1 is ", cut_rod(rod_price, n))


# Rod Extended Cutting Buttom-Up 
# Running Time: T(n) = O(n ** 2) - Quadratic RunTime

from math import inf 

def extended_buttom_up_cut_rod(p, n):
    """
    Let p bet the price of each rod at length i
    Let n be the size of the rod from i .. n
    Let q be the maximum profit for the length n
    Let r be a list of substructure optimal revenue
    """
     # Edge Case
    if n > len(p):
        return None
    if n < 0:
        return None

    # Initializing memo(a List r to keep maximum revnue)  
    r = [None] * (n+1)
    # Additional list or array to keep the cutting positions 
    cut = [None] * (n+1)
    r[0] = 0
    

    for j in range(1, n+1):
        q = -inf
        for i in range(j):
            if q < (p[i] + r[j-i-1]):
                q = p[i] + r[j-i-1]
                # The best first cut for the length j
                cut[j] = i+1
        r[j] = q

    return r[n], cut


if __name__ == "__main__":
    # Example 1
    ## Problem: Given a steal rod of length n, cut it into pieces to maximize the profit ..
    ## where profit for a piece of length i is given as price subscript i
    rod_length = [1, 2, 3, 4, 5]
    rod_price =  [1, 5, 8, 9, 10]
    n = 0

    print("Maximum Revenue in Example 1 is ", extended_buttom_up_cut_rod(rod_price, n))

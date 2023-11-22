# Output a complete list of cut sizes

from cutrodD import extended_buttom_up_cut_rod

def print_cut_rod_solution(p, n):
    """
    Let p bet the price of each rod at length i
    Let n be the size of the rod from i .. n
    """

    # Edge Case
    if n > len(p):
        return None
    if n < 0:
        return None

    r, cut = extended_buttom_up_cut_rod(p, n)

    while n > 0:
        print(f"cut[{n}] = {cut[n]}")
        # Remove the first piece
        n = n - cut[n]
    
    return r


if __name__ == "__main__":
    # Example 1
    ## Problem: Given a steal rod of length n, cut it into pieces to maximize the profit ..
    ## where profit for a piece of length i is given as price subscript i
    rod_length = [1, 2, 3, 4, 5]
    rod_price =  [1, 5, 8, 9, 10]
    n = 5

    print("Maximum Revenue in Example 1 is ", print_cut_rod_solution(rod_price, n))

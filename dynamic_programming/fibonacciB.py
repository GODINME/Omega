# Fibonacci Top Down with Memoization

def fib(n):
    # Initializing Memo called tabular
    tabular = [None] * n 
    tabular[0] = 1
    tabular[1] = 1

    for i in range(2, n):
        tabular[i] = 0

    return memo_fib(n, tabular)  


def memo_fib(n, tabular):
    if tabular[n - 1] > 0:
        return tabular[n - 1]
    
    # Save the result to avoid recomputation
    tabular[n-1] = memo_fib(n - 1, tabular) + memo_fib(n - 2, tabular)

    return tabular[n - 1]


# Example One
if __name__ == "__main__":
    print(f"Fibonacci of 5 is: {fib(5)}")
    print(f"Fibonacci of 10 is: {fib(10)}")
    print(f"Fibonacci of 15 is: {fib(15)}")
    print(f"Fibonacci of 20 is: {fib(20)}")
    print(f"Fibonacci of 25 is: {fib(25)}")
    print(f"Fibonacci of 30 is: {fib(30)}")
    print(f"Fibonacci of 35 is: {fib(35)}")
    print(f"Fibonacci of 40 is: {fib(40)}")
    print(f"Fibonacci of 45 is: {fib(45)}")
    print(f"Fibonacci of 50 is: {fib(50)}")
    
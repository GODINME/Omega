def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    m = [[0] * (n + 1) for _ in range(n + 1)]  # Initialize the M table
    s = [[0] * (n + 1) for _ in range(n + 1)]  # Initialize the S table

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parenthesization(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(s, i, s[i][j])
        print_optimal_parenthesization(s, s[i][j] + 1, j)
        print(")", end="")


# Example usage:
dimensions = [5, 10, 3, 12, 5, 50, 6]
m_table, s_table = matrix_chain_order(dimensions)

print("Optimal Parenthesization:")
print_optimal_parenthesization(s_table, 1, len(dimensions) - 1)
print("\nMinimum number of scalar multiplications:",
      m_table[1][len(dimensions) - 1])

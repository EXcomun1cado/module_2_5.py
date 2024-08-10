def get_matrix(n, m, v):
    matrix = []
    for _ in range(n):
        str_ = []
        for _ in range(m):
            str_.append(v)
        matrix.append(str_)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

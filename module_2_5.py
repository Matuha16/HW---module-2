def get_marix(n, m, value):
    matrix = []
    for i in range(2):
        matrix.append([])
        for o in range(m):
            matrix[i].append(value)
    return matrix

result1 = get_marix(2, 2, 10)
print(result1)

def get_marix(n, m, value):
    matrix = []
    for i in range(3):
        matrix.append([])
        for o in range(m):
            matrix[i].append(value)
    return matrix

result2 = get_marix(3, 5, 42)
print(result2)

def get_marix(n, m, value):
    matrix = []
    for i in range(2):
        matrix.append([])
        for o in range(m):
            matrix[i].append(value)
    return matrix

result3 = get_marix(4, 2, 13)
print(result3)
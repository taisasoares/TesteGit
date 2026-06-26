def quadrados(n):
    return [x**2 for x in range(1, n + 1)]

n = int(input())

print(quadrados(n))
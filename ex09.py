def primo(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def primosAte(n):
    return [p for p in range(1, n + 1) if primo(p)]

n = int(input())

print(primosAte(n))
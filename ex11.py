notas = [float(x) for x in input().split()]

quantidade = len([nota for nota in notas if nota > 5])

print(quantidade)
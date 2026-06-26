linhas, colunas = map(int, input("Digite o número de linhas e colunas (sem enter, separado por espaço): ").split())

matriz = []

for i in range(linhas):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)

pares = [numero for linha in matriz for numero in linha if numero % 2 == 0]

print(pares)
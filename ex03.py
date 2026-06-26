# Sem compreensão

def achatar(lista):
    resultado = []

    for elem in lista:
        if type(elem) == list:
            resultado += achatar(elem)
        else:
            resultado.append(elem)

    return resultado

lista = eval(input())

print(achatar(lista))

# Com compreensão
[1,2,[4,2],5,[2,[1,2,3],[[1]]],8]
def achatar(lista):
    return [
        x
        for elem in lista
        for x in (achatar(elem) if type(elem) == list else [elem])
    ]

lista = eval(input())

print(achatar(lista))
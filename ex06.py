def contaVogais(texto):
    return sum([1 for c in texto if c in "aeiouáàãâéêíóôõúAEIOUÁÀÃÂÉÊÍÓÔÕÚ"])

texto = input()

print(contaVogais(texto))
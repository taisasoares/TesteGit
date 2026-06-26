nomes = input().split()

maiores = [nome for nome in nomes if len(nome) > 5]

print(maiores)
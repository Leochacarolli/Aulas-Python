# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6 7
# L e o n a r d o
# -8-7-6-5-4-3-2-1

nome = 'Leonardo'
print(nome[2])
print(nome[-6])

print('o' in nome) # Se 'o' está entre a variável nome
print('Leo' in nome) # Se 'Leo' está entre a variável nome
print(10 * '-')
print('o' not in nome) # Se 'o' está entre a variável nome e o 'not' inverte o valor booleano
print('Leo' not in nome) # Se 'Leo' está entre a variável nome e o 'not' inverte o valor booleano

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
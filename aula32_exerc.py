'''
Faça um programa que peça ao usuario para digitar um número inteiro
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''

num_digitado = input("Digite um numero inteiro: ")

try:
    num_int = int(num_digitado)

    if num_int % 2 == 0:
        print(f'O número {num_int} é par')
    else:
        print(f'O número {num_int} é impar')
except:
    print('Isto não é um número inteiro')

'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. ex.
bom dia 0-11, boa tarde 12-17 e boa noite 18-23
'''

hora_digitada = input("Digite a hora atual em numero inteiro: ")

try:
    conversao = int(hora_digitada)

    if(conversao > 23):
        print('Hora inválida')
    else:
        if hora_digitada >= 0 and hora_digitada <= 11:
            print('Bom dia')
        if hora_digitada >= 12 and hora_digitada <= 17:
            print('Boa tarde')
        if hora_digitada >= 18 and hora_digitada <= 23:
            print('Boa noite')
except:
    print('Digite apenas números inteiros')

'''
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; Se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
'''

nome = input('Digite seu nome: ')

if len(nome) >= 1 and len(nome) <= 4:
    print('Seu nome é curto')
else:
    print('Digite pelo menos 1 letra')
    
if len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
if len(nome) > 6:
    print('Seu nome é muito grande')

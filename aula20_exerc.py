primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}')
else:
    print(f'{primeiro_valor} é menor que {segundo_valor}')
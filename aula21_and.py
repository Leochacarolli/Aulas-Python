# Operador logicos
# AND (e) / OR (ou) / NOT (não)
# Se qualquer valor for considerado falso, a expressão
# inteira será avaliada naquele valor.
# São considerados Falsy: 0, 0.0, '' False
# Também existe o tipo None que é usado para representar
# um não valor.

entrada = input('[E] Para entrar [S] Para sair: ')
senha = input('Digite sua senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha == senha_permitida:
    print('Entrou')
else:
    print('Saiu')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
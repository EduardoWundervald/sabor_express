# printando número pi arredondado
pi = 3.14159
# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é ímpar.')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

idade = int(input('Informe sua idade: '))

if idade <= 12:
    print('Criança')
elif idade >= 13 and idade <= 18:
    print('Adolescente')
else:
    print('Adulto')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

user1 = 123
password1 = 123

user = str(input('Informe o nome de usuário'))
password = str(input('Informe a senha'))

if user1 == user and password1 == password:
    print('Credenciais corretas')
else: 
    print('Credenciais incorretas')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.


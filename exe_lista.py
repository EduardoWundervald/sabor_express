# Como já vimos, programação é prática! Criamos mais uma lista de atividades (não obrigatórias) para você exercitar e reforçar ainda mais seu aprendizado e o conteúdo da vez são listas, blocos de repetição e try except. Bora praticar?

# Exercícios
# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

nums0 = [1,2,3,4,5,6,7,8,9,10]
names = ['Eduardo', 'Laura', 'Edimara', 'Daniel']
years = [2005, 2025]
print('---------------------------------------')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

nums = [1,2,3,4,5,6,7,8,9,10]
for numeros in nums:
    print(numeros)

print('---------------------------------------')
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

nums1 = [1,2,3,4,5,6,7,8,9,10]
soma = 0
for x in nums1:
    if(x%2!=0):
        print(x)
        soma = soma+x

print(soma)
print('---------------------------------------')
#OU \/
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for i in range(10, 0, -1):
    print(i)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

num_tabu = int(input('Informe o número: '))
for x in range (10):
    print(num_tabu, 'x', x+1, '=', (x+1)*num_tabu)

print('---------------------------------------')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

nums3 = [1,3,5,7,9]
soma = 0
try: 
    for x in nums3:
        soma = soma + x
    print(soma)
except Exception as e:
    print(f"Ocorreu um erro: {e}")


print('---------------------------------------')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
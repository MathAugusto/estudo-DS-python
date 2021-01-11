# funções simples
def simples():
    print("função simples")

simples()

# função simples
def soma(a):
    return a + 10

soma(2)

# Melhorando a função simples
def soma(a):
    result = a + 10
    print("Outcome")
    return result

soma(2)

# funções um pouco mais complexas
def salario(work_hours):
    return work_hours * 25

def bonus(work_hours):
    return salario(work_hours) + 50

# salario normal x salario com bonus (8h dia)
salario(8), bonus(8)

# IF ELIF ELSE
def prova(nota):
    if nota >= 7:
        print("Passou")
    elif nota < 7 and nota > 5:
        print("Recuperação")
    else:
        print("Reprovado")
    return nota

print(prova(4))
print(prova(6))
print(prova(8))

# Função com argumentos
def compras(item, desc, frete):
  total = item - desc + frete
  return total

# passando valor de item, desconto e frete, e obtendo o resultado
valor = compras(100,20,10)
valor

# Funções nativa
x = (2,4,-6,7,90,440)

# Valor míínimo
min(x)

# Valor máximo
max(x)

# soma de valores
sum(x)

# numero de itens na tuple
len(x)

# mostrar valor absoluto
neg = -99.988888
abs(neg)

# diminiur casas decimais e arredondar
round(neg,2)

# aredondamento

round(neg)

# potencia
pow(10,3)

# Métodos
lista = ["Ana", "Bia", "Caio"]

# Add elemento
lista.append('Davi')
lista

# Add outra lista (unir ambas)
lista.extend(['Edu', "Fabi"])
lista

print('Primeiro da lista: ' + lista[0] + " ultimo da lista: " + lista[-1] )

# Slicing
lista[2]

lista.index('Caio')

fora = ['Caio', 'Ana']
fora

# Ordena em ordem alfabética / numérico crescente
fora.sort()
fora

# Reversão do Sort()
fora.sort(reverse=True)
fora

# Split
(idade, numero_filhos) = "30,2".split(',')
print("idade: {}".format(idade))
print("numero de filhos: {}".format(numero_filhos))

# FOR
even = [0,2,5,6,8,11,12]

for n in even:
    z = n%2
    if z == 1:
        print("ímpares: {}".format(n))

# WHILE
# Multiplos de 3 até 20
val = 0
while val <= 20:
    print(val)
    val += 3

# RANGE
for s in range(10):
    print(2**s)

# Printar multiplos de 9
for cv in range(100):
    if cv%9 == 0:
        print(cv)

listas = [6,12,45,66,76]

# Contagem de multiplos de 6 na listas
def contagem(numeros):
    zerado = 0
    for zer in numeros:
        if zer%6 == 0:
            zerado += 1
    return zerado

contagem(listas)

# Iteraçao de dict
# valor = preço x quantidade
preco = {
    'arroz' : 30,
    'feijao' : 10
  }
quantidade = {
    'arroz' : 2,
    'feijao' : 3
  }
total_gasto = 0

for i in preco:
    total_gasto = total_gasto + (preco[i]*quantidade[i])
print(total_gasto)












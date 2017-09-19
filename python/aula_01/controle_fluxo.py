
# coding: utf-8

# # Controle de Fluxo
# 
# Nesse jupyter notebook, vamos visitar os comandos (instruções) de controle de fluxo em python. São eles:
# 
# - if..else
# - laços de repetição:
#  - for
#  - while
#  
#  
#  
# ## if...else
# 
# O comando *if* é útilizado quando queremos bifurcações nas decisões em nosso código, ou seja, quando queremos executar um trecho do código apenas se uma determinada condição for satisfeita.
# 
# Vamos escrever um código que imprime na tela se um dado número é positivo ou não.

# In[1]:


num = 3
if num >= 0:
    print(num, "é positivo!")
# é sempre impresso
print(num, "é negativo!")


# No exemplo, acima queríamo imprimir na tela se o número é positivo ou não, porém é sempre impresso que o número negativo.
# 
# Daí temos a expressão ```else```, que significa: *caso a condição anterior [da cláusula ```if```] não seja satisfeita execute o comando*. Rescrevendo o código acima:

# num = 3
# if num >= 0:
#     print(num, "é positivo!")
# else:
#     print(num, "é negativo!")
#     
# num = -1
# if num >= 0:
#     print(num, "é positivo!")
# else:
#     print(num, "é negativo!")

# Caso quiséssemos que o ```else``` fosse executado apenas para condições especificas? Para isso existe o comando ```elif``` (em outras linguagens *else if*). Com ele conseguimos especificar varias outras condições. Voltando ao exemplo anterior, suponhamos que além de saber se um número é positivo e negativo, queremos também saber se ele é zero.

# In[6]:


num = 3.4
if num > 0:
    print(num, "é positivo!")
elif num < 0:
    print(num, "é negativo!")
else:
    print(num, "é zero!")


# Podemos adicionar quantas cláusualas ```elif``` quisermos, porém elas devem ser precedidas pela cláusula ```if```.
# 
# ### Exercícios
# 
# Para exercitar um pouco a sintaxe do python e o que foi passado, peço para que você faça os seguintes exercícios:
# 
# #### Exercício 1
# 
# Escreva uma código que verifique se um número é par ou ímpar.

# In[10]:


# escreva seu código aqui


# #### Exercício 2
# 
# Escreva uma código que imprima o maior entre 3 números.

# In[9]:


a = 1
b = 20
c = -10

# escreva seu código aqui

# sáida esperada: 20


# ## Laços de Repetição
# 
# Laços são comandos com os quais podemos executar um bloco de código mais de uma vez. Geralmente, é utilizado para iterar sobre uma sequência (i.e., lista, tupla, string).
# 
# ### Comando for
# 
# A sintaxe do comando for é basicamente o descrito abaixo:
# 
# ```python
# for val in sequencia:
#     # trecho de código
# ```
# 
# ```val``` corresponde a valor corrente da sequência que está sendo avaliado. O laço itera sobre todos os valores da sequência até que seu último item.
# 
# #### Range
# 
# O laço for em python é um distinto dos comandos visto em outra linguagens. Aqui, precisamos de uma sequência para que possamos executar o laço, para isso o python no fornece a função ```range```. Abaixo descrevo a sintaxe e exemplos de uso dessa função.
# 
# ```python
# # cria uma sequência de 0 até fim - 1
# range(fim)
# 
# # cria uma sequência de inicio até fim - 1
# range(inicio, fim)
# 
# # cria uma sequência de inicio até fim - 1 incrementando passos
# range(inicio, fim, passos)
# ```

# In[14]:


print(list(range(9)))

print(list(range(2, 9)))

print(list(range(0, 9, 3)))


# Vamos então ver um exemplo do laço for

# In[4]:


soma = 0
n = 10
for val in range(1, n):
    soma += val
soma

print("%d = %d" % (soma, (n * (n - 1)) // 2))


# ### Comando while
# 
# O laço while é utilizado para iterar sobre um bloco de código até que uma condição de parada seja alcançada, como mostrado no exemplo de sintacxe a seguir:
# 
# ```python
# while condicao:
#     # trecho de código
# ```
# 
# No laço while, a condição é verificado antes. O corpo do while é executado se e somente se a condição for verdadeira.
# 
# Em python, a corpo do while é determindado pela identação.
# 
# Em python, qualquer valor diferente de zero é interpretado como ```True```. None e 0 são interpredatos como ```False```.
# 
# Vamos reescrever o exemplo anterior para utilizarmos o comando while.

# In[3]:


soma = 0
n = 10
i = 1
while i < n:
    soma += i
    i += 1

print("%d = %d" % (soma, (n * (n - 1)) // 2))


# Na trecho de código acima, a condição ```ì < n``` será verdadeira até que i seja menor que n (9 no nosso caso).
# 
# A cada iteração, o valor de i é incrementado em uma unidade. Isso é muito importante (causa de muitos bugs), pois esquecendo disso pode-se causar loop infinito (laço nunca para de iterar).
# 
# ### Exercícios
# 
# Para exercitar um pouco a sintaxe do python e o que foi passado, peço para que você faça os seguintes exercícios:
# 
# #### Exercício 3
# 
# Escreva um código para calcular e imprimr o n-ésimo termo da sequência [Fibonacci](https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci) utilizando ambos os laços while e for. A sequência fibonacci é uma sequência de números inteiros, que inicia com 0 e 1 e os restantes dos termos é definida pela soma dos dois anteriores a ele, ou seja, $F_n = F_{n-1} + F_{n-2}$.
# 
# Segue o exemplo dos 10 primeiros termos da sequência:
# 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# In[39]:


import math

n = input()
F1 = 0
F2 = 1
for i in range(2, n):
    temp = F1 + F2
    F1 = F2
    F2 = temp
    
if n <= 0:
    print(0)
elif n == 1:
    print(1)
else:
    print(F1 + F2)


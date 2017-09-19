
# coding: utf-8

# # Estrutura de Dados
# 
# Python oferece uma grande quantidade de estrutura de dados tais como listas (list), dicionários (dict), tuplas (tuple) e conjuntos (set).
# 
# ## Listas
# 
# Listas são estruturas de dados para armazenar mais de um valor, geralmente denotados como sequências.
# 
# Em python um lista é criada colocando todos elementos entre colchetes, como nos exemplos abaixo.

# In[1]:


# lista vazia
lista = []

# lista de inteiros
lista = [1, 2, 3]

# lista com diferentes tipos de dados
lista = [1, "Hello", 3.4]

# lista aninhada
lista = ["mouse", [8, 4, 6], ['a']]


# Note que listas em python podem conter tipos de dados distintos. Além disso, é possível armazenar lista dentro de lista (como no último exemplo).
# 
# ### Acessando elementos
# 
# Em python, há várias formas distintas para se acessar elementos em uma lista. Podemos acessar os elementos individualmente utilizando colchetes e seu endereço:

# In[2]:


s = ["p", "y", "t", "h", "o", "n"]

# acessando o primeiro elemento
print(s[0])

# acessando o último elemento
print(s[-1])


# Diferentemente de muitas linguagens de programção, python aceita indice negativo. Quando utilizamos indices negativo é como estivéssemos acessando a lista de tras para frente, onde -1 é o último elemento da lista (como no exemplo).
# 
# #### Slicing
# 
# Python nos permite acessar um subconjunto da lista facilmente com o operador de slicing (:), como mostrado adiante:

# In[3]:


# imprime a lista sem o 
# primeiro e último elementos
print(s[1:-1])

# imprime a lista sem a última letra
print(s[:-1])

# imprime a lista sem a primeira letra
print(s[1:])


# ### Alterando valores
# 
# Para se alterar algum valor, é apenas preciso atribuir um novo valor ao elemento que queremos alterar utilizando as formas de acesso expostas anteriormente.

# In[4]:


s = ["p", "y", "t", "h", "o", "n"]

s[0] = "P"

print(s)

s[1:] = [v.upper() for v in s[1:]]

print(s)


# Em python, podemos alterar mais de um elemento ao mesmo tempo utilizando o slicing.  No código acima utilizei algo um pouco estranho para isso. Portanto, vou explicar um pouco melhor como funciona o trecho a seguir:
# 
# ```python
# s[1:] = [v.upper() for v in s[1:]]
# ```
# 
# O trecho ```[v.upper() for v in s[1:]]``` é uma outra modo de criar uma lista. Nós estamos criando uma lista a partir do *slice* da lista ```s```, onde cada elemente do *slice* é transformado em uma letra maiúscula. É uma forma muito sucinfa e elegante de se criar uma lista (uso muito).
# 
# Podemos também criar uma lista levando alguma condição em consideração. Por exemplo, vamos supor que queriamos criar uma lista de elementos impares:

# In[5]:


[i for i in range(10) if i % 2]


# ## Adicionando elementos

# In[6]:


s = ["p", "y", "t", "h", "o", "n"]

# Adicionando um elemento ao final
s.append("3")
print(s)

# Concatenando duas listas
print(s + [".", "5"])


# Com esse novo conhecimento, nós temos 3 modos de criar um novo array a partir de outro. Eles estão descrito abaixo.
# O modo 1 não é só o mais elegante e sucinto, mas também o mais rápido e quando estamos desenvolvendo para muita quantidade de dados é importante saber qual é o modo mais rápido. Veja o custo de cada modo abaixo:

# In[7]:


def create_list1(n):
    return [i for i in range(n)]
    
def create_list2(n):
    l = []
    for i in range(n):
        l.append(i)
    return l

def create_list3(n):
    l = []
    for i in range(n):
        l += [i]
    return l

get_ipython().magic(u'timeit create_list1(10000000)')
get_ipython().magic(u'timeit create_list2(10000000)')
get_ipython().magic(u'timeit create_list3(10000000)')


# ### Removendo elementos

# In[8]:


s = ["p", "y", "t", "h", "o", "n"]

# saída: ['p', 'y', 'h', 'o', 'n']
s.pop(2)
print(s)

# saída: ['p', 'y', 'h', 'o']
s.remove("n")
print(s)

# saída: ['p', 'y']
s[2:] = []
print(s)


# ### Verificando a existencia de um elemento
# 
# Para se verificar a existência de um elemento em uma lista utiliza-se o comando ```in```.

# In[9]:


s = ["p", "y", "t", "h", "o", "n"]

# verificando se um elemento encontra-se na lista
print("y" in s, "r" in s)


# ## Exercício
# 
# #### Exercício 1
# 
# Faça um código que dado duas lista, do mesmo tamanho, transforme-as crie uma nova lista (com memso tamanho das anteriores) onde cada um dos elementos seja a soma dos elemento das anteriores. Por exemplo, lista1 = [1, 2, 4], lista2 = [1, 3, 9] e result = [2, 5, 13]

# In[10]:


# código aqui...


# ## Tuplas
# 
# Tuplas são similares a lista, porém elas imutaveis, ou seja, uma vez criadas não é possível mais alterar seus valores.
# 
# Em python, uma tupla é criada colocando todos elementos entre parênteses, como nos exemplos abaixo.

# In[11]:


# tupla vazia
tupla = ()

# tupla de inteiros
tupla = (1, 2, 3)

# tupla com diferentes tipos de dados
tupla = (1, "Ola", 3.4)

# tupla aninhada
tupla = ("mouse", (8, 4, 6), ['a'])


# ## Dicionários
# 
# É uma coleção não ordenada de elementos. Diferentemente das outras estruturas de dados, dicionários (dict) são compostos por parordenados (chave:valor).
# 
# Essas estruturas são otimizadas para recuperação de valores quando sabemos as chaves.

# In[12]:


# dicionário vazio
dicionario = {}

# dicionário normal
dicionario = {'c': -1, 'o': 10}

# dicionário com chaves e
# valores de tipos distintos
dicionario ={'c': -1, ("c", "c"): 10}


# ### Acessando elementos

# In[13]:


dicionario = {'nome':'Raphael', 'idade': 27}

# Saída: Raphael
print(dicionario['nome'])

# saída: 27
print(dicionario.get('idade'))


# Tentar acessar um chave que não existe lançar um erro
# dicionario['cidade']
# O método get contorna isso
dicionario.get('cidade')


# ### Alterando elementos

# In[14]:


dicionario = {'nome':'Raphael', 'idade': 27}

# Alterando valor
dicionario['idade'] = 30

# saída: {'idade': 30, 'nome': 'Raphael'}
print(dicionario)

# Inserindo um novo valor
dicionario['cidade'] = 'Belo Horizonte'

# saída: {'idade': 30, 
#    'cidade': 'Belo Horizonte',
#    'nome': 'Raphael'}
print(dicionario)


# ### Criando dicionários elegantemente

# In[15]:


quadrados = {x:x*x for x in range(10)}
print("dois ao quadrado é"),(quadrados[2])


# In[16]:


quadrados_impares = {x: x*x for x in range(10) if x%2 == 1}
quadrados_impares


# ## Conjuntos
# 
# É uma coleção não ordenada de elementos. Cada elemento é único (não duplicado) e tem de ser imutável (i.e., não é possível ter conjuntos de listas). Todavia, os conjuntos são mutáveis. [DOC](https://docs.python.org/2/library/sets.html)

# In[17]:


# conjunto vazio
conjunto = set()
print(conjunto)

# conjunto de inteiros
conjunto = {1, 2, 3}
print(conjunto)

# conjunto de dados distintos
conjunto = {"mouse", (8, 4, 6)}
print(conjunto)

# a partir de um outro iterável
conjunto = set([1, 2, 4, 5, 5, 5, 2, 4])
print(conjunto)


# ### Operações de Conjunto
# 
# É possível executar operações de conjuntos tais como união, diferença, interseção. A sintaxe é mostrada abaixo.

# In[18]:


A = {1,2,3}
B = {3,4,5,6}

# união
print("Uniao:"), (A | B, A.union(B))

# interseção
print("Intersecao"), (A & B, A.intersection(B))

# diferença
print("Dif.:"), (A - B, A.difference(B))
print("Dif.:"), (B - A, B.difference(A))

# diferença simétrica
print("Dif. simetrica:"), (A ^ B, A.symmetric_difference(B))

print("É disjunto?"),(A.isdisjoint(B))


# ### Conjuntos Imutáveis
# 
# Como mencionado, set é mutável, portanto, não é possível usá-los como chaves em dicionários. Uma forma de contornar isso é utilizando o frozenset. Basicamente, o frozenset está para o set como a tupla está para lista.
# 
# Portanto, frozenset suporta todas operações de set (exceto as que alteram seus valores, tais como update, add, remove, pop and discard).

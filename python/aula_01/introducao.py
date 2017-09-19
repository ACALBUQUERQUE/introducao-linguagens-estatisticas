
# coding: utf-8

# ## Indentificadores
# 
# * Identificadores podem ser uma combinação de letras maiúscula (A - Z) ou minúsculas (a - z) ou digitos (0 a 9) ou underscore (\_). Exemplos validos são: variable1, meuContatodor, dia\_da\_semana\_.
# 
# * Um identificador não pode começar com dígitos. No campo abaixo crie um identificador iniciando com digito, aperte crtl + enter e veja o que ocorre.

# In[1]:


1variavel


# * Palavras-chave não podem ser usadas como identificadores.

# In[2]:


for = 1


# * Caracteres especiais, como !, @, \$,% etc, não são permitidos no identificador.

# In[3]:


var!


# * Podem ser de qualquer tamanho
# 
# Brique um pouco com os identificadores.

# ## Considerações Importantes
# 
# * Python é **case-sensitive**
# * Sempre crie identificadores com nomes que façam sentido
# 
# 
# ## Instruções
# 
# Em python, o fim de uma instrução é marcada por um caracter de quebra de linha (i.e., \n). Porém, uma instrução pode ser estendida a multiplas linhas com o caracter (\). Por exemplo:

# In[4]:


a = 9 + 8 + 7 +     6 + 5 + 4 +     3 + 2 + 1
a


# Também é possível estender as linhas de um comando quando o caracter de quebra de linha está enclausurado por parenteses, chaves ou colchetes.

# In[5]:


a = (9 + 8 + 7 +
    6 + 5 + 4 +
    3 + 2 + 1)
a


# Também é possível colocar mais de uma instrução em uma mesma linha usando ponto e vírgula como separador.

# In[6]:


a = 1; b = 2; c = 3


# ## Indentação
# 
# Em python, indentação é obrigatória para definir blocos de código. Forçando o programador a boa prática de indentar, por consequência deixando o código mais legível:
# 
# O trecho de código abaixo precisa ser identado para que funcione. Favor, consertá-lo e executá-lo:

# In[7]:


if True:
print("Indentado!!!")


# ## Comentários
# 
# Comentários são muito importantes enquanto escrevemos programas. Descrevem o que está acontecendo no programa de modo que fique fácil o entendimento do código por um terceiro. Além disso, te ajuda a relembrar o funciomento do algoritmo que você escreveu há um bom tempo.
# 
# Em python, nós utilizamos o simbolo cerquilha (a.k.a., jogo da velhar, sustenido, #) para demarcar a linha como sendo um comentário, vide o exemplo:

# In[ ]:


# Isso é um comentário de uma linha
print("Oi")


# Todo comentário é ignorado pelo interpretador do python. Comentar seu código é uma boa prática de programação.
# 
# Podemos também comentar mais de uma linha por vez, como nos exemplos a seguir.
# 
# ### Comentários em mais de uma linha

# In[ ]:


# Isso é um comentário
# mais longo que o
# anterior


"""Isso é um comentário
mais longo que o
anterior"""


# # Variáveis e Tipos de Dados
# 
# ## Variáveis
# 
# Uma variável é espaço de memória usado para armazenar algum dado (valor).
# 
# Os nomes de variáveis seguem o mesmo padrão dos identificadores.
# 
# Como python é uma liguagem de tipagem dinamica, não é preciso declara a variavel antes de usá-la, nem mesmo seu tipo. É claro que é preciso atribuir um valor para variável antes!
# 
# ### Atribuíção de valor

# In[ ]:


a = 10
b = 0.5
c = "Legal!"


# Temos três atribuições distintas, sendo que cada uma das variáveis vão ter um tipo diferente. Por exemplo, *a* será um inteiro, *b* floating e *c* uma *string* (sequência de caracteres).
# 
# #### Multiplas atribuições

# In[ ]:


a, b, c = 10,  0.5, "Legal!"

a = b = c = "Mesmo Valor"


# ## Tipos
# 
# ### Numerais
# 
# Python suporta inteiros, ponto flutuante e números complexos. Eles são definidos como ```int```, ```float``` e ```complex``` em Python.
# 
# Nós podemos verificar a qual classe um valor pertence utilizando ```type``` ou então com o ```isinstance```. Veja o exemplo a seguir:

# In[ ]:


valor = 5
print(type(valor), isinstance(valor, int))

valor = 5555555555555555555555555555555555555555555
print(type(valor), isinstance(valor, long))

valor = 5.0
print(type(valor), isinstance(valor, float))

valor  = 5.0 + 4j
print(type(5.0 + 4j), isinstance(valor, float))


# Podemos converter valores para outros tipos. Por exemplo:

# In[ ]:


valor = 5
print(type(valor), type(float(valor)), type(long(valor)))


# In[ ]:


valor = 5555555555555555555555555555555555555555555555555555555555555
print(type(valor), type(float(valor)), type(int(valor)))


# Note que acima não conseguimos forçar o tipo desse inteiro enorme a ser int. Algumas conversões não são possíveis!

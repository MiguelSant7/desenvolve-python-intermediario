#### Recursividade

## Func para encontrar o fatorial de determinado número definido 
def fatorial(n): # Recebe 'n' que é o numero definido
    print(f"{n}! = ", end='')

    if (n == 0): # Comparação, caso n seja igual a 0, vai retornar 1
        print('1') # Caso Base
        return 1 # Retorna 1 pois o fatorial de 0 é 1

    else: 
        print(f"{n} * {n-1}!") 
        return n * fatorial(n-1) # Caso o if nao seja satisfeito, retorna o fatorial atualizado - 1, até que chegue até 0 
    

# print(f"O fatorial de {4} é: {fatorial(4)}")


##### 1) Faça um procedimento recursivo que receba dois valores inteiros a e b e
# imprime o intervalo fechado entre eles. Se a > b imprima uma mensagem de
# erro.

# Entrada    Saída
# 1 10       1 2 3 4 5 6 7 8 9 10
# -5 1       -5 -4 -3 -2 -1
# 5 -5       Valores invalidos
# 17 20      17 18 19 20

def recursividade(a, b): # Função definida para realizar recursividade
   # Caso 'a' seja maior que 'b', indica erro.
    if a > b: 
        print("Error") 
    else:
        # Caso 'a' seja igual a 'b', imprima 'a' já que nesse estado a tem o mesmo valor que 'b'
        if a == b: 
            print(b) # {Pode ser substituido por 'a'}
        
        else: 
            print(b, end=' ') # Imprime o atual valor de 'a' com espaço no final
            recursividade(a, b - 1) # Aumenta o valor de 'a'

# # Entrada do usuario
# a = int(input("Digite um valor: "))
# b = int(input("Digite um valor: "))

# # Chamando função
# recursividade(a, b)



#### 2) Mudando apenas uma linha, altere o código anterior para imprimir o intervalo
# invertido.

# Entrada      Saída
# 1 10         10 9 8 7 6 5 4 3 2 1
# -5 1         -1 -2 -3 -4 -5
# 5 -5         Valores invalidos
# 17 20        20 19 18 17

def recursividade(a, b): # Função definida para realizar recursividade
   # Caso 'a' seja maior que 'b', indica erro.
    if a > b: 
        print("Error") 
    else:
        # Caso 'a' seja igual a 'b', imprima 'a' já que nesse estado a tem o mesmo valor que 'b'
        if a == b: 
            print(b) # {Pode ser substituido por 'a'}
        
        else: 
            print(b, end=' ') # Imprime o atual valor de 'a' com espaço no final
            recursividade(a, b - 1) # Aumenta o valor de 'a'

# Entrada do usuario
# a = int(input("Digite um valor: "))
# b = int(input("Digite um valor: "))

# Chamando função
# recursividade(a, b)



# 3) Escreva uma função recursiva que recebe um inteiro n > 1 e calcula a soma
# dos valores entre n e 1.

# Entrada      Saída
# 5            15
# 13           78

# Função para retornar a soma dos inteiros
def inteiro(n): # Recebe "n" como parametro
   
   # Se "n" for menor que 1, o resultado é 0
    if n < 1:
        print("Erro")
        return 0
    # Se o if nao for atendido...
    else:
        # Se "n" igual a 1, retorne um já que nada foi somado
        if n == 1:
            return 1
        # Retorna n + função(n - 1(contagem))
        else: 
            return n + inteiro(n - 1)

# # Entrada
# n = int(input("Informe um valor: "))
# resultado = inteiro(n)
# # Resultado
# print(f"O valor da soma recursiva de {n} é: {resultado}")
    


# 4) Escreva uma função recursiva que recebe um inteiro n e verifica se n é um
# valor primo, ou seja, se é divisível apenas por si mesmo e por 1.


# Função para verificar se o número é primo ou nao 
def verifica_primos(n, divisor=None):
    if n < 2: # Não tem número primo menor que 2
        return False
    if n == 2: # O número 2 é o único número positivo
        return True
    if  n % divisor == 0: # Caso o resto da divisão de n pelo divisor seja 0... False
        return False
    if divisor * divisor > n: # Se o divisor vezes o divisor é maior que n... True
        return True
    
    # Retorno
    return n + verifica_primos(n, divisor + 1)


# # Entrada/Saída
# numero = int(input("Digite um número: "))
# if verifica_primos(numero):
#     print(f"{numero} é um número primo.")
# else:
#     print(f"{numero} não é um número primo.")





# 5) Implemente uma função recursiva que recebe um número inteiro decimal e
# retorna sua representação binária como uma string. Para realizar essa
# conversão, utilize o método de divisão sucessiva, onde você divide o número
# decimal por 2 e coleta os restos até que o quociente seja zero. A ordem dos
# restos coletados, de baixo para cima, forma o número binário
# correspondente.

# Exemplo de Conversão:
# Para converter o número decimal 13 para binário:
# 13 ÷ 2 = 6, resto 1
# 6 ÷ 2 = 3, resto 0
# 3 ÷ 2 = 1, resto 1
# 1 ÷ 2 = 0, resto 1
# Lendo os restos de baixo para cima, obtemos o número binário 1101.

# Função binarios
def binarios(inteiro):    

    if inteiro == 0:
        return ''
    resto = inteiro % 2 # Armazenando o resto

    print(f"{inteiro} ÷ 2 = {resto}") # Imprime com formatação
    return binarios(inteiro // 2) + str(resto)
        
# # Entrada
# numero = int(input("Informe um número: "))
# if numero == 0:
#     print("0")
# else:
#     print(f"O número {numero} em binário é: {binarios(numero)}")




# 6) Extra: Implemente uma função recursiva em Python que realiza a travessia
# em pré-ordem de uma árvore binária representada por listas aninhadas. Na
# travessia em pré-ordem (ou pré-fixada), o nó raiz é visitado primeiro, seguido
# pela subárvore esquerda e, por fim, pela subárvore direita. A questão fixa as
# constantes RAIZ_IDX, ESQ_IDX, DIR_IDX representando os índices da lista
# onde se encontra o valor raíz, o nó a esquerda e o nó a direita.
# Representação visual da árvore
# 4
# / \
# 2 5
# / \
# 1 3

# Definindo as constantes para os índices
RAIZ_IDX = 0
ESQ_IDX = 1
DIR_IDX = 2

# Função recursiva 
def pre_ordem(arvore):
    if arvore is not None:
        
        print(arvore[RAIZ_IDX], end=' ') # Imprime a raiz (pré-ordem: primeiro visita o nó raiz)
        
        if arvore[ESQ_IDX] is not None: # Visita a subárvore esquerda
            pre_ordem(arvore[ESQ_IDX])
        
        
        if arvore[DIR_IDX] is not None: # Visita a subárvore direita
            pre_ordem(arvore[DIR_IDX])

# Árvore binária representada por listas aninhadas
arvore = [
    4,              
    [               
        2,          
        [1, None, None],  
        [3, None, None]   
    ],
    [               
        5,          
        None,       
        None        
    ]
]

# Testando a função
print("Travessia em pré-ordem:")
pre_ordem(arvore)

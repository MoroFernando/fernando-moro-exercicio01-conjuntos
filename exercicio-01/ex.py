# Fernando Moro

''' ENUNCIADO 
Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a 
linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de 
operações que serão realizadas entre dois conjuntos de dados.  
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) 
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas 
em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas 
segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de 
operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas 
seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da 
operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e 
terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo 
das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver: 
4 
U 
3, 5, 67, 7 
1, 2, 3, 4  
I 
1, 2, 3, 4, 5 
4, 5 
D 
1, A, C, 34 
A, C, D, 23 
C 
3, 4, 5, 5, A, B, R 
1, B, C, D, 1 
Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um 
produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑,𝟓,𝟔𝟕,𝟕} e 
{𝟏,𝟐,𝟑,𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).  
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados 
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter 
a informação e a formatação mostrada a seguir:    
União: conjunto 1 {3,5,67,7}, conjunto 2 {1,2,3,4}. Resultado: {3,5,67,7,1,2,4}   
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer 
um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo 
de  textos  de  entrada  formatada  segundo  o  exemplo  de  saída  acima.  Observe  as  letras  maiúsculas  e 
minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.  
No  caso  do  texto  de  exemplo,  teremos  4  linhas,  e  apenas  4  linhas  de  saída,  formatadas  e 
pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação, 
implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento. 
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada 
contendo um número diferente de operações, operações com dados diferentes, e operações em ordem diferentes.  Os  arquivos  de  entrada  criados  para  os  seus  testes  devem  estar  disponíveis  tanto  no 
ambiente repl.it quanto no ambiente Github.  
Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com, 
no mínimo um arquivo de testes criado pelo próprio professor.  '''

def formatação_da_lista(conjunto:list):
    conj = []
    num = 0
    num_str = str(num) # Var para poder concatenar os números maiores que uma casa decimal

    for elemento in conjunto:

        if elemento.isnumeric():
            num_str += str(elemento)
            num = int(num_str)

        elif elemento.isalpha():
            conj.append(elemento) 
            num = None

        elif elemento == "," and num != None:
            conj.append(num) 
            num = 0
            num_str = str(num)
  
    # Como a condição de fazer o append dos números era chegar na vírgula, foi preciso criar uma forma de fazer o append do ultimo elemento do conjunto caso seja numérico.
    if elemento.isnumeric():
        conj.append(num)

    return conj

def uniao (conj_x:list, conj_y:list):
    conj_resposta = conj_x

    for elemento in conj_y:
        if elemento not in conj_x:
            conj_resposta.append(elemento)
    
    return conj_resposta

def intersecao (conj_x,conj_y):
    conj_resposta = []

    for elemento in conj_y:
        if elemento in conj_x:
            conj_resposta.append(elemento)

    return conj_resposta

def diferenca (conj_x,conj_y):
    conj_resposta = []

    for elemento in conj_x:
        if elemento not in conj_y:
            conj_resposta.append(elemento)

    for elemento in conj_y:
        if elemento not in conj_x:
            conj_resposta.append(elemento)

    return conj_resposta

def produto_cartesiano (conj_x,conj_y):
    conj_resposta = []

    for elemento_x in conj_x:
        for elemento_y in conj_y:
            p_cartesiano = (f"({str(elemento_x)},{str(elemento_y)})")
            conj_resposta.append(p_cartesiano)

    return conj_resposta

with open("operacoes.txt","r") as arquivo:

    entrada_txt = arquivo.read().splitlines()
    numero_de_operacoes = entrada_txt[0]

    contador_linha = 0
    for linha in entrada_txt:

        if contador_linha == 1:
            tipo_operacao = linha

        elif contador_linha == 2:
            conj1_resposta = formatação_da_lista(linha)
            conj1 = formatação_da_lista(linha)

        elif contador_linha == 3:
            conj2 = formatação_da_lista(linha)

            if tipo_operacao == "U":
                tipo_operacao = "União"
                conj_resposta = uniao(conj1,conj2)
                
            elif tipo_operacao == "I":
                tipo_operacao = "Interseção"
                conj_resposta = intersecao(conj1,conj2)

            elif tipo_operacao == "D":
                tipo_operacao = "Diferença"
                conj_resposta = diferenca(conj1,conj2)
            
            elif tipo_operacao == "C":
                tipo_operacao = "Produto Cartesiano"
                conj_resposta = produto_cartesiano(conj1,conj2)

            print(f"\n{tipo_operacao}: conjunto 1 {(conj1_resposta)}, conjunto 2 {(conj2)}. Resultado: {(conj_resposta)}")
            contador_linha = 0

        contador_linha += 1

    print(" ")

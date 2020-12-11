'''
1) Na engenharia de recursos hídricos, a estimativa dos tamanhos dos reservatórios depende de
estimativas precisas do escoamento da água no rio que está sendo confinado. Em alguns rios,
registros históricos de longa duração de tais dados de escoamento são difíceis de obter. Já os dados
meteorológicos sobre precipitação estão disponíveis para muitos anos do passado. Portanto, é útil
determinar a relação entre o escoamento e precipitação. Essa relação pode ser usada para fazer uma
estimativa do escoamento nos anos nos quais apenas medidas de precipitação foram feitas. Os
seguintes dados estão disponíveis para um rio que deve ser estancado:

Precipitação (cm/ano)   88,9    108,5  104,1   139,7    127     94      116,8   99,1
Escoamento (m3/ano)     14,6    16,7   15,3    23,2     19,5    16,1    18,1    16,6

a) A partir dos dados tabelados, ajuste uma reta a estes dados usando regressão linear pelo método
dos Mínimos Quadrados.
b) Determine o coeficiente de correlação para mostrar a qualidade do ajuste
c) A partir da equação da reta encontrada, determine o escoamento anual de água se a precipitação
for de 120cm.

A precipitação é a variável independente.

'''
from math import sqrt

def gauss_seidel(x_inicial, matriz, erro):

    n = len(matriz)

    x_temp = []
    for x in range(n):
        x_temp.append(-1)

    # verifica se o número de incógnitas do chute inicial é o mesmo do número de equações
    if len(x_inicial) != n:
        print("O número de incógnitas deve ser igual ao número de equações, entre com a quantidade correta de chutes iniciais.")
        return x_temp
        
    # verifica se a diagonal principal é nula
    for i in range(n):
        if matriz[i][i] == 0:
            print("A diagonal principal não pode conter zeros.")
            return x_temp

    n = len(matriz)
    x_temp = x_inicial.copy()      # i
    x_result = x_temp.copy()       # i+1
    cont = 0
    while True:
        for l in range(n):
            soma = 0
            soma += matriz[l][n]
            for c in range(n):
                # se não estiver na coluna da diagonal principal
                if c != l:
                    soma -= matriz[l][c]*x_result[c]
            x_result[l] = soma/matriz[l][l]
        
        # verifica a condição de parada para a solução encontra até então

        terminou = True
        for i in range(n):
            _erro = abs((x_result[i] - x_temp[i])/x_result[i])
            if _erro > erro:
                terminou = False
        cont += 1
        if terminou:
            break
        x_temp = x_result.copy()
    print("Número de iterações:", cont)
    return x_result

def minimos_quadrados(valores_x, valores_y):

  # calculo do ajuste
  somatorio_xi2 = 0
  somatorio_xi = 0

  somatorio_xy = 0
  indice_y = 0
  somatorio_y = 0
  
  for v in valores_x:
    somatorio_xi2 += v**2
    somatorio_xi += v

    somatorio_xy += v*valores_y[indice_y]
    somatorio_y += valores_y[indice_y]
    indice_y += 1

  n = indice_y

  linha1 = [somatorio_xi2, somatorio_xi, somatorio_xy]
  linha2 = [somatorio_xi, n, somatorio_y]

  m = [linha1, linha2]
  x_inicial = [0,0]

  r = gauss_seidel(x_inicial, m, 10**-5)

  a = r[0]
  b = r[1]

  # calculo do coeficiente de correlação (qualidade do ajuste)
  # quanto mais próximo de 1 melhor

  Sr = 0
  media = 0

  for i in range(len(valores_x)):
    Sr += (valores_y[i] - b - a*valores_x[i])**2
    media += valores_y[i]

  media = media/len(valores_y)
  St = 0

  for i in range(len(valores_y)):
    St += (valores_y[i] - media)**2

  R = sqrt((St - Sr)/St)

#   print("R =", R)
#   print("R^2 =", R**2)

  return a, b, R

eq1 = [88.9, 108.5, 104.1, 139.7, 127, 94, 116.8, 99.1]
eq2 = [14.6, 16.7, 15.3, 23.2, 19.5, 16.1, 18.1, 16.6]
a, b, R = minimos_quadrados(eq1, eq2)
print("Letra A:")
print("Equação da reta: y =", a, "*x +", b)
print("\nLetra B:")
print("Coeficiente de correlação: R =", R, "- R^2 =", R**2)
print("\nLetra C:")
print("O escoamento para uma precipitação de 120cm seria:", a*120 + b)

# Podemos observar que o ajuste foi bom, por ser acima de 0.94. 
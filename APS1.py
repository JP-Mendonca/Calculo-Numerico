# gauss seidel

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
            # parte que eu adaptei para o problema, podemos considerar válido pois 0 dividido por qualquer número é 0
            # e também, pelo sistema estar bem condicionado isso não influencia no resultado, até atender o critério
            # algum dos números no x_result será diferente de 0 obrigatoriamente para servir de parâmetro para o erro
            if x_result[i] == 0 and x_temp[i] == 0:
                _erro = 0
            else:
                _erro = abs((x_result[i] - x_temp[i])/x_result[i])
            if _erro > erro:
                terminou = False
        cont += 1
        if terminou:
            break
        x_temp = x_result.copy()
    print("Número de iterações:", cont)
    return x_result

'''
O sistema de equações utilizadas na forma de matriz foi:
    _________________________________________
   | i12 | i32 | i43 | i52 | i54 | i65 |total|
   -------------------------------------------
   |  5  |  0  |  0  | -2  |  0  |  0  | 40  |
   |  0  | -3  |  0  |  1  |  0  |  0  |  0  |
   |  0  |  0  | -3  |  1  |  0  |  0  |  0  |
   |  0  |  0  |  0  |-4/3 |  0  |  1  |  0  |
   |  0  |  0  |  0  |  1  | -3  |  0  |  0  |
   |  1  |  0  |  0  | -2  |  0  | -4  | 40  |
    -----------------------------------------
'''

matriz = [[5, 0, 0, -2, 0, 0, 40], [0, -3, 0, 1, 0, 0, 0], [0, 0, -3, 1, 0, 0, 0], [0, 0, 0, -4/3, 0, 1, 0], [0, 0, 0, 1, -3, 0, 0], [1, 0, 0, -2, 0, -4, 40]]

x_inicial = []
for i in range(len(matriz)):
  x_inicial.append(0)

print("Método de gauss-seidel:")
result = gauss_seidel(x_inicial,matriz, 10**-15)
print(result)

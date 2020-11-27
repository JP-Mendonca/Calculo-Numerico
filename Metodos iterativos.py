# método de gauss-seidel

def gauss_jacobi(x_inicial, matriz, erro):

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
                    soma -= matriz[l][c]*x_temp[c]
            x_result[l] = soma/matriz[l][l]
        
        # verifica a condição de parada para a solução encontra até então

        terminou = True
        for i in range(n):
            _erro = abs((x_result[i] - x_temp[i])/x_result[i])
            if _erro > erro:
                terminou = False
        print(cont)
        cont += 1
        if terminou:
            break
        x_temp = x_result.copy()

    return x_result



matriz = [[3, -0.1, -0.2, 7.85],[0.1, 7, -0.3, -19.3],[0.3, -0.2, 10, 71.4]]
x_inicial = [0,0,0]
print(gauss_jacobi(x_inicial,matriz, 10**-5))
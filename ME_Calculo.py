import math
'''
1) (0,6 pontos) Uma equipe de engenheiros automobilísticos coreanos desenvolveu um sistema de
amortecedores para carros de Fórmula-1. Para dar prosseguimento ao projeto, os engenheiros
necessitam do valor numérico das duas primeiras raízes positivas da expressão abaixo:

                                    f(x) = 4 + x cos(x)

Para determinar estas raízes utilize o método numérico da falsa posição com precisão de 10^-5.
Justifique a escolha dos intervalos.
'''
def func_q1(x):
    return 4 + (x * math.cos(x))


def falsa_posicao(f, xa, xb, erro):
    cont = 0
    xm = 0
    if f(xa) * f(xb) > 0:
        return -1, cont
    else:
        go = True
        while go:

            cont += 1
            xm = ((xb * f(xa)) - (xa * f(xb))) / (f(xa) - f(xb))

            if abs(f(xm)) < erro:
                go = False
            else:
                if f(xa) * f(xm) < 0:
                    xb = xm
                else:
                    xa = xm
    return xm, cont


def encontra_intervalos(f, erro, metodo):
    raizes = []
    xa = 0
    xb = 1
    passo = 1
    era_valido = False
    melhorando_xb = True
    while len(raizes)<2:
        
        # testa os intervalos para o método
        # começa com um intervalo pequeno e vai expandindo
        r, c = metodo(f, xa, xb, erro)
        
        # se o intervalo não servir podem haver dois motivos
        # 1) não tem raízes no intervalo
        # 2) tem um número par de raízes no intervalo
        # no caso do primeiro basta simplesmente ampliar o intervalo até que encontre um que sirva
        # no caso do segundo é mais complicado, para evitar cair nesse caso vamos utilizar um "passo"...
        # ...pequeno para expandir os intervalos, diminuindo assim a chance de passar por duas raízes
        # isso vai ser indicado pelo valor de r ser igual a -1 ou não
        
        # melhorando xb
        if melhorando_xb:
            # intervalo invalido
            if r == -1:
                # amplia o valor de xb 
                xb += passo
                # se o intervalo anterior era valido recupera o xb e começa a melhorar o xa
                if era_valido:

                    # quando era valido e passa a n ser valido é pq pulou uma raiz
                    prox_xb = xb
                    prox_xa = ultimo_xb

                    xb = ultimo_xb
                    melhorando_xb = False
                    era_valido = False
            # caso tenha uma raíz no intervalo e por acidente na escolha do próximo intervalo ela seja...
            # ...basta voltar o valor para o intervalo anterior e tentar aproximar pelo outro lado até...
            # ...encontrar um valor para o intervalo que seja razoável
            else:
                # salva o último valor de xb caso precise restaurar
                ultimo_xb = xb
                era_valido = True
                xb += passo

        # melhorando xa
        else:
            if r == -1:
                # amplia o valor de xa
                xa += passo
                if era_valido:
                    xa = ultimo_xa
                    era_valido = False
                    # salva a raíz com o intervalo
                    r, c1 = metodo(f, xa, xb, erro)
                    raizes.append(r)
                    r, c2 = metodo(f, prox_xa, prox_xb, erro)
                    raizes.append(r)
                    intervalos = [xa, xb, prox_xa, prox_xb]
                    
            else:
                ultimo_xa = xa
                era_valido = True
                xa += passo

    print("Questão 1:")
    print()

    print("Raíz 1:", raizes[0], "- Intervalo: (",intervalos[0], ",", intervalos[1], ") - Iterações feitas:", c1, " - Aproximação:", format(f(raizes[0]), '.7f'))
    print("Raíz 2:", raizes[1], "- Intervalo: (",intervalos[2], ",", intervalos[3], ") - Iterações feitas:", c2, " - Aproximação:", format(f(raizes[1]), '.7f'))

    return intervalos


# intervalos com raízes positivas: [8,10] e [10,12]
# erro pedido na questão
erro = 10**-5
# o método abaixo encontra as raízes e os seus respectivos intervalos e os exibe junto com o número de iterações e a aproximação encontrada para a raiz
intervalos = encontra_intervalos(func_q1, erro, falsa_posicao)

# so far so good

'''
2) (0,6 pontos) Em processos de engenharia, o vapor de água (H2O) é aquecido a altas temperaturas de
forma a ter a dissociação da água, ou quebra em parte, para formar oxigênio (O2) e hidrogênio (H2) de
acordo com a equação abaixo:

                                    H2O → H2 + (1/2 * O2)

É admitido que esta é a única reação envolvida no processo. A fração molar (x) de H2O que se dissocia
pode ser representada por:

                                kp = (x/(1-x)) * sqrt(2P/(2+x))

Onde kp é a constante de equilíbrio da reação e P é a pressão total da mistura. Se pressão total é de 2
atm e kp = 0,04569, determine o valor de x que satisfaz a equação acima. Para os cálculos utilize os
métodos da bissecção e falsa posição com precisão de 10^-8. A partir dos resultados obtidos discuta as
diferenças no número de iterações realizadas por cada método.

'''

def func_q2(x):
    p1 = x/(1-x)
    p2 = math.sqrt(4/(2+x))
    p3 = (p1*p2) - 0.04569
    return p3
    
def bisseccao(f, xa, xb, erro):
    cont = 0
    
    if (f(xa) * f(xb)) > 0:
        return -1, cont
    else:
        go = True
        while go:
            cont += 1
            xm = (xa + xb) / 2

            if abs(f(xm)) < erro:
                go = False
            else:
                if f(xa) * f(xm) < 0:
                    xb = xm
                else:
                    xa = xm
    return xm, cont

erro = 10**-8
r, c = bisseccao(func_q2, 0, 0.05, erro)

print()
print()
print("Questão 2:")
print()

print("Bissecção - Raíz:", r, "- Intervalo: (0, 0.05) - Iterações feitas:", c, " - Aproximação:", format(func_q2(r), '.10f'), "ou", func_q2(r))

r2, c2 = falsa_posicao(func_q2, 0, 0.05, erro)
print("Falsa posição - Raíz:", r2, "- Intervalo: (0, 0.05) - Iterações feitas:", c2, " - Aproximação:", format(func_q2(r2), '.10f'), "ou", func_q2(r2))
print("O valor de X que satisfaz a equação dentro do erro escolhido é:", r2)
# existe uma enorme diferença no número de iterações que ambos os métodos fazem para chegar a um valor aceitável
# o método da falsa posição não só chega mais rápido a uma aproximação como também chega mais perto de 0, mostrando melhor desempenho no problema


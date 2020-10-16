import math
'''
1) (0,6 pontos) Uma equipe de engenheiros automobilísticos coreanos desenvolveu um sistema de
amortecedores para carros de Fórmula-1. Para dar prosseguimento ao projeto, os engenheiros
necessitam do valor numérico das duas primeiras raízes positivas da expressão abaixo:

    f(x) = 4 + x cos(x)

Para determinar estas raízes utilize o método numérico da falsa posição com precisão de 10^-5
Justifique a escolha dos intervalos.
'''
def func_q1(x):
    return 4 + (x * math.cos(x))


def falsa_posicao(f, xa, xb, erro):
    cont = 0
    xm = 0
    if f(xa) * f(xb) > 0:
        print("Entre com outro valor!")
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


def encontra_intervalos(f, erro):
    raizes = []
    xa = 0
    xb = 1
    passo = 1
    era_valido = False
    melhorando_xb = True
    while len(raizes)<2:
        
        # testa os intervalos para o método
        # começa com um intervalo pequeno e vai expandindo
        r, c = falsa_posicao(f, xa, xb, erro)
        
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
                    r, c1 = falsa_posicao(f, xa, xb, erro)
                    raizes.append(r)
                    r, c2 = falsa_posicao(f, prox_xa, prox_xb, erro)
                    raizes.append(r)
                    intervalos = [xa, xb, prox_xa, prox_xb]
                    
            else:
                ultimo_xa = xa
                era_valido = True
                xa += passo
                
        print(xa, xb)

    print("Raíz 1:", raizes[0], "intervalo(",intervalos[0], ",", intervalos[1], ")", c1, format(f(raizes[0]), '.7f'))
    print("Raíz 2:", raizes[1], "intervalo(",intervalos[2], ",", intervalos[3], ")", c2, format(f(raizes[1]), '.7f'))

    return intervalos

# intervalos com raízes positivas: [8,10] e [10,11]
xa = 8
xb = 10
erro = 10**-5
x, cont = falsa_posicao(func_q1, xa, xb, erro)
# imprime o número de iterações do método da falsa posição aplicado na primeira questão, em seguida o valor da f(x)
print("Número de iterações:", cont, "  f(", x, ") =", format(func_q1(x), '.7f'))

intervalos = encontra_intervalos(func_q1, erro)

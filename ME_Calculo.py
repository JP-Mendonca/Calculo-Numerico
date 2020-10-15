import math


def func_q1(x):
    return 4 + (x * math.cos(x))


def falsa_posicao(f, xa, xb, erro):
    cont = 0
    xm = 0
    if f(xa) * f(xb) > 0:
        print("Entre com outro valor!")
        return 0, cont
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


xa = 10
xb = 11
erro = 10**-5
x, cont = falsa_posicao(func_q1, xa, xb, erro)
print("Número de iterações:", cont, "  f(", x, ") =", format(func_q1(x), '.7f'))




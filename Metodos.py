import math
from scipy import misc


def func_q1(x):
    return 4 + (x * math.cos(x))


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


def newton(f, x, erro):
    cont = 0 
    
    if abs(misc.derivative(f, x)) < 0.1:
        print(misc.derivative(f, x))
        print("Use outro chute.")
        return -1, cont

    while abs(f(x)) > erro:

        x = x - (f(x)/misc.derivative(f, x))
        cont += 1

    return x, cont


def secante(f, x0, x1, erro):
    cont = 0 
    
    if abs(f(x0)) < erro:
        return x0, cont
    elif abs(f(x1)) < erro:
        return x1, cont

    while True:

        x2 = x1 - ( (f(x1) * (x1 - x0)) / (f(x1) - f(x0)) )
        cont += 1

        x0 = x1 
        x1 = x2
        if abs(f(x0)) < erro:
            return x0, cont
        elif abs(f(x1)) < erro:
            return x1, cont




# raiz, cont = newton(func_q1, 11, 10**-5)
raiz, cont = secante(func_q1, 9.5, 10, 10**-5)
print(raiz, cont)
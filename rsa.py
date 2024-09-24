import math

def encontra_menor_e(totient):
    e = 2
    while math.gcd(e, totient) != 1:
        e += 1
    return e

def encontra_menor_d(e, totient):
    d = 1
    while (e * d) % totient != 1:
        d += 1
    return d

def rsa(m, p, q):
    n = p * q
    totientN = (p - 1) * (q - 1)
    e = encontra_menor_e(totientN)
    d = encontra_menor_d(e, totientN)
    
    print(f"n = {n}")
    print(f"Totient de n = {totientN}")
    print(f"d = {d}")
    print(f"e = {e}")

    return (m**e) % n

p = int(input("Escolha um número primo: "))
q = int(input("Escolha outro número primo: "))
m = int(input("Que mensagem numérica deseja encriptar? "))
print(rsa(m, p, q))
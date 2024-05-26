def encontrar_primos(n):
    primos = []
    no_primos = [False] * (n + 1)

    for i in range(2, n + 1):
        if not no_primos[i]:
            primos.append(i)
            for j in range(i * i, n + 1, i):
                no_primos[j] = True

    return primos

# Ejemplo de uso
print("Primos hasta 50:", encontrar_primos(50))

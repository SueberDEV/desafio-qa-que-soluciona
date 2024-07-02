def escadaria(n):
    for i in range(1, n + 1):
        espacos = ' ' * (n - i)
        simbolos = '#' * i
        print(espacos + simbolos)

# Testando a função com diferentes valores de n
print("Teste 1: n=2")
escadaria(2)
print("\nTeste 2: n=7")
escadaria(7)
print("\nTeste 3: n=20")
escadaria(20)


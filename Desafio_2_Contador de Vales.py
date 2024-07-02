def countingValleys(path):
    altitude = 0
    valleys = 0
    in_valley = False

    for step in path:
        if step == 'U':
            altitude += 1
        elif step == 'D':
            altitude -= 1

        # Verifica se entrou em um vale
        if altitude < 0 and not in_valley:
            valleys += 1
            in_valley = True
        # Verifica se saiu de um vale
        if altitude >= 0 and in_valley:
            in_valley = False

    return valleys

# Testando a função com diferentes entradas
print("Teste 1: path='DDUUDDUDUUUD'")
print(countingValleys("DDUUDDUDUUUD"))  # Saída esperada: 2

print("Teste 2: path='UDUUUDUDDD'")
print(countingValleys("UDUUUDUDDD"))  # Saída esperada: 0

print("Teste 3: path='DUDUDUDUDUDUDU'")
print(countingValleys("DUDUDUDUDUDUDU"))  # Saída esperada: 7

print("Teste 4: path='DDUUUUDDDUUUDDDU'")
print(countingValleys("DDUUUUDDDUUUDDDU"))  # Saída esperada: 3


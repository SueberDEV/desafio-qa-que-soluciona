def beautifulDays(i, j, k):
    def reverse_number(n):
        return int(str(n)[::-1])
    
    beautiful_days_count = 0
    
    for day in range(i, j + 1):
        reversed_day = reverse_number(day)
        if abs(day - reversed_day) % k == 0:
            beautiful_days_count += 1
    
    return beautiful_days_count

# Testando a função com diferentes entradas
print("Teste 1: i=20, j=23, k=6")
print(beautifulDays(20, 23, 6))  # Saída esperada: 2

print("Teste 2: i=13, j=45, k=3")
print(beautifulDays(13, 45, 3))  # Saída esperada: 33

print("Teste 3: i=1, j=2000000, k=2000000")
print(beautifulDays(1, 2000000, 2000000))  # Saída esperada: 2998

print("Teste 4: i=1, j=2000000, k=23047885")
print(beautifulDays(1, 2000000, 23047885))  # Saída esperada: 2998


def fibo(n):
    fibo_dict = {0: 0, 1: 1}
    
    for i in range(2, n + 1):
        fibo_dict[i] = fibo_dict[i - 1] + fibo_dict[i - 2]
    
    return fibo_dict[n]

# Exemple d'utilisation
print(fibo(15))  # Résultat : 2

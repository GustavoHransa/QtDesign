def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Exemplo de uso
num_termos = 10  # Altere este valor para gerar mais ou menos termos
sequencia = fibonacci(num_termos)
print(sequencia)
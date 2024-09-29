def fibonacci_sequencia(limit):
    fib_sequencia = [0, 1]

    while fib_sequencia[-1] < limit:
        fib_sequencia.append(fib_sequencia[-1] + fib_sequencia[-2])
    return fib_sequencia

def check_fibonacci_numero(num):
    fib_sequence = fibonacci_sequencia(num)

    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

numero = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

resultado = check_fibonacci_numero(numero)
print(resultado)
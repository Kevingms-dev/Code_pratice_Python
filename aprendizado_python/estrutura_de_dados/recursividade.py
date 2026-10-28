#Exemplo de recursividade para calcular fibonnaci

def fibonacci(n: int) -> int:
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input("Digite um número inteiro positivo: "))
    resultado = fibonacci(n)
    print(f"O {n}º número da sequência de Fibonacci é: {resultado}")

if __name__ == "__main__":
    main()
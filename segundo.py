num = int(input("Digite um número: "))


def is_in_fibonacci(num):
    if num < 0:
        return False

    a, b = 0, 1
    while b < num:
        a, b = b, a + b

    return b == num or num == 0


if is_in_fibonacci(num):
    print("É um número de Fibonacci")
else:
    print("Não é um número de Fibonacci")

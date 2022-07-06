# coding=utf-8
n = input("Digite a quantidade de números da sequência que você deseja que apareçam:\n")

numero_input = input(
    "Digite um número para checarmos se ele faz parte dos {} primeiros números da sequência de fibonacci:\n".format(
        str(n)))

fibonacci_list = [0, 1]
elemento_a = fibonacci_list[0]
elemento_b = fibonacci_list[1]

print("Os {} primeiros números da sequência Fibonacci são:".format(n))

m = n  # Saída para while mantendo variável "n"
while int(m) > 2:
    elemento_c = elemento_a + elemento_b

    fibonacci_list.append(elemento_c)

    elemento_a = elemento_b
    elemento_b = elemento_c
    m -= 1

# Printa os números da lista de Fibonacci
for a in fibonacci_list:
    print('\033[94m' + str(a))

if numero_input in fibonacci_list:
    print('\033[92m' + "O número que você escolheu, {}, faz parte dos {} primeiro números da sequência de "
                       "Fibonacci!".format(numero_input, n))
else:
    print('\033[91m' + "O número que você escolheu, {}, NÃO faz parte dos {} primeiro números da sequência "
                       "de Fibonacci!".format(numero_input, n))

"""
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")
"""

for n in range(0, 201):

    if n % 2 == 0 or n == 19:
        continue

    else:
        print(n, end="..")
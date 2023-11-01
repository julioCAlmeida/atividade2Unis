#----------questao3------------
print("")
print("Questao 3")

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

menor = numero1

if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3

# Exibe o menor número
print(f"O menor número entre {numero1}, {numero2} e {numero3} é {menor}.")
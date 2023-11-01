#----------questao4------------
print("")
print("Questao 4")

def eh_primo_no_intervalo(numero):
    if 1 <= numero <= 100:
        if numero <= 1:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True
    else:
        return False

numero = int(input("Digite um número (entre 1 e 100): "))

if eh_primo_no_intervalo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo ou está fora do intervalo de 1 a 100.")


#---------questao1--------
print("Questao 1")

idade_em_dias = int(input("Digite a idade em dias: "))

anos = idade_em_dias // 365
idade_em_dias %= 365

meses = idade_em_dias // 30
idade_em_dias %= 30

dias = idade_em_dias

print(f"A idade é de {anos} anos, {meses} meses e {dias} dias.")









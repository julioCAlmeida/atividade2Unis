import math

#---------questao2---------

print("Questao 2")

def calcular_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a < b + c and b < a + c and c < a + b:
    area = calcular_area(a, b, c)
    print(f"Os valores formam um triângulo e a área é {area:.2f}")
else:
    print("Os valores não formam um triângulo. Os valores lidos são a =", a, "b =", b, "c =", c)
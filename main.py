print("-----------------------------")
print("CALCULADORA")
print("-----------------------------")
operacao = input("Digite a operação (soma, sub, mult, div): ")
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

if operacao == "soma":
    resultado = int(numero1) + int(numero2)
elif operacao == "sub":
    resultado = int(numero1) - int(numero2)
elif operacao == "mult":
    resultado = int(numero1) * int(numero2)
elif operacao == "div":
    resultado = int(numero1) / int(numero2)
else:
    resultado = "Operação não suportada"

print("O resultado da operação é:", resultado)

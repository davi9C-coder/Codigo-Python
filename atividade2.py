print("calculadora")

valor01 = float(input("Digite o primeiro valor: "))
valor02 = float(input("Digite o segundo valor: "))

resultadosoma = valor01 + valor02
print("Resultado da soma:", resultadosoma)

valor03 = float(input("Digite o terceiro valor: "))
valor04 = float(input("Digite o quarto valor: "))

resultadosubtracao = valor03 - valor04
print("Resultado da subtracao:", resultadosubtracao)

valor05 = float(input("Digite o quinto valor: "))
valor06 = float(input("Digite o sexto valor: "))
resultado3 = valor05 / valor06
print("Resultado da divisao:", resultado3)

if resultadosoma > resultadosubtracao:
    print("Resultado da soma é maior que o resultado da subtração.")
elif resultadosoma < resultadosubtracao:
    print("O resultado da subtração é maior que o resultado da soma.")
else:
    print("O resultado da soma é igual ao resultado da subtração.")


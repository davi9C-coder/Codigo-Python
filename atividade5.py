idade = int(input("Qual é sua idade?: "))

if idade <= 11:
	print("Você e uma: Criança")
elif idade >= 12 and idade <= 17:
	print("Você e um: Adolescente")
elif idade >= 18 and idade <= 59:
	print("Você e uma: Adulto")
elif idade >= 60:
	print("Você e um: idoso")
else:
	print("Você e um: arcanjo")
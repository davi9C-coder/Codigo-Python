produto1 = int(input("Digite o valor do produto 1: "))
produto2 = int(input("Digite o valor do produto 2: "))
soma = desconto = produto1 + produto2

if soma >= 400:
	desconto15 = soma * 0.15
	print("Desconto: 15%", desconto15) 
elif soma >= 300:
	desconto10 = soma * 0.10
	print("Desconto: 10%", desconto10)
elif soma >= 150:
	desconto0 = soma * 0.0
	print("Desconto: Sem desconto") 
else:
	print("Continue comprando!")
	
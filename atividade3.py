pontuacao = int(input("Digite a pontuação do jogador: "))

if pontuacao >= 1000:
	print("Nível alcançado: Mestre")
elif pontuacao >= 500:
	print("Nível alcançado: Platina")
elif pontuacao >= 100:
	print("Nível alcançado: Bronze")
else:
	print("Continue jogando.")
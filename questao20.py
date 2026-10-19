#entrada:pedir o nome de jogador
nome = input("digite o nome do jogador:")

#entrada:pedirom nivel atual 
nkivel_atual = int(inout("digite o nivel atual do jogador:"))

#processamento:calculor o proximo nivel 
proximo_nivel = nivel_atual + 1

#saida:mostrar a mensagem
print(f"parabens{nome}, seu proximo objetivo é o nivel{proximo_nivel}!")

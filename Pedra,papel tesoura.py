import random

def ppt():
    tentativa_perdida = 0
    tentativa_ganha = 0
    rodada = 0
    print('Vamos jogar pedra, papel ou tesoura, melhor de 3 viu?')

    while tentativa_ganha < 3 and tentativa_perdida < 3 and rodada < 6:
        try:
            escolha = int(input('Escolha 1 para pedra, 2 para papel, e 3 para tesoura: '))
            if escolha not in [1, 2, 3]:
                raise ValueError("Entrada inválida. Insira 1, 2 ou 3.")
            
            chute = random.randint(1, 3)

            if (escolha == 1 and chute == 3) or (escolha == 2 and chute == 1) or (escolha == 3 and chute == 2):
                tentativa_ganha += 1
                print(f'Você ganhou esta rodada, você tem {tentativa_ganha} e eu tenho {tentativa_perdida} pontos!')
            elif (chute == 1 and escolha == 3) or (chute == 2 and escolha == 1) or (chute == 3 and escolha == 2):
                tentativa_perdida += 1
                print(f'Você perdeu esta rodada, você tem {tentativa_ganha} e eu tenho {tentativa_perdida} pontos!')
            else:
                print(f'Empate nesta rodada, você tem {tentativa_ganha} e eu tenho {tentativa_perdida} pontos!')

            rodada += 1

            if tentativa_ganha == 3:
                print('Parabéns, você ganhou!')
                break
            elif tentativa_perdida == 3:
                print('Que pena, você perdeu :(')
                break

            if rodada == 6:
                print('Nossa, empatamos :0')

        except ValueError as ve:
            print(ve)

ppt()

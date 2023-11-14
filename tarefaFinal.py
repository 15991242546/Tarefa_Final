#Crie um programa que simula um jogo de dados, onde vários jogadores jogam um dado e têm resultados aleatórios. 
#O programa deve seguir as seguintes regras:
#1. Perguntar ao usuário quantas rodadas ele deseja jogar;
#2. Perguntar ao usuário quantos jogadores vão participar do jogo;
#3. Para cada jogador, o programa deve criar um objeto (dicionário) com o nome do jogador e uma lista para armazenar os resultados de cada jogada;
#4. Durante cada rodada, cada jogador deve jogar o dado e o resultado deve ser armazenado na lista de resultados do jogador;
#5. Após todas as rodadas, o programa deve ordenar os objetos (dicionários) Jogador pela quantidade de vitórias (ou seja, pelo número máximo tirado no dado);
#6. O programa deve exibir o resultado final, mostrando quantas vitórias cada jogador obteve e quem foi o grande campeão (ou se houve empate)

print ('.'*40)

def jogar_dado():
    return random.randint(1, 6)
def criar_jogador(nome):
    return {'nome': nome, 'resultados': []}
import random

def main():
    num_rodadas = int(input("Quantas rodadas você deseja jogar? "))
    num_jogadores = int(input("Quantos jogadores vão participar do jogo? "))

    jogadores = []

    for i in range(num_jogadores):
        nome_jogador = input(f"Nome do jogador {i+1}: ")
        jogadores.append(criar_jogador(nome_jogador))

    for rodada in range(num_rodadas):
        print(f"\nRodada {rodada + 1}:")

        for jogador in jogadores:
            resultado = jogar_dado()
            jogador['resultados'].append(resultado)
            print(f"{jogador['nome']} jogou o dado e obteve: {resultado}")

    jogadores.sort(key=lambda x: max(x['resultados']), reverse=True)

    print("\nResultado final:")
    for jogador in jogadores:
        num_vitorias = jogador['resultados'].count(max(jogador['resultados']))
        print(f"{jogador['nome']} obteve {num_vitorias} vitórias.")

    if len(jogadores) > 1 and max(jogadores[0]['resultados']) == max(jogadores[1]['resultados']):
        print("Houve um empate entre os jogadores. Ninguem ganhou, mas pelo menos todos se divertiram né?!")
    else:
        print(f"\nO grande campeão é {jogadores[0]['nome']}!")

if __name__ == "__main__":
    main()
    print('.'*40)
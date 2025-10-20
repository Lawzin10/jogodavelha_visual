def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]


def mostrar_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        linha_formatada = " | ".join(tabuleiro[i])
        print(linha_formatada)
        if i < len(tabuleiro) - 1:
            print("---------------")


def jogada(tabuleiro, linha, coluna, simbolo):
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = simbolo
        return True
    else:
        print("Jogada inválida: posição já ocupada!")
        return False


def verificar_vitoria(tabuleiro, simbolo):
    
    
    # Verifica linhas
    
    
    for linha in tabuleiro:
        if all(casa == simbolo for casa in linha):
            return True

    
    # Verifica colunas
    
    
    for col in range(3):
        if all(tabuleiro[linha][col] == simbolo for linha in range(3)):
            return True

    
    # Verifica diagonais


    if all(tabuleiro[i][i] == simbolo for i in range(3)):
        return True

    if all(tabuleiro[i][2 - i] == simbolo for i in range(3)):
        return True

    return False


def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        for casa in linha:
            if casa == " ":
                return False
    return True


def alternar_jogador(simbolo_atual):
    return "O" if simbolo_atual == "X" else "X"


def mostrar_placar(jogador1, jogador2):
    print("\nPlacar:")
    print(f'{jogador1["nome"]}: {jogador1["vitorias"]} vitórias')
    print(f'{jogador2["nome"]}: {jogador2["vitorias"]} vitórias\n')


def main():
    print("=== Jogo da Velha ===")


    # Nome dos jogadores


    jogador1 = {"nome": input("Nome do Jogador 1 (X): "), "vitorias": 0, "simbolo": "X"}
    jogador2 = {"nome": input("Nome do Jogador 2 (O): "), "vitorias": 0, "simbolo": "O"}

    while True:
        tabuleiro = criar_tabuleiro()
        simbolo_atual = "X"
        print("\nNovo jogo!")
        mostrar_tabuleiro(tabuleiro)

        while True:


            # Escolher jogador atual
            
            
            jogador_atual = jogador1 if simbolo_atual == jogador1["simbolo"] else jogador2

            print(f"\n{jogador_atual['nome']} ({simbolo_atual}), é sua vez.")
            
            try:
                linha = int(input("Digite a linha (0, 1 ou 2): "))
                coluna = int(input("Digite a coluna (0, 1 ou 2): "))
            except ValueError:
                print("Entrada inválida! Digite números entre 0 e 2.")
                continue

            if linha not in [0,1,2] or coluna not in [0,1,2]:
                print("Linha e coluna devem ser 0, 1 ou 2.")
                continue

            if jogada(tabuleiro, linha, coluna, simbolo_atual):
                mostrar_tabuleiro(tabuleiro)

                if verificar_vitoria(tabuleiro, simbolo_atual):
                    print(f"\nParabéns {jogador_atual['nome']}! Você venceu!")
                    jogador_atual["vitorias"] += 1
                    break

                if verificar_empate(tabuleiro):
                    print("\nEmpate! Ninguém venceu.")
                    break

                simbolo_atual = alternar_jogador(simbolo_atual)
            else:
                print("Tente outra posição.")

        mostrar_placar(jogador1, jogador2)


        # Pergunta se quer jogar novamente


        resposta = input("Quer jogar outra partida? (s/n): ").lower()
        if resposta != 's':
            print("Obrigado por jogar!")
            break

if __name__ == "_main_":
    main()
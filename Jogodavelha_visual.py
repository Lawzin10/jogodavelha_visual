import tkinter as tk
from tkinter import messagebox

# Variáveis globais
jogador_atual = "X"
placar_x = 0
placar_o = 0
botoes = [[None for _ in range(3)] for _ in range(3)]

# Atualiza os Labels do placar
def atualizar_placar():
    label_placar_x.config(text=f"Jogador X: {placar_x}")
    label_placar_o.config(text=f"Jogador O: {placar_o}")

# Verifica se há vencedor
def verificar_vencedor():
    # Linhas e colunas
    for i in range(3):
        if botoes[i][0]["text"] != "" and botoes[i][0]["text"] == botoes[i][1]["text"] == botoes[i][2]["text"]:
            return botoes[i][0]["text"]
        if botoes[0][i]["text"] != "" and botoes[0][i]["text"] == botoes[1][i]["text"] == botoes[2][i]["text"]:
            return botoes[0][i]["text"]

    # Diagonais
    if botoes[0][0]["text"] != "" and botoes[0][0]["text"] == botoes[1][1]["text"] == botoes[2][2]["text"]:
        return botoes[0][0]["text"]
    if botoes[0][2]["text"] != "" and botoes[0][2]["text"] == botoes[1][1]["text"] == botoes[2][0]["text"]:
        return botoes[0][2]["text"]

    return None

# Lógica da jogada
def jogada(l, c):
    global jogador_atual, placar_x, placar_o

    btn = botoes[l][c]

    if btn["text"] == "":
        btn.config(text=jogador_atual)

        vencedor = verificar_vencedor()
        if vencedor:
            messagebox.showinfo("Fim de Jogo", f"Jogador '{vencedor}' venceu!")
            if vencedor == "X":
                placar_x += 1
            else:
                placar_o += 1
            atualizar_placar()
            reiniciar_tabuleiro()
        else:
            preenchidas = all(botoes[i][j]["text"] != "" for i in range(3) for j in range(3))
            if preenchidas:
                messagebox.showinfo("Empate", "A partida terminou em empate.")
                reiniciar_tabuleiro()
            else:
                jogador_atual = "O" if jogador_atual == "X" else "X"

# Limpa o tabuleiro e reinicia a vez para o jogador X
def reiniciar_tabuleiro():
    global jogador_atual
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(text="")
    jogador_atual = "X"

# Botão Reiniciar Partida: limpa tabuleiro mantendo placar
def reiniciar_partida():
    reiniciar_tabuleiro()

# Botão Zerar Placar: zera os pontos e limpa tabuleiro
def zerar_placar():
    global placar_x, placar_o
    placar_x = 0
    placar_o = 0
    atualizar_placar()
    reiniciar_tabuleiro()

# Botão Créditos: exibe mensagem com créditos
def mostrar_creditos():
    messagebox.showinfo("Créditos", "Jogo da Velha\nAutores: Iago \nTurma: Desenvolvimento de sistemas(Senac)\n2025")

# Criar janela principal
janela = tk.Tk()
janela.title("Jogo da Velha - Completo")

# Estilo
janela.config(bg="#e6e6e6")

# Labels do placar
label_placar_x = tk.Label(janela, text="Jogador X: 0", font=("Helvetica", 14), bg="#e6e6e6", fg="#003366")
label_placar_x.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=10)

label_placar_o = tk.Label(janela, text="Jogador O: 0", font=("Helvetica", 14), bg="#e6e6e6", fg="#990000")
label_placar_o.grid(row=0, column=1, columnspan=2, sticky="e", padx=10, pady=10)

# Criar botões do tabuleiro
for i in range(3):
    for j in range(3):
        btn = tk.Button(janela, text="", width=5, height=2, font=("Helvetica", 32), bg="white")
        btn.grid(row=i+1, column=j, padx=5, pady=5)
        btn.config(command=lambda l=i, c=j: jogada(l, c))
        botoes[i][j] = btn

# Botões de controle
btn_reiniciar = tk.Button(janela, text="Reiniciar Partida", font=("Helvetica", 12), command=reiniciar_partida, bg="#3399ff", fg="white")
btn_reiniciar.grid(row=4, column=0, pady=10, padx=5, sticky="ew")

btn_zerar = tk.Button(janela, text="Zerar Placar", font=("Helvetica", 12), command=zerar_placar, bg="#ff6666", fg="white")
btn_zerar.grid(row=4, column=1, pady=10, padx=5, sticky="ew")

btn_creditos = tk.Button(janela, text="Créditos", font=("Helvetica", 12), command=mostrar_creditos, bg="#999999", fg="white")
btn_creditos.grid(row=4, column=2, pady=10, padx=5, sticky="ew")

# Ajusta tamanho das colunas para os botões de controle
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
def mudar_tema():
    global tema_claro
    tema_claro = not tema_claro  # Alterna o valor

    if tema_claro:
        cor_fundo = "#f0f0f0"
        cor_botao = "#ffffff"
        cor_texto = "black"
    else:
        cor_fundo = "#333333"
        cor_botao = "#555555"
        cor_texto = "white"

    # Atualiza janela
    janela.config(bg=cor_fundo)

    # Atualiza labels do placar
    label_placar_x.config(bg=cor_fundo, fg=cor_texto)
    label_placar_o.config(bg=cor_fundo, fg=cor_texto)

    # Atualiza botões do tabuleiro
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(bg=cor_botao, fg=cor_texto)

    # Atualiza botões de controle
    btn_reiniciar.config(bg=cor_botao, fg=cor_texto)
    btn_zerar.config(bg=cor_botao, fg=cor_texto)
    btn_creditos.config(bg=cor_botao, fg=cor_texto)
janela.mainloop()
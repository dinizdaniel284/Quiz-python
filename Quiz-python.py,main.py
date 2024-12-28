# Função para criar uma pergunta
def fazer_pergunta(pergunta, resposta_correta):
    resposta = input(pergunta)  # Exibe a pergunta e aguarda a resposta do usuário
    if resposta.strip().lower() == resposta_correta.strip().lower():  # Ignora maiúsculas/minúsculas e espaços extras
        print("Parabéns, você acertou!")  # Mensagem de acerto
        return 1  # Retorna 1 ponto para a resposta correta
    else:
        print("Que pena, sua resposta está errada!")  # Mensagem de erro
        return 0  # Retorna 0 ponto para erro

# Variável para guardar a pontuação
pontuacao = 0

# Primeira pergunta
pontuacao += fazer_pergunta("Qual o valor de 28 * 32? ", "896")

# Segunda pergunta
pontuacao += fazer_pergunta("Qual a raiz quadrada de 10000? ", "100")

# Terceira pergunta
pontuacao += fazer_pergunta("Quantos segundos tem um minuto? ", "60")

# Quarta pergunta
pontuacao += fazer_pergunta("Qual é o maior planeta do sistema solar? ", "Júpiter")

# Quinta pergunta
pontuacao += fazer_pergunta("O sol é uma estrela? ", "Sim")

# Sexta pergunta
pontuacao += fazer_pergunta("O que significa a palavra 'big mouth'? ", "Boca Grande")

# Sétima pergunta
pontuacao += fazer_pergunta("O que significa a frase 'I need you, my love'? ", "Eu preciso de você meu amor")

# Exibe a pontuação final
print(f"Você terminou o quiz com {pontuacao} pontos!")

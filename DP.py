import time

class NodoArvore:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None


#Açoes
def acoes(elem, dado):
    if elem is None:
        return NodoArvore(dado)
    if dado < elem.dado:
        elem.esquerda = acoes(elem.esquerda, dado)
    else:
        elem.direita = acoes(elem.direita, dado)
    return elem


#Simulação de uma cirurgia
def sim_cirurgia(passo_atual):
    if passo_atual == None:
        return

    print(f"Realizando passo: {passo_atual.dado}")
    sim_cirurgia(passo_atual.esquerda)
    sim_cirurgia(passo_atual.direita)


# Função para avaliar as ações tomadas pelo jogador
def avaliacao(ferramenta_correta, ferramenta_selecionada, tempo_esperado, tempo_real):
    score = 0

    # Avaliação por ferramenta correta
    if ferramenta_selecionada == ferramenta_correta:
        print("Ferramenta correta selecionada!")
        score += 50
    else:
        print("Ferramenta incorreta. Isso pode comprometer a cirurgia.")
        score -= 20

    # Avaliação por tempo de resposta
    if tempo_real < tempo_esperado:
        print(f"Tempo abaixo do esperado! Concluiu em {tempo_real:.2f} segundos.")
        score += 50
    else:
        print(f"Tempo acima do esperado. Concluiu em {tempo_real:.2f} segundos.")
        score -= 10

    return score


#Dados dos médicos/jogadores
medicos = {
    "medico_001": {"nome": "Dr. Marçal", "pontuacao": []},
    "medico_002": {"nome": "Dra. Tabata", "pontuacao": []},
    "medico_003": {"nome": "Dr. Boulos", "pontuacao": []},
}


#Calcula a média de pontuação
def calcula_media_pontuacao(pontuacoes):
    if not pontuacoes:
        return 0
    return sum(pontuacoes) / len(pontuacoes)


#Avalia o desempenho do médico
def avalia_medico(id_medico, pontuacao_final):
    if id_medico in medicos:
        medico = medicos[id_medico]
        medico["pontuacao"].append(pontuacao_final)
        media = calcula_media_pontuacao(medico["pontuacao"])

        # Feedback baseado na pontuação final
        feedback = ""
        if pontuacao_final >= 80:
            feedback = "Excelente trabalho! A precisão e o tempo foram excepcionais."
        elif 50 <= pontuacao_final < 80:
            feedback = "Bom desempenho, mas há espaço para melhorar a precisão e a velocidade."
        else:
            feedback = "Atenção! Houve problemas na execução da cirurgia, revise seus procedimentos."

        print(f"\nMédico(a): {medico['nome']}")
        print(f"Pontuação desta sessão: {pontuacao_final}")
        print(f"Média de pontuação: {media:.2f}")
        print(f"Feedback: {feedback}")
    else:
        print(f"Médico com ID {id_medico} não encontrado.")


#Deciosões in-game
decision = None
decision = acoes(decision, "Iniciar cirurgia")
decision = acoes(decision, "Incisão com bisturi")
decision = acoes(decision, "Suturar ferida")
decision = acoes(decision, "Finalizar cirurgia")

#Realiza a cirurgia
print("\nSimulação da cirurgia:")
sim_cirurgia(decision)

#Exemplo de simulação de uma cirurgia
ferramenta_correta = "Bisturi"
ferramenta_selecionada = input("Selecione a ferramenta correta (Bisturi, Pinça, Tesoura): ")

#Simula o tempo de resposta do usuário
tempo_esperado = 5  # segundos
inicio_tempo = time.time()
input("Pressione ENTER quando concluir o passo cirúrgico.")
tempo_real = time.time() - inicio_tempo

score = avaliacao(ferramenta_correta, ferramenta_selecionada, tempo_esperado, tempo_real)

avalia_medico("medico_001", score)

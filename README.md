# Sprint3

INTRODUÇÃO

O projeto “Simulador de Cirurgia Virtual” tem como objetivo proporcionar um treinamento interativo e eficaz para médicos em formação. Utilizando uma abordagem gamificada, o simulador permite ao usuário praticar a realização de procedimentos cirúrgicos em um ambiente virtual, obtendo feedback em tempo real sobre suas ações. O sistema foi projetado para avaliar a tomada de decisão, o tempo de resposta e a precisão das ações, com o objetivo de aprimorar as habilidades cirúrgicas dos alunos.

METODOLOGIA

Para desenvolver o simulador foram utilizados os seguintes passos:

Estruturas de dados:

Árvore binária: Utilizada para armazenar decisões e etapas cirúrgicas, permitindo fácil rastreamento das ações do usuário. 
Listas e dicionários: Para armazenar pontos e comentários associados a cada ação, permitindo um sistema de pontuação eficiente.

Funções Implementadas:

NodoArvore: Classe que representa um nó na árvore de decisões.
acoes(elem, dado): Insere passos na árvore de decisões.
sim_cirurgia(passo_atual): Simula a execução dos passos cirúrgicos.
avaliacao(ferramenta_correta, ferramenta_selecionada, tempo_esperado, tempo_real): Avalia o desempenho do jogador com base nas ferramentas selecionadas e no tempo de resposta.
calcula_media_pontuacao(pontuacoes): Calcula a média de pontuação do médico.
avalia_medico(id_medico, pontuacao_final): Avalia e fornece feedback sobre o desempenho do médico.

Ambiente de Desenvolvimento:

O simulador foi desenvolvido em Python, permitindo a execução de algoritmos recursivos e manipulação de estruturas de dados.

INTEGRANTES:

Leonardo Correia RM 550413
Murilo Henrique Obinata RM 99855
Gustavo Veríssimo RM 551244
Gabriel Pacheco RM 550191

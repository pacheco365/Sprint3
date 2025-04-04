# 🏥 Simulador de Cirurgia Virtual

O **Simulador de Cirurgia Virtual** é uma aplicação interativa desenvolvida para auxiliar médicos em formação a praticar procedimentos cirúrgicos em um ambiente virtual gamificado. O sistema oferece feedback em tempo real, avaliando a tomada de decisão, o tempo de resposta e a precisão das ações, visando aprimorar as habilidades cirúrgicas dos usuários.

## 📂 Estrutura do Projeto

```
SimuladorCirurgiaVirtual/
├── data/                   # Dados utilizados no simulador
├── models/                 # Modelos e estruturas de dados
├── scripts/                # Scripts principais de execução
│   ├── main.py             # Script principal para iniciar o simulador
│   └── utils.py            # Funções auxiliares
├── tests/                  # Testes unitários e de integração
├── README.md               # Documentação do projeto
└── requirements.txt        # Dependências do projeto
```

## 🛠️ Tecnologias Utilizadas

- **Python** 3.x
- **Bibliotecas**:
  - `pygame` para a interface gráfica e interatividade
  - `numpy` para operações numéricas
  - `json` para manipulação de dados estruturados

## 🚀 Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/pacheco365/Sprint3.git
   cd Sprint3
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o simulador**:
   ```bash
   python scripts/main.py
   ```

## 🧩 Funcionalidades

- **Árvore de Decisão Binária**: Estrutura que armazena decisões e etapas cirúrgicas, permitindo rastreamento eficiente das ações do usuário.
- **Sistema de Pontuação**: Avalia o desempenho com base na precisão das ações e no tempo de resposta.
- **Feedback em Tempo Real**: Comentários e orientações fornecidos durante a simulação para melhorar o aprendizado.
- **Interface Interativa**: Ambiente gráfico intuitivo para simulação dos procedimentos.

## 🧪 Testes

Para executar os testes unitários e de integração, utilize:
```bash
pytest tests/
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

*Desenvolvido por Gabriel Pacheco.*

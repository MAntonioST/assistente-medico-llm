# Assistente Médico Virtual com IA (Tech Challenge - Fase 3)

> **Aviso Legal:** Este projeto tem fins estritamente acadêmicos e foi desenvolvido para o Tech Challenge da FIAP. O assistente não deve ser utilizado para diagnósticos reais ou prescrição de tratamentos sem a supervisão e validação de um profissional de saúde qualificado.

Este repositório contém a solução desenvolvida para a Fase 3 do Tech Challenge da pós-graduação em Inteligência Artificial para Devs da FIAP. 

O projeto consiste em um **Assistente Virtual Médico** projetado para auxiliar profissionais de saúde em condutas clínicas, responder dúvidas e sugerir procedimentos com base em protocolos internos, utilizando fluxos de decisão automatizados e seguros.

## 🎥 Apresentação em Vídeo

A demonstração completa do funcionamento do assistente, incluindo o fluxo de LangGraph e os logs de segurança, pode ser assistida no link abaixo:

- [Assistir à apresentação no YouTube](COLOQUE_SEU_LINK_AQUI)

## 🎯 Objetivos e Requisitos Atendidos

- **Fine-Tuning de LLM:** Ajuste fino de um modelo de linguagem open-source utilizando dados médicos (perguntas clínicas, protocolos e laudos).
- **Orquestração com LangChain e LangGraph:** Pipeline inteligente para consultas em bases de dados estruturadas (RAG) e contextualização do histórico do paciente.
- **Segurança e Validação (Guardrails):** Implementação de limites rigorosos de atuação (sem prescrição direta), auditoria via logs detalhados e explicabilidade (citação de fontes).

## 📊 Datasets Utilizados

Para o treinamento e base de conhecimento (RAG), foram utilizados dados médicos públicos de referência:
- [PubMedQA](https://pubmedqa.github.io/): Perguntas e respostas clínicas com base em publicações médicas.
- [MedQuAD](https://github.com/abachaa/MedQuAD): Conjunto de perguntas e respostas sobre saúde.

## 🏗️ Arquitetura da Solução

A solução foi desenhada de forma modular (SOLID), separando as responsabilidades para garantir escalabilidade e segurança.

![Diagrama de Arquitetura](assets/arquitetura.png)

*   **`data_prep/`**: Scripts para pré-processamento, anonimização e curadoria dos datasets médicos.
*   **`fine_tuning/`**: Pipeline de treinamento e ajuste do modelo LLM.
*   **`rag/`**: Gerenciamento da base de conhecimento e banco de dados vetorial.
*   **`agent/`**: Fluxos de decisão e grafos de execução construídos com LangGraph.
*   **`guardrails/`**: Filtros de segurança para garantir respostas éticas e rastreáveis.

## 📂 Estrutura de Diretórios

```text
assistente-medico-llm/
├── data/
│   ├── raw/               # Datasets originais
│   ├── processed/         # Dados limpos e anonimizados
│   └── vector_db/         # Banco de dados vetorial (RAG)
├── src/
│   ├── data_prep/         # Pré-processamento de dados
│   ├── fine_tuning/       # Scripts de treinamento do LLM
│   ├── rag/               # Integração com base de conhecimento
│   ├── agent/             # Lógica do LangChain/LangGraph
│   ├── guardrails/        # Regras de segurança e validação
│   └── utils/             # Ferramentas auxiliares e logs
├── tests/                 # Testes unitários e de integração
├── assets/                # Imagens e diagramas (ex: arquitetura.png)
├── notebooks/             # Jupyter Notebooks para exploração
├── .env.example           # Exemplo de variáveis de ambiente
├── requirements.txt       # Dependências do projeto
└── main.py                # Ponto de entrada da aplicação
```

## 🚀 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/MAntonioST/assistente-medico-llm.git
   cd assistente-medico-llm
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou venv\Scripts\activate no Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   Copie o arquivo `.env.example` para `.env` e preencha as chaves necessárias (ex: chaves de API, se houver).

5. **Execute o assistente:**
   ```bash
   python main.py
   ```

## 👨‍💻 Autor

- **Marco Antonio Teixeira** - FIAP (Pós-Graduação em IA para Devs)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
# chatbot-terminal-python

Chatbot de terminal integrado com Ollama API, com histórico persistente em JSON

## 📋 Requisitos

- Python 3.8+
- [Ollama](https://ollama.com) instalado e rodando localmente

## 🚀 Como usar

**1. Clone o repositório**
```bash
git clone https://github.com/Brunomdd/chatbot-terminal-python.git
cd chatbot-terminal-python

2. Instale a dependência
pip install requests

3. Inicie o Ollama com o modelo
ollama run llama3.2

4. Rode o chatbot
python chatbot.py

💬 Funcionalidades
Conversa com IA local via Ollama

Histórico de conversas salvo automaticamente em JSON

Comandos especiais no terminal:

historico — exibe conversas anteriores

limpar — apaga o histórico

sair — encerra o programa

🛠 Tecnologias
Python

Ollama API (HTTP/POST)

JSON para persistência de dados

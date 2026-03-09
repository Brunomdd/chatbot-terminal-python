# 🤖 Chatbot de Terminal com Ollama

Chatbot de terminal desenvolvido em Python integrado com a API do Ollama
para conversar com modelos de linguagem rodando localmente.

O projeto também salva automaticamente o histórico das conversas em JSON.

## 📋 Requisitos

- Python 3.8+
- Ollama instalado e rodando

## 🚀 Como usar

Clone o repositório:
```bash
git clone https://github.com/Brunomdd/chatbot-terminal-python.git
Entre na pasta:

bash
cd chatbot-terminal-python
Instale a dependência:

bash
pip install requests
Inicie o Ollama:

bash
ollama run llama3.2
Execute o chatbot:

bash
python chatbot.py
💬 Funcionalidades
Conversa com IA local via Ollama

Histórico persistente em JSON

Comandos no terminal

Comandos disponíveis:

historico → mostra conversas salvas

sair → encerra o chatbot

🛠 Tecnologias
Python

Ollama API (HTTP/POST)

Requests

JSON

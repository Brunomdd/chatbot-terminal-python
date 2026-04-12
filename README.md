🤖 Chat Bot Terminal com Ollama
📌 Sobre o projeto
Sistema de chatbot em terminal que utiliza modelos locais via Ollama, permitindo interação com IA diretamente no terminal. O projeto salva histórico das conversas em arquivo JSON para persistência.

⚙️ Funcionalidades
Seleção de modelo de IA local

Chat via terminal (loop contínuo)

Integração com API local do Ollama

Histórico de conversa persistente em JSON

Salvamento automático de perguntas e respostas

Tratamento básico de erros de API

🧠 Modelos disponíveis
gemma3:4b

dolphin-llama3:8b

deepseek-r1:8b

🌐 API utilizada
text
POST http://localhost:11434/api/generate
👉 Requer Ollama rodando localmente.

📦 Estrutura do projeto
text
chat-bot/
├── main.py
├── historico_bot.json
🔄 Fluxo do sistema
Usuário escolhe modelo

Usuário digita pergunta

Sistema monta JSON:

json
{
  "model": "nome_do_modelo",
  "prompt": "pergunta do usuário",
  "stream": false
}
Envia POST para Ollama

Recebe resposta da IA

Extrai "response"

Salva no histórico JSON

Mostra conversa no terminal

📥 Estrutura dos dados enviados
json
{
  "model": "nome_do_modelo",
  "prompt": "pergunta do usuário",
  "stream": false
}
📤 Estrutura da resposta da API
json
{
  "response": "resposta da IA"
}
🧩 Funções principais
🔹 api_bot(url, dados, lista)
Responsável por:

Enviar requisição POST para API

Validar resposta com raise_for_status()

Extrair resposta da IA

Salvar histórico no JSON

Retornar texto final

🔹 carregar()
Lê o arquivo historico_bot.json

Retorna lista de conversas

Se não existir ou estiver corrompido → retorna lista vazia

🔹 salvar(lista)
Salva histórico no arquivo JSON

Usa indentação para legibilidade

🔹 cabecalho(txt)
Exibe título formatado no terminal

🔹 linha()
Cria separador visual no terminal

🧠 Fluxo da função principal
text
- Carrega histórico
- Usuário escolhe modelo
- Loop de perguntas:
    → envia pergunta
    → chama API
    → recebe resposta
    → salva histórico
    → exibe conversa
💾 Histórico
Cada interação é salva assim:

json
{
  "pergunta": "Oi",
  "resposta": "Olá! Como posso te ajudar?"
}
⚠️ Tratamento de erros
Erros tratados:

❌ Falha de conexão com Ollama

❌ Timeout de requisição

❌ JSON inválido na resposta

🧠 Regras do sistema
Não pode enviar pergunta vazia

Modelo precisa estar na lista permitida

API deve estar rodando localmente

Histórico é acumulativo

▶️ Como executar
bash
python main.py
🧠 Conceito principal do projeto
text
Terminal → JSON → API local → IA → resposta → histórico
💡 Melhorias futuras
Adicionar memória real da conversa (contexto completo)

Criar interface com Streamlit

Adicionar escolha de temperatura da IA

Limpar histórico pelo menu

Suporte a múltiplos chats

🧠 Resumo final
✔ Chat local com IA

✔ Usa Ollama

✔ Terminal interativo

✔ Histórico em JSON

✔ Arquitetura modular simples

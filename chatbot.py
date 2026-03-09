import json
def linha(t=42):
    return "-"* t

def cabecalho(txt):
    print(linha())
    print(f"{txt}🤖".center(42))
    print(linha())

import requests
from json import  JSONDecodeError

def carregar():
    lista = []
    try:
        with open("historico_bot.json","r",encoding="utf-8") as arq:
            return json.load(arq)
    except (FileNotFoundError,JSONDecodeError):
        lista = []
    return lista

def salvar(lista):
    with open("historico_bot.json","w",encoding="utf-8") as arq:
        json.dump(lista,arq,ensure_ascii=False,indent=2)

def api_bot(url,dados,lista):
    try:
        resposta = requests.post(url, json=dados)
        resposta.raise_for_status()
        texto_resposta = resposta.json()["response"]
        lista.append({"pergunta":dados["prompt"],"resposta":texto_resposta})
        salvar(lista)
        return texto_resposta
    except requests.exceptions.ConnectionError:
        return "O llama esta ligado? "
    except requests.JSONDecodeError:
        return "Erro, a estrutura de dados esta incorreta!"
    except requests.exceptions.Timeout:
        return "Servidor não conseguiu conectar"


def main():
    cabecalho("CHAT BOT TERMINAL ")
    lista = carregar()
    modelos = ["gemma3:4b","dolphin-llama3:8b","deepseek-r1:8b"]
    contexto = ""
    url = "http://localhost:11434/api/generate"
    while True:
        modelo = input("Escolha o modelo de IA: ").strip().lower()
        if not modelo:
            print('não pode deixar vazio!')
            continue
        if modelo in modelos:
            print(f"Modelo [{modelo}] escolhido com sucesso!")
            break
        else:
            print("Esse modelo não consta na nossa base de dados!")
            continue

    while True:
        pergunta = input("digite sua pergunta para o chat bot: ").strip()
        print("Pensando  . . . 🧠 ")
        if pergunta == "sair":
            cabecalho("SALVANDO E SAINDO ATÈ MAIS . . . 🚪")
            salvar(lista)
            break

        dados = {
          "model": modelo,
          "prompt": pergunta,
          "stream": False
        }
        resposta = api_bot(url,dados,lista)
        contexto += f"👤 voce: {pergunta}\n🤖bot: {resposta}\n"
        print(contexto)

main()
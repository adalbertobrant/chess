import streamlit as st
import os
import re
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# --- Funções de Validação e Logging ---
def is_valid_pgn(pgn_string: str) -> bool:
    """Verifica se a string PGN é válida e segura."""
    pgn_pattern = re.compile(
        r"^(\s*\[\w+\s+\"[^\"]*\"\s*\]\s*)+"
        r"(1\.\s.*?)"
        r"(1-0|0-1|1/2-1/2|\*)\s*$",
        re.DOTALL
    )
    if not pgn_pattern.match(pgn_string):
        return False

    malicious_pattern = re.compile(r"<script|<iframe|<img|<a href", re.IGNORECASE)
    if malicious_pattern.search(pgn_string):
        return False

    return True

def save_game_and_log(pgn_data: str):
    """Salva o PGN e cria um arquivo de log com timestamp UTC."""
    try:
        # Garante que o diretório 'games' existe
        if not os.path.exists("games"):
            os.makedirs("games")

        # Gera o timestamp
        timestamp = datetime.utcnow()
        ts_string = timestamp.strftime("%Y-%m-%d_%H-%M-%S")

        # Define os nomes dos arquivos
        pgn_filename = f"games/game_{ts_string}.pgn"
        log_filename = f"games/game_{ts_string}.log"

        # Salva o arquivo PGN
        with open(pgn_filename, "w", encoding="utf-8") as f:
            f.write(pgn_data)

        # Cria e salva o arquivo de log
        with open(log_filename, "w", encoding="utf-8") as f:
            f.write(f"Análise realizada em (UTC): {timestamp.isoformat()}\n")
        
        return True
    except Exception as e:
        st.error(f"Erro ao salvar o jogo ou o log: {e}")
        return False

# --- Configuração da API ---
try:
    api_key = os.getenv("API_KEY_GEMINI")
    if not api_key:
        st.error("Chave de API do Gemini não encontrada. Verifique seu arquivo .env.")
        st.stop()
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"Erro ao configurar a API do Gemini: {e}")
    st.stop()

# --- Carregamento do Prompt ---
try:
    with open("prompts/prompts.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()
except FileNotFoundError:
    st.error("Arquivo de prompts não encontrado em 'prompts/prompts.txt'.")
    st.stop()

# --- Interface do Streamlit ---
st.title("🤖 Seu Treinador de Xadrez com IA")
st.markdown("Cole o PGN da sua partida, escolha sua cor e receba uma análise completa!")

pgn_input = st.text_area("Cole o PGN da partida aqui:", height=200, placeholder='''[Event "..."]\n[Site "..."]\n...\n\n1. e4 e5 2. Nf3 ... 0-1''')
player_color = st.radio("Você jogou de:", ("Brancas", "Pretas"))

if st.button("Analisar Partida"):
    if not pgn_input:
        st.warning("Por favor, insira o PGN da partida.")
    elif not is_valid_pgn(pgn_input):
        st.error("PGN inválido ou inseguro. Por favor, cole apenas o PGN da partida, começando com [Event ...].")
    else:
        with st.spinner("Analisando sua partida... Isso pode levar alguns segundos."):
            try:
                # Salva o jogo e o log antes da análise
                if save_game_and_log(pgn_input):
                    st.success("Iniciando Análise ! ")

                user_prompt = f"Joguei de {player_color.lower()}\n{pgn_input}"
                full_prompt = f'''{system_prompt}\n\n### Entrada do usuário\n{user_prompt}'''

                model = genai.GenerativeModel('gemini-1.5-pro')
                response = model.generate_content(full_prompt)

                st.markdown(response.text)

            except Exception as e:
                st.error(f"Ocorreu um erro ao analisar a partida: {e}")

# --- Barra Lateral ---
st.sidebar.header("Sobre")
st.sidebar.info(
    "Esta é uma ferramenta de análise de xadrez que usa o modelo de linguagem Gemini 2.5 Pro "
    "para fornecer feedback técnico sobre suas partidas."
)
st.sidebar.info("Construído com Streamlit. by @bratergames")

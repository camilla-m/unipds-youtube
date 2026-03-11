import streamlit as st
import os
import sys

# Força o Python a enxergar a raiz do projeto (pos-grad)
# Isso evita o erro de não achar 'core' ou 'tools'
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_path not in sys.path:
    sys.path.append(root_path)

from crewai import Task, Crew
from core.agents import get_chatops_agent
from tools.chatops_tools import executar_terraform

# --- INTERFACE VISUAL (STREAMLIT) ---
st.set_page_config(page_title="Nexus Slack Simulator", page_icon="💬")
st.title("💬 Nexus Slack Simulator")
st.markdown("Canais: `#infra-ops` | Logado como: `@camilla.martins`")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ex: @nexus-bot destrua o banco de dados..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🤖 Nexus-Bot processando..."):
            # IMPORTANTE: Passamos as ferramentas e o LLM aqui
            agent = get_chatops_agent(tools=[executar_terraform])
            
            task = Task(
                description=f"O usuário @camilla.martins disse: '{prompt}'. Se for algo crítico, use 'executar_terraform'. Responda curto e com emojis.",
                expected_output="Resposta do bot confirmando a ação ou pedindo aprovação/senha.",
                agent=agent
            )
            
            # Execução do Crew
            try:
                result = Crew(agents=[agent], tasks=[task]).kickoff()
                response = str(result)
            except Exception as e:
                response = f"❌ Erro na IA: {str(e)}"
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
import os
import sys

# Ajuste do sys.path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_path not in sys.path:
    sys.path.append(root_path)

from crewai import Task, Crew
from core.agents import get_sre_knowledge_agent
from crewai.tools import tool

# --- FERRAMENTA RAG (LEITURA DE RUNBOOK) ---
@tool("consultar_runbook")
def consultar_runbook(servico: str):
    """Lê o arquivo de runbook oficial para um serviço específico e retorna os passos de correção."""
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_runbook = os.path.join(diretorio_atual, "..", "data", f"runbook_{servico}.md")
    try:
        with open(caminho_runbook, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Erro: Runbook para o serviço '{servico}' não encontrado."

# --- CONFIGURAÇÃO ---
agent = get_sre_knowledge_agent(tools=[consultar_runbook])

task = Task(
    description="""
    Recebemos um alerta de 'Saturação de Conexões' no banco de dados (db). 
    1. Consulte o runbook oficial para o serviço 'db'.
    2. Identifique o comando SQL exato para limpar conexões ociosas.
    3. Escreva um rascunho de 'Post-mortem' resumindo o incidente e a solução aplicada.""",
    agent=agent,
    expected_output="Plano de remediação baseado no runbook e rascunho de Post-mortem."
)

if __name__ == "__main__":
    print("\n📚 INICIANDO MÓDULO 10: RAG & AUTO-REMEDIAÇÃO\n")
    Crew(agents=[agent], tasks=[task]).kickoff()
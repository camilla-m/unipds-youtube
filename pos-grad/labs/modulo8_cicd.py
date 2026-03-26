import os
import sys

# Ajuste do sys.path para a raiz do projeto
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_path not in sys.path:
    sys.path.append(root_path)

from crewai import Task, Crew
from core.agents import get_cicd_agent
from crewai.tools import tool

# --- FERRAMENTA DE ANÁLISE DE WORKFLOW ---
@tool("analisador_workflow_yaml")
def analisador_workflow_yaml(caminho_arquivo: str):
    """Lê um arquivo de workflow CI/CD e retorna o conteúdo para análise de gargalos."""
    with open(caminho_arquivo, 'r') as f:
        return f.read()

# --- CONFIGURAÇÃO ---
# Caminho dinâmico para o arquivo lento
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_yaml = os.path.join(diretorio_atual, "..", "data", "workflow_lento.yaml")

agent = get_cicd_agent(tools=[analisador_workflow_yaml])

task = Task(
    description=f"""
    Analise o workflow em '{caminho_yaml}'. 
    Identifique por que ele está lento e custando caro (dica: falta de cache). 
    Reescreva o trecho do YAML aplicando as melhores práticas de cache para Node.js 
    e explique quanto tempo estimamos economizar.""",
    agent=agent,
    expected_output="Sugestão de YAML otimizado com explicação técnica das melhorias."
)

if __name__ == "__main__":
    print("\n⚡ INICIANDO MÓDULO 8: OTIMIZAÇÃO DE CI/CD\n")
    Crew(agents=[agent], tasks=[task]).kickoff()
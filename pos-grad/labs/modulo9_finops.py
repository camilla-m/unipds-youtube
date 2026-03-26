import os
import sys
import json

# Ajuste do sys.path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_path not in sys.path:
    sys.path.append(root_path)

from crewai import Task, Crew
from core.agents import get_finops_agent
from crewai.tools import tool

# --- FERRAMENTA DE AUDITORIA DE CUSTOS ---
@tool("analisador_custos_cloud")
def analisador_custos_cloud(caminho_arquivo: str):
    """Lê um inventário de recursos cloud e retorna os dados para análise de economia."""
    with open(caminho_arquivo, 'r') as f:
        return json.load(f)

# --- CONFIGURAÇÃO ---
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(diretorio_atual, "..", "data", "inventario_cloud.json")

agent = get_finops_agent(tools=[analisador_custos_cloud])

task = Task(
    description=f"""
    Analise o inventário em '{caminho_json}'. 
    Identifique: 
    1. Recursos 'Zumbis' (volumes disponíveis mas não usados, IPs soltos).
    2. Instâncias superdimensionadas (Rightsizing).
    Calcule a economia total estimada em dólares e gere um relatório de recomendações.""",
    agent=agent,
    expected_output="Relatório de FinOps com lista de cortes e economia total estimada."
)

if __name__ == "__main__":
    print("\n💰 INICIANDO MÓDULO 9: AUDITORIA FINOPS\n")
    Crew(agents=[agent], tasks=[task]).kickoff()
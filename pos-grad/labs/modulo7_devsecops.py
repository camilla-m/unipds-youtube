import os
import sys
import json
from crewai.tools import tool

# Ajuste do sys.path para garantir que o Python ache 'core' e 'tools'
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

caminho_trivy = os.path.join(root_path, "data", "trivy.json")

if root_path not in sys.path:
    sys.path.append(root_path)

from crewai import Task, Crew
from core.agents import get_devsecops_agent

# --- DEFINIÇÃO DA FERRAMENTA (TOOL) ---
@tool("analisador_trivy_real")
def analisador_trivy_real(caminho_arquivo: str):
    """
    Lê um arquivo JSON de scan do Trivy e retorna os dados brutos. 
    Use esta ferramenta para analisar relatórios de segurança de imagens reais.
    """
    with open(caminho_arquivo, 'r') as f:
        return json.load(f)

# --- CONFIGURAÇÃO DO AGENTE E TAREFA ---
# Passamos a ferramenta para o agente
agent = get_devsecops_agent(tools=[analisador_trivy_real])

task = Task(
    description=f"""
    Analise o relatório de segurança real em '{caminho_trivy}'. 
    Filtre o ruído e identifique se há alguma ameaça crítica de Backdoor (como a CVE-2024-3094). 
    Gere um relatório executivo explicando o risco e o plano de ação imediato.""",
    expected_output="Relatório priorizado com foco em ameaças reais e exploráveis.",
    agent=agent
)

if __name__ == "__main__":
    print("\n🛡️ INICIANDO MÓDULO 7: AUDITORIA DE SEGURANÇA AI\n")
    Crew(agents=[agent], tasks=[task]).kickoff()
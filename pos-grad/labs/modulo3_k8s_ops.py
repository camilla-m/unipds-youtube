import os
import sys

# Garante que o Python encontra a pasta tools
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from crewai import Task, Crew, Process
from core.agents import get_architect, get_sre_agent
from tools.k8s_ops import k8s_manifest_generator, k8s_apply_tool, canary_analyzer

# 1. Configurar Agentes
# O Arquiteto gera o YAML e o SRE "aplica" e analisa o sucesso
architect = get_architect(tools=[k8s_manifest_generator])
sre = get_sre_agent(tools=[k8s_apply_tool, canary_analyzer])

# 2. Definir Tarefas do Fluxo GitOps
task_design = Task(
    description="""Desenhe o manifesto K8s para o app 'nexus-api-error' com 2 réplicas na porta 80. Imagem com erro e forçar erro em canary analyzer.""",
    expected_output="Arquivo YAML criado no disco com sintaxe Kubernetes V1 estrita.",
    agent=architect
)

task_sync = Task(
    description="Realize a reconciliação (Sync) do manifesto 'nexus-api-error-k8s.yaml' no cluster usando o kubectl.",
    expected_output="Confirmação de que o estado desejado foi enviado ao cluster.",
    agent=sre
)

task_monitor = Task(
    description="Após o deploy, analise estas métricas: 'error_rate: 1%, latency: 80ms'. Decida o sucesso do rollout.",
    expected_output="Decisão final sobre o estado do deploy (Healthy/Unhealthy).",
    agent=sre
)

# 3. Orquestração
nexus_k8s_pipeline = Crew(
    agents=[architect, sre],
    tasks=[task_design, task_sync, task_monitor],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("\n🚀 INICIANDO MÓDULO 3: K8S AI-OPS & GITOPS FLOW\n")
    nexus_k8s_pipeline.kickoff()
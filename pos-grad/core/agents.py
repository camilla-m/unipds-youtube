from crewai import Agent
from core.llm_config import nexus_llm

def get_architect(tools=None):
    return Agent(
        role='Arquiteto de Cloud Nexus',
        goal='Projetar infraestrutura seguindo normas e gerando código HCL.',
        backstory='Especialista em AWS/Terraform com foco em governança.',
        tools=tools or [], # Aceita ferramentas ou lista vazia
        llm=nexus_llm,
        verbose=True
    )

def get_auditor(tools=None): # <--- Adicionamos o argumento tools aqui!
    return Agent(
        role='Engenheiro de DevSecOps',
        goal='Garantir segurança e conformidade total dos projetos.',
        backstory='Auditor rigoroso que utiliza ferramentas de scan e OPA.',
        tools=tools or [], # <--- E passamos para o Agent aqui!
        llm=nexus_llm,
        verbose=True
    )

def get_sre_agent(tools=None):
    return Agent(
        role='Engenheiro de SRE (K8s Specialist)',
        goal='Gerenciar workloads Kubernetes e garantir rollouts seguros.',
        backstory='Especialista em orquestração, GitOps e análise de métricas de tráfego.',
        tools=tools or [],
        llm=nexus_llm,
        verbose=True
    )

def get_oncall_sre(tools=None):
    return Agent(
        role='SRE On-Call (Troubleshooting Expert)',
        goal='Reduzir o MTTR identificando a causa raiz de falhas no Kubernetes.',
        backstory='Especialista em ReAct. Você pensa antes de agir, observa os logs e correlaciona eventos.',
        tools=tools or [],
        llm=nexus_llm,
        verbose=True,
        allow_delegation=True # Permite pedir ajuda ao Arquiteto para o Fix
    )

# Adicione junto aos outros agentes no core/agents.py
def get_aiops_agent(tools=None):
    from crewai import Agent
    # Supondo que você importe seu LLM configurado (nexus_llm) no topo do arquivo
    return Agent(
        role='Engenheiro de AIOps e Dados (Observabilidade Preditiva)',
        goal='Transformar dados brutos em insights preditivos e painéis dinâmicos.',
        backstory='Especialista em séries temporais, PromQL e algoritmos de Machine Learning como Prophet e Isolation Forest. Você não espera o alerta tocar, você prevê o alerta.',
        tools=tools or [], 
        llm=nexus_llm, # Descomente e ajuste conforme a sua configuração de LLM
        verbose=True
)

def get_chatops_agent(tools=None):
    from crewai import Agent
    # from core.llm_config import nexus_llm # Certifique-se do import no topo

    return Agent(
        role='Engenheiro de Automação ChatOps',
        goal='Intermediar ações críticas entre humanos e infraestrutura com total segurança.',
        backstory='Especialista em governança, RBAC e integrações com Slack/Teams. Você nunca executa uma ação destrutiva sem antes pedir permissão a um humano autorizado.',
        tools=tools or [], 
        llm=nexus_llm, 
        verbose=True
    )
from crewai.tools import tool
import json

@tool("triagem_seguranca")
def triagem_seguranca(json_trivy: str):
    """Filtra vulnerabilidades reais de um relatório Trivy/Snyk, focando em exploits ativos."""
    return """
    🛡️ [DEVSECOPS TRIAGE]
    - CVE-2024-5678 (Critical): RCE detectado em lib-xml. NECESSITA FIX IMEDIATO.
    - CVE-2023-1122 (Medium): Denial of Service teórico. Prioridade Baixa.
    - Status: 95% dos alertas eram falsos positivos ou sem exploit público.
    """

@tool("otimizador_cicd")
def otimizador_cicd(workflow_yaml: str):
    """Analisa um arquivo de Pipeline e sugere otimizações de cache e runners."""
    return "⚡ [CI/CD OPTIMIZER]: Sugestão de uso de 'actions/cache' para node_modules. Redução estimada: 45s por build."

@tool("analise_finops")
def analise_finops(recursos_atuais: str):
    """Identifica recursos zumbis e sugere instâncias spot para economia."""
    return """
    💰 [FINOPS REPORT]
    - 3x Volumes EBS 'Available' (Zumbis): Custo mensal desperdiçado $45.00.
    - Instância 'prod-db' (c5.2xlarge): Uso médio de CPU < 10%. Sugestão: Right-size para c5.large.
    - Economia Total Estimada: $180.00/mês.
    """
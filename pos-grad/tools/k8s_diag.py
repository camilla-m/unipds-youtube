import subprocess
from crewai.tools import tool

@tool("inspect_pod_failure")
def inspect_pod_failure(pod_name: str):
    """Analisa logs e eventos de um Pod para diagnosticar CrashLoopBackOff ou OOMKilled."""
    # Simulação de diagnóstico técnico
    if "api" in pod_name:
        return """
        EVENTOS: 
        - Warning  BackOff  Back-off restarting failed container
        LOGS:
        - Error: Cannot connect to database at 10.0.1.5:5432
        DIAGNÓSTICO: Falha de conectividade (Network/Config).
        """
    if "worker" in pod_name:
        return "STATUS: Terminated | REASON: OOMKilled | MEMORY_USAGE: 512Mi (Limit: 512Mi)."
    
    return f"Logs do Pod {pod_name} parecem normais, mas o Readiness Probe está falhando."

@tool("suggest_fix")
def suggest_fix(issue_type: str):
    """Sugere a correção técnica no manifesto baseado no diagnóstico."""
    fixes = {
        "OOMKilled": "Aumentar os 'resources.limits.memory' para 1Gi no Deployment.",
        "ImagePullBackOff": "Corrigir a tag da imagem para 'latest' ou uma versão válida no ECR/DockerHub.",
        "CrashLoopBackOff": "Verificar variáveis de ambiente (DB_URL) ou segredos (Secrets) ausentes."
    }
    return fixes.get(issue_type, "Revisar a configuração do Readiness Probe no manifesto.")
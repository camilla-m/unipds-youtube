import subprocess
import os
from crewai.tools import tool

@tool("checkov_scan")
def checkov_scan(filename: str = "main.tf"):
    """Executa o scanner Checkov real no arquivo para encontrar falhas de segurança."""
    if not os.path.exists(filename):
        return f"❌ Erro: O arquivo {filename} não foi encontrado para o scan."

    try:
        # Executa o comando checkov que você instalou via pip
        # --quiet: mostra apenas os erros
        # --compact: formato mais fácil para a IA ler
        resultado = subprocess.run(
            ["checkov", "-f", filename, "--quiet", "--compact", "--no-guide"],
            capture_output=True,
            text=True
        )

        # Se o checkov encontrar erros, ele sairá com código diferente de 0
        if resultado.returncode != 0 or "FAILED" in resultado.stdout:
            return f"❌ Falhas de Segurança Detectadas pelo Checkov:\n{resultado.stdout}"
        
        return "✅ Checkov: Nenhuma vulnerabilidade detectada. O código está seguro."

    except FileNotFoundError:
        return "⚠️ Erro: Comando 'checkov' não encontrado. Rode 'pip install checkov' no terminal."
    except Exception as e:
        return f"⚠️ Erro inesperado ao rodar o scanner: {str(e)}"
        
@tool("opa_business_rules")
def opa_business_rules(content: str):
    """
    Simula o motor de decisão do OPA (Open Policy Agent).
    Valida regras de compliance da Nexus que scanners genéricos não pegam.
    """
    # 1. Regra de Negócio: Região Geográfica (Compliance de Soberania de Dados)
    if "us-east-1" not in content.lower():
        return "❌ OPA REJECTED: Violação da regra 'SOBERANIA_DADOS'. Recursos Nexus só podem residir em us-east-1."

    # 2. Regra de Negócio: Custo/Tamanho (Compliance Financeiro)
    if "t3.large" in content.lower():
        return "❌ OPA REJECTED: Violação da regra 'COST_CONTROL'. Instâncias large exigem aprovação manual do financeiro."

    # 3. Regra de Negócio: Segurança de Perímetro
    if "0.0.0.0/0" in content:
        return "❌ OPA REJECTED: Violação da regra 'NO_PUBLIC_INGRESS'. CIDR aberto não permitido."

    return "✅ OPA PASSED: O código respeita as políticas de governança da Nexus."
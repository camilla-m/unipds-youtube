from crewai.tools import tool

@tool("check_rules")
def check_rules(query: str):
    """Consulta os padrões de nomenclatura e segurança da empresa Nexus."""
    return "Padrão: Prefixo 'nexus-', Região 'us-east-1', S3 sempre privado."
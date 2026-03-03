from crewai.tools import tool

@tool("consultar_normas")
def consultar_normas(query: str):
    """Consulta os padrões de nomenclatura e segurança da empresa Nexus."""
    return "Padrão: Prefixo 'nexus-', Região 'us-east-1', S3 sempre privado."
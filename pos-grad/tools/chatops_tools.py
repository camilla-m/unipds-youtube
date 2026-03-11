from crewai.tools import tool

@tool("executar_terraform")
def executar_terraform(comando: str, senha_gestor: str = "Nenhuma"):
    """
    Ferramenta para aplicar mudanças de infraestrutura via Terraform.
    Se o comando envolver 'destruir', 'apagar' ou 'destroy', a senha_gestor DEVE ser 'GESTOR-APROVA'.
    """
    comando_lower = comando.lower()
    
    if any(palavra in comando_lower for palavra in ["destruir", "apagar", "destroy"]):
        if senha_gestor != "GESTOR-APROVA":
            return "🛑 BLOQUEADO: Ação crítica! Informe a senha_gestor correta para prosseguir."
        return "✅ APROVADO: Human-in-the-loop validado. Terraform executado com sucesso."
            
    return f"✅ SUCESSO: O comando '{comando}' foi executado (Baixo impacto)."
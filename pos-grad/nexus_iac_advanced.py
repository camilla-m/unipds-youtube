import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool

load_dotenv()

# CONFIGURAÇÃO LLM (GROQ/LLAMA 3.3)
nexus_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.1
)

# --- TOOLS DO MÓDULO 2 ---

@tool("opa_policy_validator")
def opa_policy_validator(hcl_content: str):
    """Valida o HCL contra políticas OPA (Open Policy Agent). 
    Verifica se o bucket tem criptografia e se NÃO é público."""
    # Simulação de análise Rego
    if "public" in hcl_content.lower() or "acl = \"public-read\"" in hcl_content.lower():
        return "❌ OPA REJECTED: Buckets públicos não são permitidos pela política de segurança (Rego: deny_public_buckets)."
    if "encryption" not in hcl_content.lower() and "server_side_encryption" not in hcl_content.lower():
        return "❌ OPA REJECTED: Falta bloco de criptografia (Rego: require_encryption)."
    return "✅ OPA PASSED: O código segue todas as políticas de compliance."

@tool("drift_detector")
def drift_detector(resource_name: str):
    """Compara o estado real (Cloud) com o desejado (Código). 
    Simula a descoberta de uma alteração manual no ambiente."""
    # Simulação de Drift
    return f"⚠️ DRIFT DETECTADO no {resource_name}: Alguém alterou a ACL para 'public-read' manualmente via Console AWS."

@tool("writer_tool")
def writer_tool(content: str, filename: str = "main.tf"):
    """Salva o código HCL no disco."""
    clean_content = content.replace("```hcl", "").replace("```", "").strip()
    with open(filename, "w") as f:
        f.write(clean_content)
    return f"✅ Arquivo {filename} salvo com sucesso."

# --- AGENTES ---

arquiteto_iac = Agent(
    role='Especialista em Cloud/IaC',
    goal='Traduzir requisitos em módulos Terraform seguros.',
    backstory='Você é mestre em HCL e Pulumi. Sua missão é criar código que passe no OPA.',
    tools=[writer_tool],
    llm=nexus_llm,
    verbose=True
)

auditor_compliance = Agent(
    role='Auditor de Policy-as-Code',
    goal='Validar conformidade usando OPA e detectar Drift no ambiente.',
    backstory='Você garante que a IA não gere recursos inseguros e monitora mudanças manuais.',
    tools=[opa_policy_validator, drift_detector],
    llm=nexus_llm,
    verbose=True
)

# --- TAREFAS (Aulas 2.1, 2.2 e 2.3) ---

tarefa_gerar_e_validar = Task(
    description="""(Aula 2.1 & 2.2) Gere um bucket S3 para o projeto 'Apollo'. 
    O código deve ser validado pela ferramenta OPA. Se o OPA rejeitar, você deve corrigir o código 
    até ser aprovado. No final, salve como 'main.tf'.""",
    expected_output="HCL aprovado pelo OPA e salvo em disco.",
    agent=arquiteto_iac
)

tarefa_remediar_drift = Task(
    description="""(Aula 2.3) Verifique se há drift no recurso 'nexus-apollo-s3'. 
    Se houver, sugira o código de remediação para voltar ao estado desejado.""",
    expected_output="Plano de remediação para corrigir o Drift detectado.",
    agent=auditor_compliance
)

# --- ORQUESTRAÇÃO ---
nexus_crew = Crew(
    agents=[arquiteto_iac, auditor_compliance],
    tasks=[tarefa_gerar_e_validar, tarefa_remediar_drift],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    nexus_crew.kickoff()
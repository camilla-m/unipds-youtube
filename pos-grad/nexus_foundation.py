import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM # Importamos LLM aqui
from crewai.tools import tool

# 1. CARREGAMENTO DE VARIÁVEIS
load_dotenv()

# 2. CONFIGURAÇÃO DO MODELO VIA GROQ (Atualizado para Llama 3.3)
nexus_llm = LLM(
    model="groq/llama-3.3-70b-versatile", # <--- Modelo atualizado aqui
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

# 3. IMPLEMENTAÇÃO DE RAG (Aula 1.3)
@tool("consultar_normas_sre")
def consultar_normas_sre(query: str):
    """Consulta os padrões de nomenclatura e segurança da empresa Nexus."""
    normas = {
        "nomenclatura": "Todos os recursos devem prefixar com 'nexus-' e sufixar com '-prod' ou '-dev'.",
        "segurança": "Buckets S3 nunca devem ser públicos. Devem ter versionamento ativo.",
        "região": "Todos os recursos devem ser deployados em us-east-1 (N. Virginia)."
    }
    
    query_lower = query.lower()
    if "nome" in query_lower or "padrão" in query_lower:
        return normas["nomenclatura"]
    if "segurança" in query_lower or "público" in query_lower:
        return normas["segurança"]
    
    return "Regra geral: Siga o Least Privilege e use a região us-east-1."

# 4. DEFINIÇÃO DOS AGENTES
arquiteto = Agent(
    role='Arquiteto de Cloud Nexus',
    goal='Projetar infraestrutura seguindo rigorosamente as normas da empresa.',
    backstory='Você é um arquiteto sênior focado em governança.',
    tools=[consultar_normas_sre],
    llm=nexus_llm, # <--- Usando o objeto LLM novo
    verbose=True,
    allow_delegation=False
)

revisor_seguranca = Agent(
    role='Engenheiro de DevSecOps',
    goal='Validar se o projeto do arquiteto está seguro e padronizado.',
    backstory='Você é um auditor de segurança rigoroso.',
    llm=nexus_llm, # <--- Usando o objeto LLM novo
    verbose=True,
    allow_delegation=False
)

# 5. DEFINIÇÃO DAS TAREFAS
tarefa_desenho = Task(
    description="Projete um bucket S3 para os logs do projeto Apollo usando as normas da Nexus.",
    expected_output="Um resumo contendo: Nome do Bucket, Região e Status de Segurança.",
    agent=arquiteto
)

tarefa_revisao = Task(
    description="Revise se o projeto Apollo segue o padrão de nomenclatura e segurança.",
    expected_output="Veredito final: APROVADO ou REPROVADO.",
    agent=revisor_seguranca
)

# 6. ORQUESTRAÇÃO
nexus_crew = Crew(
    agents=[arquiteto, revisor_seguranca],
    tasks=[tarefa_desenho, tarefa_revisao],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("\n🚀 EXECUTANDO MÓDULO 1: FUNDAÇÃO NEXUS (MODO GROQ NATIVO)\n")
    try:
        # Importante: No seu .env, você pode até APAGAR a OPENAI_API_KEY agora
        resultado = nexus_crew.kickoff() 
        print("\n✅ RESULTADO FINAL:\n")
        print(resultado)
    except Exception as e:
        print(f"\n❌ Erro na execução: {e}")
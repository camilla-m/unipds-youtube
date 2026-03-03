import os
import subprocess
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool

# 1. SETUP AMBIENTE
load_dotenv()

# Configuração da Groq (Llama 3.3)
nexus_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.1
)

# 2. FERRAMENTA: ESCRITA DE ARQUIVO (Módulo 2.2)
@tool("escritor_de_arquivo")
def escritor_de_arquivo(conteudo: str, nome_arquivo: str = "main.tf"):
    """Útil para salvar código Terraform no disco local."""
    try:
        # Limpa blocos de markdown que a IA costuma enviar
        codigo_limpo = conteudo.replace("```hcl", "").replace("```", "").strip()
        with open(nome_arquivo, "w") as f:
            f.write(codigo_limpo)
        return f"✅ Arquivo {nome_arquivo} salvo com sucesso!"
    except Exception as e:
        return f"❌ Erro ao salvar: {str(e)}"

# 3. FERRAMENTA: SCAN DE SEGURANÇA (Módulo 2.3)
@tool("scanner_de_seguranca")
def scanner_de_seguranca(nome_arquivo: str = "main.tf"):
    """Roda o Checkov no arquivo gerado para encontrar falhas de segurança."""
    try:
        # Executa o checkov via subprocesso
        resultado = subprocess.run(
            ["checkov", "-f", nome_arquivo, "--quiet", "--no-guide"],
            capture_output=True, text=True
        )
        if "Passed checks: 0" in resultado.stdout or "FAILED" in resultado.stdout:
            return f"⚠️ Vulnerabilidades encontradas:\n{resultado.stdout}"
        return "✅ Código validado! Nenhuma falha crítica de segurança encontrada."
    except Exception as e:
        return f"⚠️ Erro ao rodar scanner (Certifique-se que o checkov está instalado): {str(e)}"

# 4. AGENTES
arquiteto_iac = Agent(
    role='Arquiteto Terraform',
    goal='Gerar código HCL limpo e salvar no disco.',
    backstory='Especialista em automação AWS. Você entende requisitos e cria arquivos main.tf.',
    tools=[escritor_de_arquivo],
    llm=nexus_llm,
    verbose=True
)

auditor_seguranca = Agent(
    role='Auditor de DevSecOps',
    goal='Validar a segurança do arquivo gerado e sugerir melhorias.',
    backstory='Você é rigoroso. Sua missão é garantir que o Checkov não aponte erros.',
    tools=[scanner_de_seguranca],
    llm=nexus_llm,
    verbose=True
)

# 5. TAREFAS
tarefa_geracao = Task(
    description="""Crie um código Terraform para um bucket S3 chamado 'nexus-production-data'. 
    Habilite o versionamento e salve o código no arquivo 'main.tf' usando a ferramenta.""",
    expected_output="Código gerado e salvo no arquivo.",
    agent=arquiteto_iac
)

tarefa_auditoria = Task(
    description="""Analise o arquivo 'main.tf' usando o scanner_de_seguranca. 
    Se houver falhas (ex: falta de criptografia), peça para o Arquiteto corrigir.""",
    expected_output="Relatório final de conformidade.",
    agent=auditor_seguranca
)

# 6. CREW
nexus_iac_crew = Crew(
    agents=[arquiteto_iac, auditor_seguranca],
    tasks=[tarefa_geracao, tarefa_auditoria],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("\n🚀 INICIANDO MÓDULO 2: IAC COPILOT\n")
    nexus_iac_crew.kickoff()
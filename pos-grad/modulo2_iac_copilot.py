import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from crewai import Task, Crew, Process
from core.agents import get_arquiteto, get_auditor
from tools.file_writer import writer_tool
from tools.security_scan import checkov_scan, opa_business_rules

arquiteto = get_arquiteto(tools=[writer_tool])
auditor = get_auditor(tools=[checkov_scan, opa_business_rules])

task_gerar = Task(
    description="Gere um arquivo 'main.tf' para um bucket S3 seguro chamado 'nexus-apollo-data'. Região deve ser us-west-2.",
    expected_output="Arquivo main.tf gerado com sucesso.",
    agent=arquiteto
)

task_auditar = Task(
    description="Valide o 'main.tf' usando checkov e OPA. Se houver erro, o arquiteto deve corrigir.",
    expected_output="Relatório de conformidade final.",
    agent=auditor
)

nexus_pipeline = Crew(
    agents=[arquiteto, auditor],
    tasks=[task_gerar, task_auditar],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("\n🚀 EXECUTANDO PIPELINE MODULAR\n")
    nexus_pipeline.kickoff()
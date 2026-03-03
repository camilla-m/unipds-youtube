from crewai import Task, Crew
from core.agents import get_arquiteto
from tools.policy_rag import consultar_normas

arquiteto = get_arquiteto(tools=[consultar_normas])

task = Task(
    description="Desenhe um bucket S3 para logs seguindo as normas da empresa.",
    expected_output="Plano detalhado com nome e região.",
    agent=arquiteto
)

Crew(agents=[arquiteto], tasks=[task]).kickoff()
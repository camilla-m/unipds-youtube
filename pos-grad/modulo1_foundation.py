from crewai import Task, Crew
from core.agents import get_architect
from tools.policy_rag import check_rules

architect = get_architect(tools=[check_rules])

task = Task(
    description="Desenhe um bucket S3 para logs seguindo as normas da empresa.",
    expected_output="Plano detalhado com nome e região.",
    agent=architect
)

Crew(agents=[architect], tasks=[task]).kickoff()
import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

# Centraliza a inteligência do projeto
nexus_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)
# Módulo 1: Fundamentos e Arquitetura de IA para Infra

Este módulo estabelece a base conceitual e técnica para a utilização de Modelos de Linguagem de Grande Escala (LLMs) em fluxos de trabalho DevOps e Engenharia de Plataforma.

## 🎓 Conteúdo Programático

### 1.1 LLMs e APIs no Contexto DevOps
Nesta aula, exploramos a transição do processamento de linguagem natural (NLP) para a geração de código de infraestrutura.
- **Arquitetura de Transformers:** Como o mecanismo de *Self-Attention* permite que a IA entenda dependências em arquivos YAML e HCL.
- **Ecossistema de APIs:** - **GPT-4o:** O estado da arte para raciocínio e *Function Calling*.
  - **Claude 3.5 Sonnet:** Líder atual em geração de código limpo e seguimento de instruções complexas.
  - **AWS Bedrock:** A escolha para ambientes empresariais que exigem isolamento de dados e compliance.

### 1.2 Frameworks de Agentes (LangChain & CrewAI)
Diferenciamos o "Chat" (interação manual) do "Agente" (automação autônoma).
- **Abstração de Ferramentas (Tools):** Como encapsular scripts CLI e APIs de Cloud para que a LLM possa "executar" ações.
- **Orquestração Multi-Agente:** O uso do CrewAI para definir papéis (Roles), metas (Goals) e backstories, permitindo que IAs colaborem como um time de SRE.

### 1.3 RAG e Prompting Estruturado
Como garantir precisão técnica e evitar alucinações.
- **RAG (Retrieval-Augmented Generation):** Técnica de injetar contextos externos (documentação técnica, segredos de infra, runbooks) no prompt da LLM.
- **Chain-of-Thought (CoT):** Técnica de prompting que força o modelo a descrever seu raciocínio passo a passo antes de sugerir um comando `kubectl` ou `terraform`.
- **Few-Shot:** Ensinar padrões de nomenclatura da empresa através de exemplos práticos no prompt.

---

## 🛠️ Laboratório Prático: Nexus Foundation

O script `nexus_foundation.py` demonstra a integração de todos os conceitos acima:
1. **Conexão via API** com GPT-4.
2. **Uso de Tools** para simular uma consulta de RAG em políticas corporativas.
3. **Fluxo Sequencial** entre um Arquiteto e um Engenheiro de Segurança.

### Como Executar
1. Instale as dependências:
   ```bash
   pip install crewai langchain-openai python-dotenv
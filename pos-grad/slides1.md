---
marp: true
theme: uncover
class: invert
paginate: true
backgroundColor: #0d1117
color: #e6edf3
style: |
  section { text-align: left; font-size: 22px; }
  h1 { color: #58a6ff; font-size: 40px; }
  h2 { color: #79c0ff; font-size: 30px; }
  code { background-color: #161b22; color: #ff7b72; }
  b { color: #d2a8ff; }

---

# Módulo 1: Fundamentos e Arquitetura de IA para Infra
## A Revolução da IA Agêntica no Ciclo DevOps
**Professora:** Camilla Martins
**Tecnologias:** CrewAI, Groq (Llama 3.3), RAG e Python 3.13

---

# 1.1 LLMs e o Contexto DevOps
### Por que não usar apenas o Chat comum?

- **O Desafio da Alucinação:** LLMs padrão tendem a "chutar" nomes de recursos e sintaxes de versões antigas de provedores de Cloud.
- **Arquitetura de Transformers:** O mecanismo de **Self-Attention** permite que o modelo entenda a hierarquia de um YAML. Se você define um `Service` no K8s, a IA entende a relação com o `Selector` do `Deployment`.
- **Diferença entre Modelos:**
  - **Modelos Proprietários (OpenAI/Claude):** Excelentes em raciocínio, mas possuem custos de API e latência variável.
  - **Modelos de Alta Performance (Llama 3.3 via Groq):** Permitem automações em tempo real devido à velocidade de inferência (Tokens por segundo).

---

# 1.2 Anatomia de um Agente de IA
### Saindo da Resposta Passiva para a Ação Ativa

Um **Agente** no CrewAI é composto por quatro pilares fundamentais:

1. **Role (Papel):** Define o escopo de atuação (ex: SRE, Arquiteto).
2. **Goal (Objetivo):** O resultado esperado que o agente deve perseguir.
3. **Backstory (Histórico):** Dá o tom e a experiência ao agente, influenciando como ele prioriza decisões (ex: "Você prioriza segurança sobre custo").
4. **Tools (Ferramentas):** Funções Python que permitem à IA sair do mundo das palavras e interagir com o sistema (Ler arquivos, executar CLI, consultar APIs).

---

# 1.3 Frameworks de Orquestração: CrewAI
### Por que usar CrewAI em vez de scripts simples?

- **Sistemas Multi-Agente:** Permite que diferentes "especialistas" colaborem. Um arquiteto desenha, um engenheiro de segurança revisa.
- **Processos (Workflows):**
  - **Sequential:** Uma tarefa depende da conclusão da outra (Ideal para CI/CD).
  - **Hierarchical:** Um gerente coordena a execução dos agentes.
- **Auto-Correction:** Se um agente falha ao executar uma ferramenta (ex: erro de sintaxe no Terraform), ele pode tentar se corrigir antes de entregar o resultado final.

---

# 1.4 RAG: Retrieval-Augmented Generation
### Conectando a IA aos Dados Privados da Empresa

- **O que é:** Técnica de fornecer contexto externo à LLM no momento da pergunta.
- **Por que no DevOps?**
  - IA não conhece sua **VPC ID**.
  - IA não conhece seu **Padrão de Nomenclatura**.
  - IA não conhece seus **Runbooks de Incidente**.
- **O Fluxo:**
  1. Pergunta do Usuário -> 2. Busca em Base de Conhecimento (Docs/Tools) -> 3. Prompt Enriquecido -> 4. Resposta Precisa.

---

# 1.5 Padrões de Prompting para Infraestrutura
### Técnicas para Garantir Estabilidade

- **Few-Shot Prompting:** Enviar exemplos de "Input -> Output" para que a IA siga o padrão da empresa.
- **Chain-of-Thought (CoT):** Instruir a IA a "explicar seu raciocínio" antes de gerar o código final. Isso reduz erros lógicos em 40%.
- **Negative Prompts:** Definir o que a IA **NÃO** deve fazer (ex: "Nunca use senhas em texto claro", "Nunca gere buckets públicos").

---

# 🛠️ Laboratório: O Ecossistema Nexus
### O que construímos no Módulo 1?

- **Engine:** Configuração da Groq com Llama 3.3 via LiteLLM.
- **Tool de Normas:** Uma função Python que simula um banco de dados de governança.
- **O Fluxo Agêntico:**
  - **Arquiteto:** Pensa -> Consulta Normas -> Projeta Recurso.
  - **DevSecOps:** Recebe Projeto -> Valida contra Normas -> Emite Veredito.
- **O Resultado:** Uma resposta estruturada que garante que a infraestrutura nasce "compliance".

---

# 🎯 Conclusão do Módulo
- IA em DevOps não é sobre chat, é sobre **Agentes**.
- Ferramentas (Tools) são as mãos da IA.
- RAG é o cérebro que conhece o SEU ambiente.

**Próximo Módulo:** Geração de arquivos físicos e Validação com ferramentas de Segurança (Checkov).
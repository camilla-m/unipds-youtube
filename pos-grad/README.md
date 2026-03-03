# Módulo 1: Fundamentos e Arquitetura de IA para Infraestrutura

Este módulo estabelece a base técnica para a utilização de Modelos de Linguagem de Grande Escala (LLMs) aplicados à Engenharia de Plataforma e DevOps, focando na transição de chatbots passivos para **Agentes Autônomos**.

## 🎯 Objetivos de Aprendizado
- Compreender a arquitetura de **Transformers** e sua aplicação em linguagens de infraestrutura (HCL/YAML).
- Configurar ambientes de execução de IA utilizando **Python 3.13** e **Groq**.
- Implementar fluxos agênticos multi-agentes com **CrewAI**.
- Aplicar conceitos de **RAG (Retrieval-Augmented Generation)** para governança de dados.

---

## 🏗️ Arquitetura do Sistema (Nexus Foundation)

O laboratório deste módulo implementa um sistema de decisão em dois níveis:
1. **Agente Arquiteto:** Responsável por interpretar a necessidade de negócio e consultar as normas técnicas via **Custom Tools**.
2. **Agente DevSecOps:** Atua como um *Quality Gate*, revisando as proposições do arquiteto antes da finalização.

### Stack Tecnológica
- **Linguagem:** Python 3.13+
- **Orquestrador:** CrewAI
- **LLM:** Llama 3.3-70b (via Groq Cloud)
- **Interface de API:** LiteLLM (Ponte de conectividade)

---

## 🛠️ Configuração do Ambiente

### 1. Requisitos de Sistema
Certifique-se de ter o Python instalado e crie um ambiente virtual para evitar conflitos de dependências:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalação de Dependências
Instale as versões validadas para este módulo:

```bash
pip install python-dotenv crewai==0.28.8 langchain-groq litellm
```

### 3. Variáveis de Ambiente (.env)
Crie um arquivo .env na raiz do projeto com suas chaves de API.
Nota: Devido a restrições de inicialização do CrewAI, uma chave placeholder da OpenAI é necessária mesmo utilizando Groq.

```bash
GROQ_API_KEY=gsk_your_key_here
OPENAI_API_KEY=sk-placeholder
```

### 🚀 Execução do Laboratório
O script principal (nexus_foundation.py) demonstra o conceito de RAG Funcional. O agente não possui conhecimento prévio das normas da empresa "Nexus", ele é forçado a utilizar uma ferramenta (tool) para buscar essas informações antes de responder.

Para rodar o laboratório:

```bash
python3 nexus_foundation.py
```

### O que observar no output:

- Thought Process: Acompanhe o raciocínio da IA decidindo usar a ferramenta de normas.
- Tool Output: Veja a extração dos prefixos nexus- e sufixos -prod em tempo real.
- Final Verdict: A revisão de segurança validando se o plano está em conformidade.

### 📚 Conceitos-Chave para Revisão

- Agentic Workflow: A IA deixa de ser um oráculo e passa a ser um colaborador que executa funções.
- Chain-of-Thought: Técnica de prompting que estruturamos nas Tasks para garantir que a IA explique o plano antes de sugerir comandos críticos.
- Tokenização: Como a infraestrutura é "quebrada" em pedaços lógicos para processamento da LLM.

---

### 💡 Dica para a Professora:
Se você for disponibilizar esse código no GitHub ou em um portal do aluno, adicione um arquivo `.gitignore` simples para garantir que ninguém suba as chaves de API:

```text
.env
venv/
__pycache__/
*.tfstate
*.tfvars
```
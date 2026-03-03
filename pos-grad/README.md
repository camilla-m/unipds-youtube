# Módulo 1: Fundamentos e Arquitetura de IA para Infraestrutura

Este módulo estabelece a base técnica para a utilização de Modelos de Linguagem de Grande Escala (LLMs) aplicados à Engenharia de Plataforma e DevOps, focando na transição de chatbots passivos para **Agentes Autônomos**.

## 🎯 Objetivos de Aprendizado

- Compreender a arquitetura de **Transformers** e sua aplicação em linguagens de infraestrutura (HCL/YAML)
- Configurar ambientes de execução de IA utilizando **Python 3.13** e **Groq**
- Implementar fluxos agênticos multi-agentes com **CrewAI**
- Aplicar conceitos de **RAG (Retrieval-Augmented Generation)** para governança de dados

---

## 🏗️ Arquitetura do Sistema (Nexus Foundation)

O laboratório deste módulo implementa um sistema de decisão em dois níveis:

1. **Agente Arquiteto:** Responsável por interpretar a necessidade de negócio e consultar as normas técnicas via **Custom Tools**
2. **Agente DevSecOps:** Atua como um *Quality Gate*, revisando as proposições do arquiteto antes da finalização

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

Crie um arquivo `.env` na raiz do projeto com suas chaves de API.

**Nota:** Devido a restrições de inicialização do CrewAI, uma chave placeholder da OpenAI é necessária mesmo utilizando Groq.

```bash
GROQ_API_KEY=gsk_your_key_here
OPENAI_API_KEY=sk-placeholder
```

### 4. Configuração de Perfil AWS (Opcional)

Se você for trabalhar com recursos AWS (Módulo 2), configure suas credenciais:

```bash
# Instalar AWS CLI (se ainda não tiver)
brew install awscli  # macOS
# ou
pip install awscli

# Configurar um novo perfil
aws configure --profile nexus-dev

# Será solicitado:
# AWS Access Key ID: sua_access_key
# AWS Secret Access Key: sua_secret_key
# Default region name: us-east-1
# Default output format: json
```

Para usar o perfil no Terraform, adicione ao arquivo `.env`:

```bash
AWS_PROFILE=nexus-dev
# ou diretamente nas variáveis de ambiente
export AWS_PROFILE=nexus-dev
```

**Verificar credenciais:**

```bash
aws sts get-caller-identity --profile nexus-dev
```

---

## 🚀 Execução do Laboratório

O script principal (`nexus_foundation.py`) demonstra o conceito de RAG Funcional. O agente não possui conhecimento prévio das normas da empresa "Nexus", ele é forçado a utilizar uma ferramenta (tool) para buscar essas informações antes de responder.

Para rodar o laboratório:

```bash
python3 nexus_foundation.py
```

### O que observar no output:

- **Thought Process:** Acompanhe o raciocínio da IA decidindo usar a ferramenta de normas
- **Tool Output:** Veja a extração dos prefixos `nexus-` e sufixos `-prod` em tempo real
- **Final Verdict:** A revisão de segurança validando se o plano está em conformidade

---

## 📚 Conceitos-Chave para Revisão

- **Agentic Workflow:** A IA deixa de ser um oráculo e passa a ser um colaborador que executa funções
- **Chain-of-Thought:** Técnica de prompting que estruturamos nas Tasks para garantir que a IA explique o plano antes de sugerir comandos críticos
- **Tokenização:** Como a infraestrutura é "quebrada" em pedaços lógicos para processamento da LLM

---

# Módulo 2: IaC Copilot — Automação, Compliance e Self-Healing

Neste módulo, evoluímos a Inteligência Artificial de uma interface de chat para um **Motor de Execução de Infraestrutura**. O foco é a materialização de ativos de nuvem (Terraform) e a implementação de camadas de segurança programática.

## 🎯 Objetivos Técnicos
- **Infrastructure-as-Code Synthesis:** Tradução de requisitos de alto nível para HCL (HashiCorp Configuration Language).
- **Static Code Analysis (SCA):** Integração profunda com **Checkov** para detecção de misconfigurations.
- **Policy-as-Code (PaC):** Validação de regras de negócio via **OPA (Open Policy Agent)**.
- **Drift Management:** Identificação de divergências entre o estado real da nuvem e o código versionado.

---

## 🏗️ Arquitetura do Pipeline Agêntico

O ecossistema deste módulo é composto por um fluxo de **Feedback Loop Fechado**, onde a IA atua como desenvolvedora e auditora simultaneamente.

### 1. Camada de Geração (`nexus_iac_copilot.py`)
Utiliza o Agente **Arquiteto Terraform** para:
- Interpretar prompts em linguagem natural.
- Mapear requisitos para provedores específicos (AWS/GCP/Azure).
- Executar a `writer_tool` para persistir o código em arquivos `.tf`.

### 2. Camada de Governança (`nexus_iac_advanced.py`)
Implementa o Agente **Auditor de DevSecOps**, que possui duas "visões" críticas:
- **Visão Técnica (Checkov):** Escaneia o arquivo gerado em busca de vulnerabilidades (ex: S3 público, criptografia desativada, falta de logs).
- **Visão de Negócio (OPA):** Valida se o recurso segue as políticas da Nexus (ex: Regiões permitidas, tags obrigatórias).

### 3. Camada de Remediação (Self-Healing)
Se qualquer auditor reprovar o código, o erro é injetado novamente no contexto do Arquiteto. A IA realiza a **refatoração autônoma** até que o código atinja o estado de compliance total.

---

## 🛠️ Configuração e Pré-requisitos

### Instalação de Dependências
Além do CrewAI e Groq, este módulo exige ferramentas de análise estática:

```bash
# Instalação do Scanner de IaC
pip install checkov

# Instalação das dependências de orquestração
pip install litellm langchain-groq python-dotenv
```

Sugerimos que você pode instalar o checkov como binário também na sua máquina!


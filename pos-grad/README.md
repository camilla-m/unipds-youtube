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

# Módulo 2: IaC Copilot - Automação e Governança de Infraestrutura

Após compreendermos os fundamentos das LLMs e a orquestração de agentes no Módulo 1, entramos na fase de **implementação física**. No Módulo 2, transformamos a "conversa" em ativos de engenharia reais.

## 🎯 Objetivos de Aprendizado

- Implementar **Custom Tools** para interação com o Sistema de Arquivos (OS)
- Automatizar a geração de **Terraform HCL** com foco em modularidade
- Integrar scanners de segurança (**Checkov**) no fluxo agêntico
- Criar um loop de **Self-Healing IaC**: Detecção de falhas de segurança e correção automática pela IA

---

## 🛠️ O Ecossistema de Automação

Diferente do módulo anterior, aqui o Agente Arquiteto recebe capacidades de escrita. O fluxo segue o padrão **PR-First assistido**:

1. **Input:** "Preciso de um ambiente de storage para produção"
2. **Brainstorming:** O agente decide a melhor arquitetura
3. **Action:** O agente chama a `escritor_de_arquivo` e gera o `main.tf`
4. **Validation:** O Agente Auditor executa o `Checkov` e lê o output
5. **Feedback Loop:** Se houver falhas de segurança (ex: bucket sem criptografia), o Auditor devolve o erro para o Arquiteto, que reescreve o código até que ele passe no scan

---

## 🧰 Ferramentas Adicionais

Além das bibliotecas de IA, este módulo exige:

- **Checkov:** Scanner de Infraestrutura como Código
- **Terraform CLI:** Para validação de sintaxe

```bash
pip install checkov
```

---

## 🚀 Execução do Laboratório

Para validar o fluxo de Automação e Governança, execute o script principal:

```bash
python3 nexus_iac_copilot.py
```

### O que acontece durante a execução:

- **Geração:** O Agente Arquiteto criará um plano HCL
- **Persistência:** O arquivo `main.tf` será criado fisicamente na sua pasta
- **Auditoria:** O Agente Auditor invocará o Checkov via subprocesso Python
- **Ciclo de Correção:** Caso o Checkov encontre falhas (ex: `CKV_AWS_144` - falta de criptografia em repouso), o Auditor enviará o log de erro de volta para o Arquiteto. O Arquiteto irá refatorar o código e salvar novamente até que o scan retorne `PASSED`

---

## ⚠️ Pontos de Atenção

- **Permissões de Escrita:** Certifique-se de que o script tem permissão para criar arquivos na pasta atual
- **Versão do Terraform:** O código gerado é compatível com Terraform 1.0+
- **Instalação do Checkov:** Caso o comando `checkov` não seja encontrado, certifique-se de que o diretório de scripts do Python está no seu PATH (comum em macOS com Python 3.13)

---

## 📚 Conclusão do Módulo

Ao final deste laboratório, você terá implementado um pipeline de Compliance-as-Code movido a IA, onde a inteligência não apenas sugere, mas executa e garante a segurança da infraestrutura antes mesmo do `terraform apply`.

---
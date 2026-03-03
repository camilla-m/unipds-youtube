# 🚀 Nexus AI-Ops Framework

**Engenharia de Plataforma e SRE assistida por IA agêntica**

O **Nexus AI-Ops** é um ecossistema modular desenvolvido para demonstrar a aplicação de agentes de IA no ciclo de vida de operações de TI (DevOps & SRE). O projeto evolui de uma fundação de consulta (RAG) para a automação de infraestrutura (IaC), orquestração de containers (Kubernetes) e resolução de incidentes (Troubleshooting).

---

## 🏗️ Arquitetura do Projeto

O repositório separa a **Inteligência (Agentes)** das **Capacidades de Execução (Tools)**.

### `core/` — o cérebro

- **`llm_config.py`**: configuração de conexão com Llama 3.3 via Groq/LiteLLM.
- **`agents.py`**: personas (Arquiteto Cloud, Auditor, SRE e On-Call).

### `tools/` — as mãos

- **`policy_rag.py`** (Mod 1): consulta de normas e documentação.
- **`file_writer.py`** (Mod 2): persistência de arquivos de infraestrutura.
- **`security_scan.py`** (Mod 2): integração com Checkov e OPA.
- **`k8s_ops.py`** (Mod 3): manifestos K8s, reconciliação GitOps e canary.
- **`k8s_diag.py`** (Mod 4): diagnóstico de Pods (logs, eventos, describe).
- **`obs_tools.py`** (Mod 4): consultas simuladas em Prometheus e Jaeger.

### `labs/`

Scripts de entrada de cada módulo (`modulo1_*.py` a `modulo4_*.py`).

---

## 🎓 Trilha de Aprendizado (Ementa Completa)

### 🟢 Módulo 1 — Fundação e RAG

- **Aula 1.1:** Arquitetura de Transformers aplicada a código e comparativo de modelos.
- **Aula 1.2:** Frameworks de agentes (LangChain e CrewAI).
- **Aula 1.3:** Implementação de RAG e padrões de Chain-of-Thought para evitar alucinações.

### 🔵 Módulo 2 — IaC Copilot (Terraform e Cloud)

- **Aula 2.1:** Tradução de linguagem natural para HCL (Terraform).
- **Aula 2.2:** Compliance-as-Code: integração com Checkov e OPA.
- **Aula 2.3:** Detecção de drift e planos de remediação.

### 🟡 Módulo 3 — Kubernetes AI-Ops

- **Aula 3.1:** Manifestos e Autoscaling: geração de YAMLs (Deployments/Services).
- **Aula 3.2:** Estratégias de Rollout: IA como tomadora de decisão em Canary Deployments.
- **Aula 3.3:** GitOps Inteligente: reconciliação assistida (Argo CD / Flux).

### 🔴 Módulo 4 — Troubleshooting e Diagnóstico (ReAct)

- **Aula 4.1:** Framework **ReAct**: ensinando a IA a "pensar, agir e observar".
- **Aula 4.2:** Depuração de Pods: diagnóstico de CrashLoopBackOff e OOMKilled.
- **Aula 4.3:** Observabilidade: correlação de traces em Jaeger e métricas em Prometheus.

**Prática:** script de "Self-Healing" que identifica falhas e sugere correções no código.

---

## 🚀 Guia de Execução (passo a passo)

### 1) Preparação do ambiente

```bash
# Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# Instalar dependências e scanner Checkov
pip install -r requirements.txt
pip install checkov
```

### 2) Configuração de credenciais

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
OPENAI_API_KEY=sk-placeholder
```

### 3) Executar laboratórios

Sempre execute a partir da raiz do projeto:

```bash
# Módulo 1 (Fundação)
python3 modulo1_foundation.py

# Módulo 2 (IaC/Segurança)
python3 modulo2_iac_copilot.py

# Módulo 3 (Kubernetes)
python3 modulo3_k8s_ops.py

# Módulo 4 (Incidentes/ReAct)
python3 modulo4_troubleshooting.py
```

---

## 🛠️ Troubleshooting

- **ImportError:** execute os comandos na raiz da pasta principal (`/pos-grad/`), não em subpastas.
- **Checkov Fail (Mod 2):** valide a instalação com:

```bash
pip show checkov
```

- **Simulações (Mods 3 e 4):** operações destrutivas ou dependentes de clusters reais (Argo CD, Prometheus) usam mocks em Python para focar no fluxo lógico da IA.

---

## ✅ Status

**Módulos 1, 2, 3 e 4 finalizados e integrados.**

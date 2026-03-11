# 🚀 Nexus AI-Ops: Trilha de Engenharia Agêntica

Este repositório contém os laboratórios práticos da Pós-Graduação em AI-Ops e Engenharia de Plataforma. O projeto evolui de uma base de conhecimento (RAG) até a criação de agentes que operam infraestrutura real com governança.

## 🛠️ 1. Preparação do Terreno

### Pré-requisitos

- Python 3.10 a 3.13
	- Evite Python 3.14 experimental para garantir compatibilidade com CrewAI.
- Docker e `kubectl` instalados
	- Necessários para os módulos 3 e 4.
- Uma chave de API da Groq
	- Llama 3.3 é o motor utilizado no projeto.

### Instalação

```bash
# Clone o repositório e entre na pasta
git clone https://github.com/seu-usuario/nexus-ai-ops.git
cd nexus-ai-ops

# Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
pip install streamlit
```

### Instalação no Windows

Use **PowerShell** ou **Prompt de Comando**.

#### PowerShell

```powershell
# Clone o repositório e entre na pasta
git clone https://github.com/seu-usuario/nexus-ai-ops.git
cd nexus-ai-ops

# Crie o ambiente virtual
py -3.11 -m venv venv

# Ative o ambiente virtual
.\venv\Scripts\Activate.ps1

# Instale as dependências
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install streamlit
```

Se o PowerShell bloquear a ativação do ambiente virtual, execute:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

#### Prompt de Comando (CMD)

```bat
git clone https://github.com/seu-usuario/nexus-ai-ops.git
cd nexus-ai-ops

py -3.11 -m venv venv
venv\Scripts\activate.bat

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install streamlit
```

### Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
OPENAI_API_KEY=sk-placeholder
```

> `OPENAI_API_KEY` pode ser usada apenas como placeholder para evitar erros de inicialização do CrewAI, dependendo da configuração local.

## 🎓 2. Guia de Execução dos Laboratórios

### 🟢 Módulo 1 & 2: IA Consultiva e IaC

**Cenário:** validar normas internas e gerar código Terraform seguro.

```bash
# Rodar diagnóstico de arquitetura e segurança Cloud
python3 labs/modulo2_iac_copilot.py
```

### 🟡 Módulo 3: Kubernetes Ops

**Cenário:** criar manifestos K8s blindados.

```bash
# Geração de YAMLs e estratégia de rollout
python3 labs/modulo3_k8s_ops.py
```

### 🔴 Módulo 4: Troubleshooting (Self-Healing)

**Cenário:** recuperar um serviço quebrado no cluster.

```bash
# 1. Simular o erro (Pod entra em CrashLoop)
kubectl apply -f checkout-broken.yaml

# 2. Chamar o Agente SRE para diagnosticar e curar
python3 labs/modulo4_troubleshooting.py

# 3. Aplicar a cura
kubectl apply -f checkout-k8s-fix.yaml
```

### 🟣 Módulo 5: AIOps Preditivo

**Cenário:** prever saturação de disco 4h antes de acontecer.

```bash
# Gerar alerta preditivo e dashboard do Grafana
python3 labs/modulo5_aiops.py
```

### 💬 Módulo 6: ChatOps e Governança (Simulador)

**Cenário:** interagir com a infraestrutura via chat com aprovação do gestor.

```bash
# Iniciar o simulador de Slack no navegador
./venv/bin/python3 -m streamlit run labs/modulo6_chatops.py
```

No chat, tente: **@nexus-bot destrua o banco**. O sistema pedirá a senha: **GESTOR-APROVA**.

## 🛠️ Solução de Problemas

### Erro `ModuleNotFoundError: crewai`

Certifique-se de que as dependências foram instaladas e que o ambiente virtual está ativo.

### Erro de versão do Python (3.14)

Se estiver no macOS e o comando `python3` apontar para 3.14, use o interpretador do ambiente virtual:

```bash
./venv/bin/python3
```

No Windows, prefira usar:

```powershell
py -3.11
```

ou o Python do ambiente virtual:

```powershell
.\venv\Scripts\python.exe
```

### `ImportError` em `tools`

Sempre execute os scripts a partir da raiz do projeto, nunca de dentro da pasta `labs`.
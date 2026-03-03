---
marp: true
theme: uncover
class: invert
paginate: true
backgroundColor: #0d1117
color: #e6edf3
style: |
  section { text-align: left; font-size: 20px; }
  h1 { color: #00ff88; font-size: 38px; border-bottom: 2px solid #00ff88; }
  h2 { color: #00d4ff; font-size: 28px; }
  code { background-color: #1a1f29; color: #ffca28; }
  b { color: #00ff88; }

---

# Módulo 2: IaC Copilot & Advanced Governance
## Do Código à Governança com Checkov e OPA
**Professora:** Camilla Martins
**Tecnologias:** Terraform, Checkov, OPA, CrewAI.

---

# 2.1 Aula: O Copilot de Infraestrutura
### De Requisitos a Arquivos Físicos

- **Evolução do Agente:** A IA deixa de apenas sugerir código e passa a gerenciar o sistema de arquivos via `writer_tool`.
- **Tradução HCL:** Como mapear "Ambiente de Produção" para argumentos de segurança robustos no Terraform.
- **Workflow:** Entrada em Linguagem Natural -> Processamento Agêntico -> Arquivo `main.tf` persistido.

---

# 2.2 Aula: Security Scan com Checkov
### Static Code Analysis (SCA) movido a IA

- **O que é o Checkov?** Ferramenta líder para escanear falhas de segurança em IaC.
- **Integração Agêntica:** O Agente Auditor executa o Checkov e "lê" o relatório de erros.
- **Loop de Self-Healing:** Se o Checkov reprova o código (ex: falta de criptografia no S3), a IA refatora o arquivo automaticamente até que o scan passe com sucesso.

---
marp: true
theme: uncover
class: invert
paginate: true
backgroundColor: #0d1117
color: #e6edf3
style: |
  section { text-align: left; font-size: 20px; }
  h1 { color: #00ff88; font-size: 38px; border-bottom: 2px solid #00ff88; }
  h2 { color: #00d4ff; font-size: 28px; }
  code { background-color: #1a1f29; color: #ffca28; }
  b { color: #00ff88; }

---

# Módulo 2: IaC Copilot & Advanced Governance
## Do Código à Governança com Checkov e OPA
**Professora:** Camilla Martins
**Tecnologias:** Terraform, Checkov, OPA, CrewAI.

---

# 2.1 Aula: O Copilot de Infraestrutura
### De Requisitos a Arquivos Físicos

- **Evolução do Agente:** A IA deixa de apenas sugerir código e passa a gerenciar o sistema de arquivos via `writer_tool`.
- **Tradução HCL:** Como mapear "Ambiente de Produção" para argumentos de segurança robustos no Terraform.
- **Workflow:** Entrada em Linguagem Natural -> Processamento Agêntico -> Arquivo `main.tf` persistido.

---

# 2.2 Aula: Security Scan com Checkov
### Static Code Analysis (SCA) movido a IA

- **O que é o Checkov?** Ferramenta líder para escanear falhas de segurança em IaC.
- **Integração Agêntica:** O Agente Auditor executa o Checkov e "lê" o relatório de erros.
- **Loop de Self-Healing:** Se o Checkov reprova o código (ex: falta de criptografia no S3), a IA refatora o arquivo automaticamente até que o scan passe com sucesso.

---

# 2.3 Aula: Advanced Governance com OPA
### Policy-as-Code e Detecção de Drift

- **OPA (Open Policy Agent):** Validação de regras de negócio que scanners comuns não pegam (ex: "Buckets só podem existir na região us-east-1").
- **Detecção de Drift:** Monitoramento do estado real da nuvem versus o código.
- **Remediação Assistida:** A IA identifica mudanças manuais indevidas e gera o plano de ação para restaurar a conformidade.

---

# Prática: O Pipeline Nexus de IaC
### O que construímos no Advanced.py?

1. **Arquiteto:** Gera o HCL inicial.
2. **Auditor Checkov:** Garante que não há vulnerabilidades técnicas (SCA).
3. **Auditor OPA:** Garante que o código segue as regras da empresa.
4. **SRE Agent:** Detecta Drift e propõe correções de estado.

```bash
# Executando o ciclo de Chechov
python3 nexus_iac_copilot.py
````

---

# 2.3 Aula: Advanced Governance com OPA
### Policy-as-Code e Detecção de Drift

- **OPA (Open Policy Agent):** Validação de regras de negócio que scanners comuns não pegam (ex: "Buckets só podem existir na região us-east-1").
- **Detecção de Drift:** Monitoramento do estado real da nuvem versus o código.
- **Remediação Assistida:** A IA identifica mudanças manuais indevidas e gera o plano de ação para restaurar a conformidade.

---

# Prática: O Pipeline Nexus de IaC
### O que construímos no Advanced.py?

1. **Arquiteto:** Gera o HCL inicial.
2. **Auditor Checkov:** Garante que não há vulnerabilidades técnicas (SCA).
3. **Auditor OPA:** Garante que o código segue as regras da empresa.
4. **SRE Agent:** Detecta Drift e propõe correções de estado.

```bash
# Executando o ciclo completo de IA-Ops
python3 nexus_iac_advanced.py
```
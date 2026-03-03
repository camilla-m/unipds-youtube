---
marp: true
theme: uncover
class: invert
paginate: true
backgroundColor: #0a0e14
color: #babbbd
style: |
  section { text-align: left; font-size: 20px; }
  h1 { color: #00ff88; font-size: 38px; border-bottom: 2px solid #00ff88; padding-bottom: 10px; }
  h2 { color: #00d4ff; font-size: 28px; }
  code { background-color: #1a1f29; color: #ffca28; border-radius: 5px; }
  b { color: #00ff88; }
  .highlight { color: #ff7b72; font-weight: bold; }

---

# Módulo 2: IaC Copilot
## Arquitetura de Geração e Validação de Infraestrutura
**Professora:** Camilla Martins
**Tópicos:** Automação de HCL, File System Tools e DevSecOps Loop.

---

# 2.1 Tradução de Linguagem Natural para HCL
### O Desafio da Sintaxe e Semântica

- **Mapeamento de Requisitos:** Como a IA interpreta "Ambiente de Produção" e traduz para argumentos como `prevent_destroy = true` ou `versioning { enabled = true }`.
- **Modularização:** Instruindo agentes a não apenas criar recursos "soltos", mas a estruturar módulos Terraform reutilizáveis.
- **Tratamento de Strings:** O uso de **Regex** e limpeza de blocos de Markdown (` ```hcl `) para garantir que o código gerado seja interpretável pelo compilador do Terraform.

---

# 2.2 Custom Tools: As "Mãos" do Agente
### Integrando IA com o Sistema Operacional

Para que um Agente DevOps seja útil, ele precisa de **Efeito Colateral** (interagir com o mundo exterior).
- **Escrita de Arquivos:** Implementação de ferramentas Python que utilizam bibliotecas como `os` e `pathlib`.
- **Segurança de Execução:** - O perigo de injeção de comandos em ferramentas de escrita.
  - Implementação de **Guardrails** para restringir onde e o que a IA pode escrever.
- **Persistência de Estado:** Garantindo que o Agente saiba onde salvou o arquivo para que o próximo agente (Auditor) possa encontrá-lo.

---

# 2.3 DevSecOps: O Ciclo de Feedback com Checkov
### Auditoria Automatizada em Tempo Real

Não basta gerar código; é preciso garantir a **Conformidade (Compliance)**.
- **Checkov Integration:** Uma ferramenta de Static Code Analysis (SCA) que verifica +1000 políticas de segurança.
- **O Loop de Correção (Self-Healing):**
  1. **Auditor** executa o scan.
  2. **Auditor** extrai a `GUID` da falha (ex: CKV_AWS_145).
  3. **Auditor** envia o contexto do erro de volta para o **Arquiteto**.
  4. **Arquiteto** reaplica o conhecimento para corrigir o código.

---

# 2.4 Arquitetura do Lab: IaC Copilot Workflow

1. **Agente Arquiteto (The Builder):** - Objetivo: Gerar HCL funcional.
   - Ferramenta: `escritor_de_arquivo`.
2. **Agente Auditor (The Gatekeeper):**
   - Objetivo: Garantir Zero Vulnerabilidades.
   - Ferramenta: `scanner_de_seguranca` (Python Wrapper sobre Checkov).
3. **Workflow:** Sequencial com revisão. O processo só termina quando o Checkov retornar `Passed`.

---

# 🛠️ Laboratório: Hands-on
- Configuração do **Checkov** no ambiente virtual.
- Desenvolvimento da Tool de Subprocesso para execução de comandos CLI via Agente.
- Simulação de erro de segurança proposital para observar o **Agente de IA corrigindo o código sozinho**.

---

# 🚀 Conclusão do Módulo 2
- IA não substitui o engenheiro, mas potencializa a **velocidade de entrega**.
- A governança é feita via **Código e Scanners**, não via processo manual.
- O resultado final é um arquivo `main.tf` pronto para o `terraform apply`.

**Próximo Módulo:** Agentes para Kubernetes: Deploy e Operação.
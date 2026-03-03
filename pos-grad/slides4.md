---
marp: true
theme: uncover
class: invert
paginate: true
backgroundColor: #0a0e14
color: #e6edf3

---

# Módulo 4: Troubleshooting com ReAct
## Reduzindo MTTR com Inteligência Agêntica
**Professora:** Camilla Martins

---

# Aula 4.1: Framework ReAct
- **Raciocínio Computacional:** Pensar -> Agir -> Observar.
- **Diferença de Agentes Simples:** O Agente ReAct decide qual ferramenta usar baseado na resposta da ferramenta anterior.

---

# Aula 4.2: Depuração de Pods
- **CrashLoopBackOff:** Falha na aplicação ou config.
- **OOMKilled:** Estrangulamento de recursos (Memory Limits).
- **Análise Automática:** A IA lê o `describe pod` e extrai a causa raiz em segundos.

---

# Aula 4.3: Observabilidade Distribuída
- **Correlação:** Unindo métricas (Prometheus) e Traces (Jaeger).
- **Gargalos:** Identificando se a lentidão é no Banco de Dados ou na latência da rede.

---

# Prática: Self-Healing Script
- Automação do ciclo completo: Identificação da falha -> Proposta de correção -> Atualização do código (Fix).
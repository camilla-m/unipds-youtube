---
marp: true
theme: uncover
class: invert
paginate: true
backgroundColor: #0a0e14
color: #e6edf3

---
# Módulo 3: K8s AI-Ops
## Orquestração e SRE Assistida por IA

---

## 3.1 Manifestos e Inteligência de Escala
- **YAML Generativo:** A IA não apenas escreve código, ela entende a infraestrutura necessária (Containers, Ports, Probes).
- **Readiness Probes:** Essencial para evitar que o tráfego chegue a pods não inicializados.

---

## 3.2 O "Go/No-Go" do Rollout
- **Canary Analysis:** Como a IA interpreta logs de erro para decidir o futuro do deploy.
- **Remediação em Tempo Real:** Se o Canary falha, o Agente SRE executa o rollback preventivo.

---

## 3.3 GitOps: O Elo entre IA e Cluster
- **Reconciliação:** A IA atua como o engenheiro que submete o desejo ao Git.
- **Argo CD / Flux:** A peça de software que garante que o desejo da IA se torne realidade no Kubernetes.
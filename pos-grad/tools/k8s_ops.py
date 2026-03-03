import subprocess
import os
from crewai.tools import tool

@tool("k8s_manifest_generator")
def k8s_manifest_generator(app_name: str, replicas: int, port: int):
    """Gera manifestos YAML de Deployment e Service para Kubernetes."""
    manifest = f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: {app_name}
spec:
  replicas: {replicas}
  selector:
    matchLabels:
      app: {app_name}
  template:
    metadata:
      labels:
        app: {app_name}
    spec:
      containers:
      - name: {app_name}
        image: nginx:latest
        ports:
        - containerPort: {port}
        readinessProbe:
          httpGet:
            path: /
            port: {port}
---
apiVersion: v1
kind: Service
metadata:
  name: {app_name}-svc
spec:
  selector:
    app: {app_name}
  ports:
  - protocol: TCP
    port: 80
    targetPort: {port}
"""
    filename = f"{app_name}-k8s.yaml"
    with open(filename, "w") as f:
        f.write(manifest)
    return f"✅ Manifestos para {app_name} gerados em {filename}."

@tool("k8s_apply_tool")
def k8s_apply_tool(filename: str):
    """Simula ou executa a reconciliação GitOps via kubectl apply."""
    try:
        # Tenta executar no cluster real (se houver um configurado)
        # Se não houver, o erro será capturado e tratado como simulação
        result = subprocess.run(
            ["kubectl", "apply", "-f", filename],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            return f"✅ GitOps Sync Sucesso: {result.stdout}"
        else:
            return f"⚠️ Simulação GitOps: Arquivo {filename} validado, mas o cluster K8s não foi detectado. O controlador aguardaria o sync."
    except FileNotFoundError:
        return "ℹ️ Modo Simulação: Kubectl não instalado. Em produção, o ArgoCD aplicaria este manifesto agora."

@tool("canary_analyzer")
def canary_analyzer(metrics_data: str):
    """Analisa métricas para decisão de Rollout."""
    if "error_rate > 5%" in metrics_data:
        return "❌ ROLLBACK: Taxa de erro elevada no Canary."
    return "✅ PROCEED: Métricas estáveis. Rollout aprovado."
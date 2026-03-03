from crewai.tools import tool

@tool("query_prometheus_metrics")
def query_prometheus_metrics(query: str):
    """Executa uma query PromQL no Prometheus para analisar métricas de CPU/Memória/Latência."""
    if "latency" in query.lower() or "duration" in query.lower():
        return "📊 Prometheus Result: Latência média no endpoint /checkout é de 850ms (ALTA). P99 estourado."
    if "error" in query.lower():
        return "📊 Prometheus Result: Taxa de erro de 5XX está em 12% nos últimos 5 minutos."
    return "📊 Prometheus Result: Métricas dentro do baseline normal."

@tool("query_jaeger_traces")
def query_jaeger_traces(service_name: str):
    """Consulta o Jaeger para encontrar gargalos em traces distribuídos."""
    return f"🔍 Jaeger Trace: O gargalo do serviço '{service_name}' está na chamada para o banco de dados PostgreSQL (Span duration: 800ms)."
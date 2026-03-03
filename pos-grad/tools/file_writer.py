from crewai.tools import tool

@tool("writer_tool")
def writer_tool(content: str, filename: str = "main.tf"):
    """Salva código gerado em um arquivo físico."""
    with open(filename, "w") as f:
        f.write(content.replace("```hcl", "").replace("```", "").strip())
    return f"✅ Arquivo {filename} salvo."
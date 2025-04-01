
from rich.console import Console
from rich.panel import Panel

def painel_simples(texto, isArquivo):
  
    console = Console()
    if isArquivo:
        with open(texto, 'r') as f:
            texto = f.read()
    painel = Panel(texto)
    console.print(painel)

def painel_destacado(texto, isArquivo):
    
    console = Console()
    if isArquivo:
        with open(texto, 'r') as f:
            texto = f.read()
    painel = Panel(texto, style="green", title="Painel Destacado", border_style="bold red")
    console.print(painel)

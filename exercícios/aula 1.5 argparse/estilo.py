from rich.console import Console
from rich.text import Text

def estilo_simples(texto, isArquivo):

    console = Console()
    if isArquivo:
        with open(texto, 'r') as f:
            texto = f.read()
    text = Text(texto, style="red")
    console.print(text)

def estilo_bold(texto, isArquivo):
    
    console = Console()
    if isArquivo:
        with open(texto, 'r') as f:
            texto = f.read()
    text = Text(texto, style="bold")
    console.print(text)

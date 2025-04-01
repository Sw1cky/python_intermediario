import rich

from rich.console import Console
from rich.text import Text

def layout_simples(texto, isArquivo):
  
    console = Console()
    if isArquivo:
        with open(texto, 'r') as f:
            texto = f.read()
    text = Text(texto)
    console.print(text)

def layout_destacado(texto, isArquivo):

    console = Console()
    if isArquivo:
        with open(texto, 'r') as f:
            texto = f.read()
    text = Text(texto, style="bold magenta")
    console.print(text)

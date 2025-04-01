from rich.console import Console
from rich.progress import Progress

def progresso_simples(texto, isArquivo):

    console = Console()
    if isArquivo:
        with open(texto, 'r') as f:
            texto = f.read()
    with Progress() as progress:
        task = progress.add_task("[cyan]Processando...", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            console.print(texto)

def progresso_avancado(texto, isArquivo):
   
    console = Console()
    if isArquivo:
        with open(texto, 'r') as f:
            texto = f.read()
    with Progress(transient=True) as progress:
        task = progress.add_task("[green]Carregando...", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            console.print(texto)

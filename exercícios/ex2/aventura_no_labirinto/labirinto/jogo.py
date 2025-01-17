# labirinto/jogo.py

from labirinto.labirinto import Labirinto
from rich.console import Console
from rich.panel import Panel
from pynput.keyboard import Listener, Key

console = Console()

def mostrar_instrucoes():
    """
    Mostra as instruções do jogo.
    """
    console.print(Panel(
        "[bold blue]Seja bem-vindo ao Aventura no Labirinto![/bold blue]\n"
        "Use as teclas para se mover:\n"
        " - [bold green]W[/bold green]: Norte\n"
        " - [bold green]S[/bold green]: Sul\n"
        " - [bold green]A[/bold green]: Oeste\n"
        " - [bold green]D[/bold green]: Leste\n\n"
        "Seu objetivo é chegar à saída marcada por '[bold red]X[/bold red]'. Boa sorte!",
        title="[bold yellow]Instruções[/bold yellow]"
    ))

def capturar_movimento(callback):
    """
    Captura o movimento do jogador usando o teclado.
    """
    def on_press(key):
        if key == Key.esc:
            return False
        elif hasattr(key, 'char') and key.char:
            callback(key.char)

    with Listener(on_press=on_press) as listener:
        listener.join()

def jogar(modo="normal"):
    """
    Controla o fluxo principal do jogo.
    :param modo: Define o modo de dificuldade (normal ou difícil).
    """
    tamanho = 5 if modo == "normal" else 7
    labirinto = Labirinto(tamanho)
    labirinto.gerar_labirinto()

    console.print(Panel(f"Modo: [bold green]{modo.upper()}[/bold green]", title="[bold yellow]Informação[/bold yellow]"))
    mostrar_instrucoes()

    def movimentar_jogador(tecla):
        movimentos = {"w": "norte", "s": "sul", "a": "oeste", "d": "leste"}
        direcao = movimentos.get(tecla.lower())
        if direcao:
            if labirinto.mover_jogador(direcao):
                console.print(f"[green]Você se moveu para o {direcao}.[/green]")
            else:
                console.print("[red]Movimento inválido![/red]")
            if labirinto.chegou_na_saida():
                console.print("[bold green]Parabéns! Você encontrou a saída![/bold green]")
                return False
            labirinto.mostrar_labirinto()
        return True

    labirinto.mostrar_labirinto()
    capturar_movimento(movimentar_jogador)


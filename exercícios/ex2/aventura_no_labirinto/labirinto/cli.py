import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Jogo Aventura no Labirinto.")
    parser.add_argument("--modo", choices=["normal", "dificil"], default="normal", help="Modo de dificuldade")
    return parser.parse_args()

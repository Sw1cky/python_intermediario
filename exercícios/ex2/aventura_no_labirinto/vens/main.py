from labirinto.cli import parse_args
from labirinto.jogo import jogar

if __name__ == "__main__":
    args = parse_args()
    jogar(modo=args.modo)
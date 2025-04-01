import argparse
from personalizador import layout, painel, progresso, estilo

def main():
    parser = argparse.ArgumentParser(description="Imprimir texto formatado com Rich")
    parser.add_argument("texto", help="Texto ou caminho para um arquivo de texto")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento é um arquivo")
    parser.add_argument("-m", "--modulo", choices=["layout", "painel", "progresso", "estilo"], required=True, help="Escolha o módulo")
    parser.add_argument("-f", "--funcao", choices=["simples", "destacado", "avancado", "bold"], required=True, help="Escolha a função")

    args = parser.parse_args()

    # Mapeando funções de acordo com os módulos
    modulos = {
        "layout": layout,
        "painel": painel,
        "progresso": progresso,
        "estilo": estilo
    }

    funcoes = {
        "simples": "layout_simples",
        "destacado": "layout_destacado",
        "avancado": "progresso_avancado",
        "bold": "estilo_bold"
    }

    modulo = modulos[args.modulo]
    funcao = getattr(modulo, f"{args.funcao}")

    funcao(args.texto, args.arquivo)

if __name__ == "__main__":
    main()

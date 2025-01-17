
class Labirinto:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matriz = [[" " for _ in range(tamanho)] for _ in range(tamanho)]
        self.posicao_jogador = (0, 0)

    def mostrar_labirinto(self):
        for linha in self.matriz:
            print("".join(linha))

    def mover_jogador(self, direcao):
        x, y = self.posicao_jogador
        if direcao == "norte" and x > 0:
            x -= 1
        elif direcao == "sul" and x < self.tamanho - 1:
            x += 1
        elif direcao == "leste" and y < self.tamanho - 1:
            y += 1
        elif direcao == "oeste" and y > 0:
            y -= 1
        self.posicao_jogador = (x, y)

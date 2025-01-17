def encontrar_caminho(labirinto, posicao, destino, caminho=None):
   
    if caminho is None:
        caminho = []

    x, y = posicao
    if posicao == destino:
        return caminho

    movimentos = [("norte", (x - 1, y)), ("sul", (x + 1, y)), ("oeste", (x, y - 1)), ("leste", (x, y + 1))]
    for direcao, (novo_x, novo_y) in movimentos:
        if 0 <= novo_x < len(labirinto) and 0 <= novo_y < len(labirinto[0]) and labirinto[novo_x][novo_y] not in ("#", "O"):
            labirinto[x][y] = "O"
            resultado = encontrar_caminho(labirinto, (novo_x, novo_y), destino, caminho + [direcao])
            labirinto[x][y] = " "
            if resultado:
                return resultado

    return None
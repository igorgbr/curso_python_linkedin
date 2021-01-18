def escreve_arquivo():
    arquivo = open("novo_arquivo.txt", "w+")

    arquivo.write("Linha gerada com a função 'escreve_arquivo'\r\n")

    arquivo.close()


''' escreve_arquivo() '''


def altera_arquivo():
    arquivo = open("novo_arquivo.txt", "a+")

    arquivo.write("Linha gerada com a função 'altera_arquivo'\r\n")

    arquivo.close()


altera_arquivo()

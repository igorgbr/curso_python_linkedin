from html.parser import HTMLParser


class meu_parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Tag de abertura encontrada")
        if attrs.__len__() > 0:
            for a in attrs:
                print("  valores encontrados: ", a[0], " = ", a[1])

    def handle_endtag(self, tag):
        print("Tage de fechamento encontrada")

    def handle_comment(self, data):
        print("Comentario encontrado.")

    def handle_data(self, data):
        print("Valores encontrados.")
        if data.isspace():
            print("valor encontrado é um espaço")
        else:
            print("O valor encontrado é: ", data)


def meu_objeto():
    meu_parser1 = meu_parser()
    arquivo = open(
        "//home//igor//projetos_pessoais//curso_python_linkedin//data_e_hora//calendario.html",
        "r",
    )
    dados = arquivo.read()
    meu_parser1.feed(dados)


meu_objeto()

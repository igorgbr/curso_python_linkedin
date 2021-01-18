class minha_classe():
    def __init__(self):
        self.meuAtributo = "passou pelo construtor"

    def meuMetodo(self):
        print("Passou pelo meuMetodo")

    def meuMetodo2(self, valor):
        self.outroAtributo = valor
        print(self.outroAtributo)


def criaObjeto():
    meuObj = minha_classe()
    var1 = meuObj.meuAtributo
    print(var1)

    meuObj.meuMetodo()

    meuObj.meuMetodo2("executando um metodo")


criaObjeto()

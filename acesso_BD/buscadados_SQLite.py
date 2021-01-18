import sqlite3


def manipula_dados(banco_dados, comando):
    conexao = sqlite3.connect(banco_dados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    conexao.close()


def seleciona_dados(banco_dados, comando):
    conexao = sqlite3.connect(banco_dados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()

    for linha in linhas:
        print(linha)


def manipulacao_dados():
    pathBD = "//home//igor//projetos_pessoais//curso_python_linkedin//acesso_BD//BancoDeDados.db"

    comandoINSERT = "INSERT INTO estados(nome_estado, sigla_estado, nome_capital) VALUES ('Texas', 'TX', 'Teste Inclussao')"
    comandoSELECT = "SELECT nome_estado  FROM estados"

    """ manipula_dados(pathBD, comandoINSERT) """
    seleciona_dados(pathBD, comandoSELECT)


manipulacao_dados()

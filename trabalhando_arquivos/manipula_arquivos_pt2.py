import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def cria_zip_modo1():
    shutil.make_archive(
        "arquivo_compactado",
        "zip",
        "//home//igor//projetos_pessoais//curso_python_linkedin//básico",
    )


""" cria_zip_modo1() """


def cria_zip_modo2():
    with ZipFile("arquivo_zip_modo2.zip", "w") as novoZip:
        novoZip.write("arquivo_alterado.txt")
        novoZip.write("novo_arquivo.txt")
        novoZip.write("arquivo_compactado.zip")


""" cria_zip_modo2() """


def deleta_arquivo():
    os.remove("arquivo_zip_modo2.zip")


deleta_arquivo()

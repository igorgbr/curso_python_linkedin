from datetime import date
''' from datetime import time '''
from datetime import datetime


def manipula_data_e_hora():
    hoje = date.today()
    print("Hoje é: ", hoje)
    print("Partes da data: ", hoje.day, hoje.month, hoje.year)
    print("numero do dia da semana: ", hoje.weekday())
    dias = ["seg", "ter", "quar", "quint", "sext", "sab", "doming"]
    print("nome abreviado do dia da semana: ", dias[hoje.weekday()])

    data = datetime.now()
    print("data e hora ", data)

    tempo = datetime.time(data)
    print("hora atual ", tempo)


manipula_data_e_hora()

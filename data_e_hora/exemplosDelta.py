from datetime import date
''' from datetime import time
from datetime import datetime
from datetime import timedelta '''


def quantos_dias_faltam(ano, mes, dia):
    hoje = date.today()
    dataProcurada = date(ano, mes, dia)

    qtos_dias = dataProcurada - hoje

    mensagem_retorno = (
        "Faltam "
        + str(qtos_dias).replace("days, 0:00:00", "")
        + " dias para a data "
        + dataProcurada.strftime("%d/%m/%y")
    )

    print(mensagem_retorno)


quantos_dias_faltam(2022, 10, 29)

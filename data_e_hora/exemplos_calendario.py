import calendar


def imprime_mes():
    for mes in calendar.month_name:
        print(mes)

    for dia in calendar.day_name:
        print(dia)


''' imprime_mes() '''


def cria_lista_days():
    dias = []
    for dia in calendar.day_name:
        dias.append(dia)
    return dias


print(cria_lista_days())

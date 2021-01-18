import calendar


def calendario_texto():
    calendario_texto = calendar.TextCalendar(calendar.SUNDAY)
    txt_calendario = calendario_texto.formatmonth(2019, 6)
    print(txt_calendario)


""" calendario_texto() """


def calendario_html():
    calendario_html = calendar.HTMLCalendar(calendar.SUNDAY)
    html_calendario = calendario_html.formatmonth(2019, 8)

    arquivo = open("novo_calendario.html", "a+")
    arquivo.write("\r\n\r\n" + html_calendario)
    arquivo.close()


calendario_html()

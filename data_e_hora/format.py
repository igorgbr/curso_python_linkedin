from datetime import datetime


def formata_data_hora():
    hoje = datetime.now()

    print(hoje.strftime("O ano é: %Y"))
    print(hoje.strftime("Data e hora local: %c"))

    print(hoje.strftime("A hora atual é: %I:%M:%S %p"))


formata_data_hora()

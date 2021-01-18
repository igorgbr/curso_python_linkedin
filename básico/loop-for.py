def loop_for():
    for x in range(5, 10):
        print(x)


loop_for()


def loop_array():
    dias = [
        "segunda",
        "terça",
        "quarta",
        "quinta",
        "sexta",
        "sabado",
        "domingo",
    ]
    for d in dias:
        print(d)


loop_array()


def loop_enumerated():
    dias = [
        "segunda",
        "terça",
        "quarta",
        "quinta",
        "sexta",
        "sabado",
        "domingo",
    ]
    for i, d in enumerate(dias):
        print(i, d)


loop_enumerated()

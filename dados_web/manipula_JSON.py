import urllib.request
import json


def manipula_JSON():
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    weburl = urllib.request.urlopen(endereco)
    if weburl.getcode() == 200:
        dados = weburl.read()
        obj_JSON = json.loads(dados)

        contagem = obj_JSON["metadata"]["count"]
        print("Contagem: " + str(contagem))

        for local in obj_JSON["features"]:
            if (
                local["properties"]["place"]
                == "55 km S of Whites City, New Mexico"
            ):
                print("Encontrado registro especial *******")
            else:
                print(local["properties"]["place"])


manipula_JSON()

import urllib.request
import json


def manipula_JSON():
    end = "https://jsonplaceholder.typicode.com/posts"
    weburl = urllib.request.urlopen(end)

    if weburl.getcode() == 200:
        dados = weburl.read()
        dados_JSON = json.loads(dados)

        for user in dados_JSON:
            if(user["id"]) <= 3:
                print(user["userId"])
                print(user["title"])
                print(user["body"])


manipula_JSON()

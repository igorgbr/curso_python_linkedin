import pymongo
from pymongo import MongoClient


def manipula_dados_MongoDB():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.conheca_python

    for i in range(1, 10):
        objdic = {"codigo": i}
        db.conheca_mongodb.insert_one(objdic)

    db.conheca_mongodb.update_one(
        {"codigo": 2}, {"$set": {"atributoNovo": 789}}
    )

    db.conheca_mongodb.delete_one({'codigo': 1})

    resultado_consulta = db.conheca_mongodb.find({})

    for doc in resultado_consulta:
        print(doc)


manipula_dados_MongoDB()

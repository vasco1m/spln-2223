import re
import json


file = open('medicina.json', 'r',encoding='utf8')
entradas = json.load(file)

medicalDict = {}

for entrada in entradas:
    traducoes = {}
    if "en" in entradas[entrada]:
        traducoes["en"] = entradas[entrada]["en"]
    if "es" in entradas[entrada]:
        traducoes["es"] = entradas[entrada]["es"]
    if "pt" in entradas[entrada]:
        traducoes["pt"] = entradas[entrada]["pt"]
    if "la" in entradas[entrada]:
        traducoes["la"] = entradas[entrada]["la"]
    termo = ""
    sexo = ""
    notas = ""
    sin = ""
    var = ""
    vid = ""
    if "termo" in entradas[entrada]:
        termo = entradas[entrada]["termo"]
    if "sexo" in entradas[entrada]:
        sexo = entradas[entrada]["sexo"]
    if "notas" in entradas[entrada]:
        notas = entradas[entrada]["notas"]
    if "sinonimos" in entradas[entrada]:
        sin = entradas[entrada]["sinonimos"]
    if "variacoes" in entradas[entrada]:
        var = entradas[entrada]["variacoes"]
    if "vid" in entradas[entrada]:
        vid = entradas[entrada]["vid"]
    traducoes["ga"] = {
        "termo": termo,
        "sexo": sexo,
        "notas": notas,
        "sin": sin,
        "var": var,
        "vid": vid
    }
    medicalDict[entrada] = traducoes

output = open('medicinaAbs.json', 'w',encoding='utf8')
json.dump(medicalDict, output,ensure_ascii=False)
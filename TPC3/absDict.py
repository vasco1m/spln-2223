import re
import json


file = open('medicina.json', 'r',encoding='utf8')
entradas = json.load(file)

medicalDict = {}

for entrada in entradas:
    traducoes = {}
    areas = ""
    if "area" in entradas[entrada]:
        areas = entradas[entrada]["area"].split(" ")
    if "en" in entradas[entrada]:
        if ";" in entradas[entrada]["en"]:
            traducoes["en"] = entradas[entrada]["en"].split(";")
        else:
            traducoes["en"] = entradas[entrada]["en"]
    if "es" in entradas[entrada]:
        if ";" in entradas[entrada]["es"]:
            traducoes["es"] = entradas[entrada]["es"].split(";")
        else:
            traducoes["es"] = entradas[entrada]["es"]
    if "pt" in entradas[entrada]:
        if ";" in entradas[entrada]["pt"]:
            traducoes["pt"] = entradas[entrada]["pt"].split(";")
        else:
            traducoes["pt"] = entradas[entrada]["pt"]
    if "la" in entradas[entrada]:
        if ";" in entradas[entrada]["la"]:
            traducoes["la"] = entradas[entrada]["la"].split(";")
        else:
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
        if ";" in entradas[entrada]["sinonimos"]:
            sin = entradas[entrada]["sinonimos"].split(";")
        else:
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
    ent = {
        "Areas": areas,
        "Traduções": traducoes,
    }
    medicalDict[entrada] = ent

output = open('medicinaAbs.json', 'w',encoding='utf8')
json.dump(medicalDict, output,ensure_ascii=False, indent=4)
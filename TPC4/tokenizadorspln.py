#!/usr/bin/env python3
"""Module to tokenize books
"""

__version__ = "0.2"

import fileinput
import re

# Quebras de página ✅
# Separar pontuação das palavras
# Marcar capítulos ✅
# Separar parágrafos de linhas pequenas
# Juntar linhas da mesma frase ✅
# Uma frase por linha ✅

def get_abrevituras():
    file = open("conf/abrevituras.txt", "r")
    abrevituras = file.read()
    langs = abrevituras.split("#")
    langs = remove_empty(langs)
    abrev_dict = {}
    for lang in langs:
        ln,*abrevs = lang.split("\n")
        abrevs = remove_empty(abrevs)
        if len(abrevs) > 0:
            abrev_dict[ln] = abrevs
    return abrev_dict

def remove_empty(l):
    return [x.strip() for x in l if x.strip()]

def tokenizer():
    text = ""
    for line in fileinput.input():
        text += line

    regex_cap = r".*(CAP[ÍI]TULO\s+\w+).*"

    text = re.sub(regex_cap, r"\n# \1", text)

    regex_nl = r"([a-z0-9,;–\?])\s*\n\s*\n\s*([a-z0-9])"

    text = re.sub(regex_nl, r"\1 \2", text)

    regex_nl2 = r"([a-z0-9,;–])\s*\n\s*([a-z0-9])"

    text = re.sub(regex_nl2, r"\1 \2", text)

    regex_nl3 = r"([\.\?])\s*\n\s*\n\s*([A-Z–])"

    text = re.sub(regex_nl3, r"\1\n\2", text)

    regex_nl4 = r"([\.\?])\s*\n\s*([A-Z–])"

    text = re.sub(regex_nl4, r"\1\n\2", text)

    regex_nl5 = r"([A-Z])\s*\n([A-Z])"

    text = re.sub(regex_nl5, r"\1 \2", text)

    #regex_pont = r"([a-z0-9,;–])\s*([,;–])"

    #text = re.sub(regex_pont, r"\1 \2", text)

    regex_frase = r"([a-z0-9,;–\(\)])\s*([\.?!])\s*([^,\”])"

    text = re.sub(regex_frase, r"\1\2\n\3", text)

    regex_frase2 = r"(Sr.|Sra.)\s*\n"

    text = re.sub(regex_frase2, r"\1 ", text)

    regex_frase3 = r"\.\n\.\.\s*"

    text = re.sub(regex_frase3, r"...", text)

    regex_frase4 = r"(.*\.\”)\s*([A-Z].*)"

    text = re.sub(regex_frase4, r"\1\n\2", text)

    return text

arr_poemas = []

def guarda_poema(poema):
    arr_poemas.append(poema[1])
    return f">>{len(arr_poemas)}<<"

def poemas():
    regex_poema = r"(<poema>(.*?)</poema>)"
    text = re.sub(regex_poema, guarda_poema, text, flags=re.S)


def save(text):
    #salvar o texto
    with open("resultado.txt", "w") as f:
        f.write(text)


def main():
    print("Tokenizador de textos para o SPLN")
    print("Versão", __version__)
    print("")
    print("Arquivo de entrada: ", fileinput.filename())
    print("Arquivo de saída: resultado.txt")
    text = tokenizer()
    save(text)

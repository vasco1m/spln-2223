#!/usr/bin/env python3
"""Module to tokenize books
"""
__version__ = "0.3"


import fileinput
import re
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog= 'Tokenizador',
        description= 'Tokenize a given file',
        epilog= 'Created by Vasco Matos'
    )


    parser.add_argument('--input', '-i', help="Define the input file", default=None,required=False)
    parser.add_argument('--output', '-o', help="Define the output file", required=False)
    parser.add_argument('--lang', '-l', help="Define the language of abbreviations to use", required=False)
    parser.add_argument('--abrev', '-a', help="Define the file with abbreviations", required=False)
    args = parser.parse_args()

    input = "stdin"
    output = "stdout"
    lang = "pt"
    abrev_file = "conf/abrevituras.txt"

    try:
        if args.input is not None:
            input = args.input
        if args.output is not None:
            output = args.output
        if args.lang is not None:
            lang = args.lang
        if args.abrev is not None:
            abrev_file = args.abrev
        abrev = get_abrevituras(abrev_file)[lang]
    except:
        print("Error parsing arguments")
        sys.exit(1)

    text = tokenizer(input, abrev)
    save(text, output)

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

def tokenizer(input, abrev):
    text = ""
    #read the file
    if input == "stdin":
        for line in fileinput.input():
            text += line
    else:
        with open(input, "r") as f:
            text = f.read()

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

    def ab(a):
        l = a[0].lower()
        if l in abrev.keys():
            return "#Abrev#" + abrev[l] + "#"
        return a[0]

    regex_abrev = r'\w+\.'
    text = re.sub(regex_abrev, ab, text)

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


def save(text, output):
    #salvar o texto
    with open(output, "w") as f:
        f.write(text)

    
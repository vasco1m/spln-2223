# ZEP -> E*
# E -> EC
#    | ER
# EC -> num pals pos CORPO
# CORPO -> area LINGUAS
# LINGUAS -> pt pals
#          | en pals
#          | es pals
# ER -> pals VID
# VID -> Vid.- pals

import re
import json

texto = open('medicina.xml', 'r').read()

def removeXMLfirstLines(texto):
    texto = re.sub(r'<\?xml.*\n', r'', texto)
    texto = re.sub(r'<!DOCTYPE.*\n', r'', texto)
    texto = re.sub(r'<pdf2xml.*\n', r'', texto)
    texto = re.sub(r'<page.*\n', r'', texto)
    texto = re.sub(r'<fontspec.*\n', r'', texto)
    texto = re.sub(r'</pdf2xml>', r'', texto)
    return texto


texto = removeXMLfirstLines(texto)


def remove_header_footer_wLines(texto):
    texto = re.sub(r'<text.* font="1">ocabulario.*</text>', r'###', texto)
    texto = re.sub(r'.*\n###\n.*\n', r'', texto)
    texto = re.sub(r'<page.*\n|</page>\n', r'', texto)
    texto = re.sub(r'<text.* font="3">\s*</text>', r'', texto)
    texto = re.sub(r'\n<text.* font="3"><b>\s*</b></text>', r'', texto)
    texto = re.sub(r'\n<text.* font="4"><b>\s*</b></text>', r'', texto)
    texto = re.sub(r'<text.* font="5">\s*</text>', r'', texto)
    texto = re.sub(r'\n<text.* font="12">\s*</text>', r'', texto)
    return texto

texto = remove_header_footer_wLines(texto)

def marcaE(texto):
    #Entradas Completas
    texto = re.sub(r'<text.* font="2">\s*(\d+)\s*</text>\n<text.* font="3"><b>\s*(.*)</b></text>\n\n<text.* font="3"><b>\s*(.*)(m|f|a|s)\s*(pl)*</b></text>', r'###C \1 \2\3\nSex. \4\n\5', texto) # Marcar entradas completas do dicionário separadas por linhas
    texto = re.sub(r'<text.* font="3"><b>\s*(\d+.*)\s*</b></text>\n<text.* font="10"><i><b>\s*(.*)</b></i></text>\n<text.* font="3"><b>\s*(m|f|a|s)\s*(pl)*</b></text>', r'###C \1 \2\nSex. \3\n\4', texto) # Marcar entradas completas do dicionário separadas por linhas
    texto = re.sub(r'<text.* font="2">\s*(\d+)\s*</text>\n<text.* font="3"><b>\s*(.*)(m|f|a|s)\s*(pl)*</b></text>', r'###C \1 \2\nSex. \3\n\4', texto) # Marcar entradas completas do dicionário separadas por linhas
    texto = re.sub(r'<text.* font="3"><b>\s*(.*)</b></text>\n\n<text.* font="3"><b>\s*(.*)(m|f|a|s)\s*(pl)*</b></text>', r'###C \1 \2\nSex. \3\n\4', texto) # Marcar entradas completas do dicionário separadas por linhas
    texto = re.sub(r'<text.* font="12">\s*(\d+)\s*</text>\n<text.* font="11"><b>\s*(.*)(m|f|a|s)\s*(pl)*</b></text>', r'###C \1 \2\nSex. \3\n\4', texto) # Marcar entradas completas do dicionário separadas por linhas
    texto = re.sub(r'<text.* font="3"><b>\s*(\d+.*)(m|f|a|s)\s*(pl)*</b></text>', r'###C \1\nSex. \2\n\3', texto) # Marcar entradas completas do dicionário
    #Entradas Remissivas
    texto = re.sub(r'<text.* font="8"><b>\s*(.*)\s*</b></text>', r'###R \1', texto) # Marcar entradas remissívas do dicionário
    texto = re.sub(r'<text.* font="3"><b>\s*(\S.*)</b></text>', r'###R \1', texto) # Marcar entradas remissívas do dicionário
    texto = re.sub(r'<text.* font="11"><b>\s*(\S.*)</b></text>', r'###R \1', texto) # Marcar entradas remissívas do dicionário
    texto = re.sub(r'###R\s*\n', r'\n', texto) # Remover linhas vazias antes de uma entrada remissíva
    texto = re.sub(r'<text.* font="2">\s*</text>\n', r'', texto)
    texto = re.sub(r'\n<text.* font="10"><i><b>\s*(.*)</b></i></text>', r'\1', texto)
    return texto

texto = marcaE(texto)

def marcaLinguas(texto):
    texto = re.sub(r'<text.* font="0">\s*</text>', r'', texto) # Remover linhas vazias antes de uma linguágem
    texto = re.sub(r'<text.* font="0">\s*;\s*</text>', r';', texto) # Remover linhas com apenas um ponto e vírgula e fonte 0
    texto = re.sub(r'<text.* font="0">\s*(es|en|pt|la)\s*</text>\n', r'@ \1', texto) # Marcar liguágens do dicionário
    texto = re.sub(r'<text.* font="7"><i>\s*(.*)</i></text>\n;\n', r'\1;', texto)
    texto = re.sub(r'<text.* font="7"><i>\s*(.*)</i></text>', r'\1', texto)
    return texto


texto = marcaLinguas(texto)


def marcaVariacoes(texto):
    texto = re.sub(r'<text.* font="5">\s*VAR\.- (.*)</text>', r'VAR. \1', texto) # Marcar variações
    return texto


texto = marcaVariacoes(texto)


def marcaSinonimos(texto):
    texto = re.sub(r'\n<text.* font="0">\s*</text>', r'', texto) # Marcar sinonimos
    texto = re.sub(r'<text.* font="0">\s*SIN\.- (.*)</text>', r'SIN. \1', texto) # Marcar sinonimos
    texto = re.sub(r'\n<text.* font="0">\s*(.*)</text>', r'\1', texto) # Marcar sinonimos
    texto = re.sub(r'<text.* font="5">\s*SIN\.- (.*)</text>', r'SIN. \1', texto) # Marcar sinonimos
    texto = re.sub(r'\n<text.* font="5">\s*(.*)</text>', r'\1', texto) # Marcar sinonimos
    return texto


texto = marcaSinonimos(texto)


def marcaArea(texto):
    texto = re.sub(r'<text.* font="6"><i>\s*(.*)</i></text>', r'AREA. \1', texto) # Marcar área
    return texto


texto = marcaArea(texto)


def marcaVid(texto):
    texto = re.sub(r'<text.* font="5">\s*Vid\.- (.*)</text>', r'VID. \1', texto)
    texto = re.sub(r'<text.* font="0">\s*Vid\.- (.*)</text>', r'VID. \1', texto)
    return texto


texto = marcaVid(texto)


def marcaNotas(texto):
    texto = re.sub(r'<text.* font="9">\s*</text>\n', r'', texto)
    texto = re.sub(r'<text.* font="9">\s*Nota\.-(.*)</text>', r'Nota. \1', texto)
    texto = re.sub(r'\n<text.* font="9">\s*(.*)</text>', r'\1', texto)
    return texto


texto = marcaNotas(texto)


def removeSimbQuim(texto):
    texto = re.sub(r'\n<text.* font="13"><b>(\d+)</b></text>', r'\1', texto)
    texto = re.sub(r'\n<text.* font="14">(\d+)</text>', r'\1', texto)
    texto = re.sub(r'\n<text.* font="15"><i>(\d+)</i></text>', r'\1', texto)
    return texto


texto = removeSimbQuim(texto)


texto = re.sub(r' {2,}', r' ', texto)


entradas = texto.split('###')
dicC = {}
dicR = {}

for entrada in entradas:
    r = 0
    if entrada.startswith('C'):
        match = re.match(r'C\s*(\d+)\s*(.*)\nSex\.\s*(.*)', entrada)
        if match:
            id = match.group(1)
            termo = match.group(2)
            sexo = match.group(3)
            entrada = re.sub(r'C\s*(\d+)\s*(.*)\nSex\.\s*(.*)', r'', entrada)
            area = ""
            notas = ""
            sinonimos = ""
            variacoes = ""
            vid = ""
            linguas = {}
            match = re.search(r'AREA\.\s*(.*)', entrada)
            if match:
                area = match.group(1)
                entrada = re.sub(r'AREA\.\s*(.*)', r'', entrada)
            match = re.search(r'SIN\.\s*(.*)', entrada)
            if match:
                sinonimos = match.group(1)
                entrada = re.sub(r'SIN\.\s*(.*)', r'', entrada)
            match = re.search(r'Vid\.\s*(.*)', entrada)
            if match:
                vid = match.group(1)
                entrada = re.sub(r'Vid\.\s*(.*)', r'', entrada)
            match = re.search(r'Nota\.\s*(.*)', entrada)
            if match:
                notas = match.group(1)
                entrada = re.sub(r'Nota\.\s*(.*)', r'', entrada)
            match = re.search(r'VAR\.\s*(.*)', entrada)
            if match:
                variacoes = match.group(1)
                entrada = re.sub(r'VAR\.\s*(.*)', r'', entrada)
            linguas = entrada.split('@ ')
            es = ""
            en = ""
            pt = ""
            la = ""
            for lingua in linguas:
                if lingua.startswith('es'):
                    es = lingua.replace('es', '')
                    es = re.sub(r'\n', r'', es)
                elif lingua.startswith('en'):
                    en = lingua.replace('en', '')
                    en = re.sub(r'\n', r'', en)
                elif lingua.startswith('pt'):
                    pt = lingua.replace('pt', '')
                    pt = re.sub(r'\n', r'', pt)
                elif lingua.startswith('la'):
                    la = lingua.replace('la', '')
                    la = re.sub(r'\n', r'', la)
            dicC[id] = {'termo': termo, 'sexo': sexo, 'area': area, 'notas': notas, 'sinonimos': sinonimos, 'variacoes': variacoes, 'vid': vid, 'es': es, 'en': en, 'pt': pt, 'la': la}
    else:
        match = re.match(r'R\s*(.*)\n', entrada)
        if match:
            termo = match.group(1)
            entrada = re.sub(r'R\s*(.*)\n', r'', entrada)
            vid = ""
            match = re.search(r'Vid\.\s*(.*)', entrada)
            if match:
                vid = match.group(1)
                entrada = re.sub(r'Vid\.\s*(.*)', r'', entrada)
            dicR["r" + str(r)] = {'termo': termo, 'vid': vid}
            r += 1

with open("medicina.json", "w") as outfile:
    json.dump(dicC | dicR, outfile)

with open("medicinaC.json", "w") as outfile:
    json.dump(dicC, outfile)

with open("medicinaR.json", "w") as outfile:
    json.dump(dicR, outfile)

file = open('medicina.txt', 'w')

file.write(texto)
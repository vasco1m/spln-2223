import re

f = open("medicina.txt", "r")
data = f.read()

data = re.sub("\d+\n+Vocabulario", "", data)
data = re.sub("\d+\n+", "", data)

entries = re.findall("([0-9]+[ a-zA-Z\n\t;áàéèíìóòúù\.-]+)", data)

dictCa = {}
dictEs = {}
dictEn = {}
dictPt = {}
dictLa = {}

for entry in entries:
    match = re.match("([0-9]+) ([\w áàéèíìóòúù-]+)([m|f|s|a])\n*\t*([\w áàéèíìóòúù-]+)\n*", entry)
    if match is not None and match.group(2) is not None:
        if match.group(3) is not None and match.group(4) is not None:
            dictCa[match.group(2)] = (match.group(3), match.group(4))
        elif match.group(3) is not None:
            dictCa[match.group(2)] = (match.group(3), None)
        elif match.group(4) is not None:
            dictCa[match.group(2)] = (None, match.group(4))
        else:
            dictCa[match.group(2)] = (None, None)
        matchEs = re.search(r'es (.+)', entry)
        if matchEs is not None and matchEs.group(1) is not None:
            dictEs[match.group(2)] = matchEs.group(1)
        matchEn = re.search(r'en (.+)', entry)
        if matchEn is not None and matchEn.group(1) is not None:
            dictEn[match.group(2)] = matchEn.group(1)
        matchPt = re.search(r'pt (.+)', entry)
        if matchPt is not None and matchPt.group(1) is not None:
            dictPt[match.group(2)] = matchPt.group(1)
        matchLa = re.search(r'la (.+)', entry)
        if matchLa is not None and matchLa.group(1) is not None:
            dictLa[match.group(2)] = matchLa.group(1)
    else:
        continue
        #print(entry)

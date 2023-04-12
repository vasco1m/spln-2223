# Scripting no Processamento de Linguagem Natural

## Trabalho Prático 1 - Módulos

Neste trabalho prático, era-nos proposto que desenvolvêssemos uma pequena ferramenta, explorando módulos Python sugeridos pelos docentes. Os mesmos variam desde bibliotecas para manipulação de texto, processamento de linguagem natural, parsing, entre outros.

O grupo optou por explorar o PyTesseract e o TextBlob, obtendo como resultado final um pequeno script que permite extrair texto de uma imagem e representar o mesmo noutros formatos, bem como traduzi-lo. O programa tem ainda a possibilidade de imprimir informação adicional sobre os dados extraídos.

```bash
usage: pytesseract-test.py [-h] -i IMAGE [-b | --boxes | --no-boxes]
                           [-v | --verbose | --no-verbose]
                           [-o | --orientation | --no-orientation] [-p PDF]
                           [-x XML] [-ho HOCR]
                           [-t | --translate | --no-translate] [-li LANGIN]
                           [-lo LANGOUT]

optional arguments:
  -h, --help            show this help message and exit
  -i IMAGE, --image IMAGE
                        path to input image
  -b, --boxes, --no-boxes
  -v, --verbose, --no-verbose
  -o, --orientation, --no-orientation
  -p PDF, --pdf PDF     Generate pdf
  -x XML, --xml XML     Generate xml
  -ho HOCR, --hocr HOCR
                        Generate hocr
  -t, --translate, --no-translate
  -li LANGIN, --langIn LANGIN
                        language of the original text (default is english)
  -lo LANGOUT, --langOut LANGOUT
                        language of the translated text (default is portuguese)
```

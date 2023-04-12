from PIL import Image
import sys
import pytesseract
from textblob import TextBlob
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-b","--boxes", action=argparse.BooleanOptionalAction)
ap.add_argument("-v", "--verbose", action=argparse.BooleanOptionalAction)
ap.add_argument("-o", "--orientation", action=argparse.BooleanOptionalAction)
ap.add_argument("-p", "--pdf", type=str, default="",
	help="Generate pdf")
ap.add_argument("-x", "--xml", type=str, default="",
    help="Generate xml")
ap.add_argument("-ho", "--hocr", type=str, default="",
    help="Generate hocr")
ap.add_argument("-t", "--translate", action=argparse.BooleanOptionalAction)
ap.add_argument("-li", "--langIn", type=str, default="en",
	help="language of the original text (default is english)")
ap.add_argument("-lo", "--langOut", type=str, default="pt",
    help="language of the translated text (default is portuguese)")
args = vars(ap.parse_args())

try:
    res = pytesseract.image_to_string(Image.open(args["image"]), lang=None)
    if res:
        print(res)
        if args["boxes"]:
            print("Bounding box estimates: ")
            print(pytesseract.image_to_boxes(Image.open(args["image"])))
        if args["verbose"]:
            print("Verbose data: ")
            print(pytesseract.image_to_data(Image.open(args["image"])))
        if args["orientation"]:
            print("Orientation and script detection: ")
            print(pytesseract.image_to_osd(Image.open(args["image"])))
        if args["pdf"]:
            print("Searchable PDF: ", args["pdf"])
            pdf = pytesseract.image_to_pdf_or_hocr(args["image"], extension='pdf')
            with open(args["pdf"], 'w+b') as f:
                f.write(pdf) # pdf type is bytes by default
        if args["xml"]:
            print("XML output: ", args["xml"])
            xml = pytesseract.image_to_alto_xml(args["image"])
            with open(args["xml"], 'w+b') as f:
                f.write(xml)
        if args["hocr"]:
            print("HOCR output: ", args["hocr"])
            hocr = pytesseract.image_to_pdf_or_hocr(args["image"], extension='hocr')
            with open(args["hocr"], 'w+b') as f:
                f.write(hocr)
        if args["translate"]:
            blob = TextBlob(res)
            print("Translated text:")
            translation = blob.translate(from_lang=args["langIn"], to=args["langOut"])
            print(translation)
    else:
        print("No text found")
except RuntimeError as timeout_error:
    print("An error occured")
    pass

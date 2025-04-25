from os import listdir, path, makedirs
from utils import getProccessedPdfs
from tqdm import tqdm
import pypdfium2 as pdfium
import time
from extract_image import extract_DPE_from_image
# Setting ocrmypdf logging to quiet

output_folder = "txt"


def convertToText(input_folder, wb):
    if not path.exists(output_folder):
        makedirs(output_folder)
    if not path.exists(output_folder):
        makedirs(output_folder)
        print("The new directory is created!")
    onlypdf = []
    for f in listdir(input_folder):
        if f.endswith(".pdf"):
            onlypdf.append(f)
    
    ws = wb.active
    PROCESSED_PDFS = getProccessedPdfs(ws)
    wb.close()
    print("Checked if PDFs already in Excel sheet")
    pbar = tqdm(tqdm(onlypdf, ncols=len(onlypdf)))
    for f in pbar:
        pbar.set_description(f"Processing OCR {f}")
        text_file = path.join(output_folder, f.split('.')[0]+".txt")
        if(path.isfile(text_file)):
            continue
        code = (f.split('.')[0].split("_")[0])
        if(code in PROCESSED_PDFS):
            continue
        res = extract_DPE_from_image(path.join(input_folder, f))
        text = generate_with_pdfium(path.join(input_folder, f))
        text += "\n"
        if(res is not None):
            cons,em = res
            text += f"émissions\n{cons}|{em}\n"
        with open(text_file, "+a", encoding="utf-8") as file:
            file.write(text)


def generate_with_pdfium(pdf_file):
    #print(f"generating text with pdfium {pdf_file}")
    final_text = ""
    pdf = pdfium.PdfDocument(pdf_file)
    page1 = pdf[0]
    page7 = pdf[6]
    page8 = pdf[7]

    textpage1 = page1.get_textpage()
    textpage7 = page7.get_textpage()
    textpage8 = page8.get_textpage()

    # Extract text from the whole page
    final_text += textpage1.get_text_range()
    final_text += "\n=SPLIT=\n"
    final_text += textpage7.get_text_range()
    final_text += "\n=SPLIT=\n"
    final_text += textpage8.get_text_range()
    
    return final_text


if __name__ == "__main__":
    print("converting pdf to text")
    start_time = time.time()
    with open("file.txt", "w") as f:
        f.write(generate_with_pdfium(
            "/Users/amirbraham/Desktop/mission/pdf/005008B0001_B0002_DPE_20230703.pdf"))
    print("--- %s seconds ---" % (time.time() - start_time))

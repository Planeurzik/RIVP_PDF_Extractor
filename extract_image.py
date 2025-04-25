import os
import fitz  # PyMuPDF
import io
from PIL import Image
from pytesseract import pytesseract
import time
import cv2
import numpy as np
import re

import sys

if os.name == 'nt':
    if getattr(sys, 'frozen', False):
        tess_path = os.path.join(sys._MEIPASS, "tess/tesseract.exe")
    else:
        tess_path = "tess/tesseract.exe"
    pytesseract.tesseract_cmd = tess_path

    
# Output directory for the extracted images
output_dir = "images"
# Desired output image format
output_format = "png"
margin = 50

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# file path you want to extract images from


def extract_DPE_from_image(pdf):
    page_index = 0
    pdf_file = fitz.open(pdf)
    page = pdf_file[page_index]
    image_list = page.get_images(full=True)
    if(len(image_list) == 0):
        return ""

    # Iterate over the images on the page to get correct image 
    correct_image_index = 4
    img = image_list[correct_image_index]
    ratio = img[2]/img[3] # desired image has a ratio > 1
    if(ratio < 1):
        correct_image_index = 3
        img = image_list[correct_image_index]
    xref = img[0]
    base_image = pdf_file.extract_image(xref)
    image_bytes = base_image["image"]
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert("RGB")
    image = np.array(image) 
    image = image[:, :, ::-1].copy() 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 200)
    contours, hierarchy = cv2.findContours(edged, 
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # getting largest contour , contains the numbers we are looking for
    c_index = 0
    max = 0
    for i in range(len(contours)):
        c = contours[i]
        if(cv2.contourArea(c) > max):
            max = cv2.contourArea(c)
            c_index = i
    #geneating mask to crop contour (eveything else becomes black)
    img = gray
    mask = np.zeros_like(img)
    cv2.drawContours(mask, contours, c_index, 255, -1)
    out = np.zeros_like(img) # Extract out the object and place into output image
    out[mask == 255] = img[mask == 255]

    (y, x) = np.where(mask == 255)
    (topy, topx) = (np.min(y), np.min(x))
    (bottomy, bottomx) = (np.max(y), np.max(x))
    out = out[topy:bottomy+1, topx:bottomx+1]
    

    h = 0
    rows,cols = out.shape
    uthresh=0.85
    lthresh=0.8

    #here we crop image to remove upper region that is mostly black (improves ocr somehow)
    for i in range(rows):
        nb_black_cols= 0
        for j in range(cols):
            k =  out[i,j]
            if(k==0):
                nb_black_cols +=1
        if(nb_black_cols/cols < uthresh and (nb_black_cols / cols) > lthresh):
            h = i

    #print(h)
    crop_img = out
    crop_img = crop_img[h:, :]
    th, im_th = cv2.threshold(crop_img, 128, 255, cv2.THRESH_BINARY)
    #cv2.imshow("img",im_th)
    #cv2.waitKey(0)
    df = pytesseract.image_to_data(im_th,config='--psm 12 -c load_system_dawg=F -c load_freq_dawg=F -c tessedit_char_whitelist=0123456789°',lang='eng', output_type='data.frame')
    df = df[df.conf != -1]
    #print(df)
    if(len(df.index) < 2):
        return None
    
    text_cons = str(df["text"].iloc[0]).split(".")[0] 
    text_em = str(df["text"].iloc[1]).split(".")[0]
    cons = re.sub("[^0-9]", "", text_cons)
    em = re.sub("[^0-9]", "", text_em)
    cons = int(cons)
    em = int(em)

    return (cons,em)


if __name__ == "__main__":
    start_time = time.time()
    i = 0
    for f in os.listdir("pdfa"):
        print(extract_DPE_from_image("pdfa/"+f))
        i+=1
        if(i>2):
            break


    #print(i)

    print("--- %s seconds ---" % (time.time() - start_time))

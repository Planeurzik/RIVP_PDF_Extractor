import os
import tkinter as tk
from tkinter import filedialog, messagebox
from main import scrape
from convert_pdf_to_text import convertToText
import openpyxl
import time
from spinner import Spinner
DEV = False
if(not DEV):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Choose XLSX", "Choisissez le fichier Excel")
    file_path = filedialog.askopenfilename(title = "Select Excel File", filetypes=[("Excel files", ".xlsx .xls")], initialdir='./')
    messagebox.showinfo("Choose PDF", "Choisissez le dossier contenant tous les PDF")
    folder_path = filedialog.askdirectory(title = "Select Folder that contains ALL PDF", initialdir='./')
    if(not os.path.exists(file_path) or not os.path.exists(folder_path)):
        messagebox.showerror("Error", "Vous n'avez pas indiqué un des deux chemins")
        quit()

if(DEV):
    file_path = "excel.xlsx"
    folder_path="pdf"
#print(file_path)
#print(folder_path)
print("converting pdfs to text :")
start_time = time.time()
wb_readonly = openpyxl.load_workbook(file_path,read_only=True)
#print("--- %s seconds ---" % (time.time() - start_time))
convertToText(folder_path,wb_readonly)
#print("--- %s seconds ---" % (time.time() - start_time))
wb_readonly.close()
#print("--- %s seconds ---" % (time.time() - start_time))
print("Scraping the data...")
with Spinner():
    wb = openpyxl.load_workbook(file_path)
    #print("--- %s seconds ---" % (time.time() - start_time))
    scrape(wb)
    #print("--- %s seconds ---" % (time.time() - start_time))
    wb.close()
#print("--- %s seconds ---" % (time.time() - start_time))

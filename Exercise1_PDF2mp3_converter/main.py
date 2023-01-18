#in cmd: python -m pip install pyttsx3
#        python -m pip install pyPDF2

#Global imports
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pyttsx3, PyPDF2

# FUNCTIONS
#gives the user the ability to choose the PDF to be converted
def open_file():
    file = tk.filedialog.askopenfilename(mode = 'r', filetypes = [('PDF Files', '*.pdf')])
    if file is None:
        raise ValueError("File does not exist.")
    return file

#
def pdf_converter(pdf_file,mp3_file):
    pdfreader = PyPDF2.PdfFileReader(open(pdf_file, 'rb'))
    speaker = pyttsx3.init()

    for page_num in range(pdfreader.numPages):
        text = pdfreader.getPage(page_num).extractText()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)

    speaker.save_to_file(clean_text, mp3_file)
    speaker.runAndWait()

    speaker.stop()

#MAIN CODE
 
root= Tk.Tk()
root.withdraw()
pdf_file = open_file()
mp3_file = f"{pdf_file[-4:]}.mp3"
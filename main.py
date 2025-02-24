import pandas as pd #python lib used for working with data sets
import glob #a module in python that's used for file patternmatching.
            #It helps find file paths that match a specific pattern
from fpdf import FPDF
from pathlib import Path #creates a special object that holds the path of the file

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")


    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()


    filename = Path(filepath).stem #to extract the name of the file without the extenstion
    invoice_nr, invoice_date = filename.split("-")
    
    
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

 
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {invoice_date}")

 
    pdf.output(f"PDFs/{filename}.pdf")
import pandas as pd #python lib used for working with data sets
import glob #a module in python that's used for file patternmatching.
            #It helps find file paths that match a specific pattern

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
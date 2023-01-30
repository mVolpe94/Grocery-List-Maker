import pandas as pd
import inflect
import ingredient

PATH = "Kate's Plant Based Meals.xlsx"

data = pd.read_excel(PATH, na_filter="")

cols = data.columns

def get_sheet_names(path=PATH):
  data = pd.ExcelFile(path).sheet_names
  return data

def get_col_names(sheet, path=PATH, na_filter=""):
  data = pd.read_excel(path, sheet, na_filter=na_filter)
  cols = data.columns
  return list(cols)

def get_col_data(colname, sheet, path=PATH):
  df = pd.read_excel(path, sheet, na_filter="")
  data = df[colname].tolist()
  rows = []
  for row in data:
    if row != "":
      rows.append(row)
  return rows

def setup_meal(title, ingredient):
  ...

if __name__ == "__main__":
  sheets = get_sheet_names()
  cols = get_col_names(sheets[0])
  print(get_col_data(cols[2]))
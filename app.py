"""
from tabula import read_pdf
df = read_pdf('bill.pdf',pages='all')
import pdb
pdb.set_trace()
print(df)
"""
import camelot.io as camelot
pdf = camelot.read_pdf('bill.pdf',pages='all')
print(pdf)
dataframe = pdf[0].df
print(dataframe)
import pdb
pdb.set_trace()

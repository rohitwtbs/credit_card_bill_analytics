from tabula import read_pdf
df = read_pdf('credit_bill.pdf',pages='all')
import pdb
pdb.set_trace()
print(df)

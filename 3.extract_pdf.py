import camelot

tables = camelot.read_pdf('table.pdf', pages='1')
print(tables)

tables.export('tablex.csv', f='csv', compress=True)

tables[0].to_csv('tablex.csv')



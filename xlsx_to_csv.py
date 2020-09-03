import xlrd
import csv

def csv_from_excel(xlsx_name, csv_name):
    wb = xlrd.open_workbook(xlsx_name)
    sh = wb.sheet_by_name('1')
    your_csv_file = open(csv_name, 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

# runs the csv_from_excel function:
csv_from_excel("Mag30Aug.xlsx", "Mag30Aug.csv")
csv_from_excel("TOTO30Aug.xlsx", "TOTO30Aug.csv")
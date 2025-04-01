import xlsxwriter
from kovcheg import array

def writer(parametr):
    book = xlsxwriter.Workbook(r"/home/timofey/Documents/write_kovcheg.xlsx")
    page = book.add_worksheet("товар")

    row = 0
    column = 0

    page.set_column('A:A', 20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 20)
    page.set_column('D:D', 20)
    page.set_column('E:E', 20)
    page.set_column('F:F', 20)
    page.set_column('G:G', 20)
    page.set_column('H:H', 20)
    page.set_column('I:I', 20)
    page.set_column('J:J', 20)
    page.set_column('K:K', 20)
    page.set_column('L:L', 20)
    page.set_column('M:M', 20)
    page.set_column('N:N', 20)
    page.set_column('O:O', 20)
    page.set_column('P:P', 20)
    page.set_column('Q:Q', 20)
    page.set_column('R:R', 20)

    
    

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        page.write(row, column+5, item[5])
        page.write(row, column+6, item[6])
        page.write(row, column+7, item[7])
        page.write(row, column+8, item[8])
        page.write(row, column+9, item[9])
        page.write(row, column+10, item[10])
        page.write(row, column+11, item[11])
        page.write(row, column+12, item[12])
        page.write(row, column+13, item[13])
        page.write(row, column+14, item[14])
        page.write(row, column+15, item[15])
        page.write(row, column+16, item[16])
        page.write(row, column+17, item[17])
        row += 1

    book.close()


writer(array)

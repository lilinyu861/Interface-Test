# coding=utf-8

import xlwt


class Writedata(object):
    def __init__(self, save_path):
        self.save_path = save_path

    # 将数据写入excel中
    def data_write(self, save_path, datas):
        book = xlwt.Workbook(encoding="utf-8")
        sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)
        # 将数据写入第i行，第j列
        i = 0
        for data in datas:
            for j in range(len(data)):
                sheet.write(i, j, data[j])
            i += 1
        book.save(self.save_path)

    def data_write_row_col(self, row, col, data):
        book = xlwt.Workbook(encoding="utf-8")
        sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)
        # 将数据写入i行j列
        sheet.write(row, col, data)
        book.save(self.save_path)
'''
s =[[1,2],[0]]
W = Writedata()
W.data_write("../reports/data_origin/1.xls", s)
'''
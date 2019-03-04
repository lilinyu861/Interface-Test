# coding=utf-8

import xlwt


class Writedata(object):
    # 将数据写入excel中
    def data_write(self, save_path, datas):
        book = xlwt.Workbook(encoding="utf-8")
        sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)
        # 将数据写入第i行，第j列
        i = 0
        for data in datas:
            for j in range(len(data)):
                sheet.write(i, j, data[j])
            i += 1
        book.save(save_path)


'''
s =[[1,2],[0]]
W = Writedata()
W.data_write("../reports/data_origin/1.xls", s)
'''
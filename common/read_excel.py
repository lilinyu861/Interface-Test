# coding=utf-8
import xlrd


class ReadExcel(object):
    # 初始化
    def __init__(self, path):
        self.path = path

    # 读取excel中的数据，并将数据按列存储到列表s0，s1中
    # s0中存储测试用例，s1中存储测试用例解释
    def read_and_save_cols_excel(self):
        # 读取测试用例
        data = xlrd.open_workbook(self.path)
        table = data.sheet_by_index(0)
        # ncols存储表格中数据的列数
        ncols = table.ncols

        # 按列存储excel数据到列表s1中
        s0 = []
        title0 = table.row_values(0)
        for i in range(0, ncols, 2):
            s = table.col_values(i)[1:]
            s0.append(s)
        # 按列读取excel测试用例的解释
        s1 = []
        for i in range(1, ncols, 2):
            ss = table.col_values(i)[1:]
            s1.append(ss)

        return s0, s1

    # 读取excel中的数据，并将数据按行存储到列表s2中
    def read_and_save_rows_excel(self):
        # 读取测试用例
        data = xlrd.open_workbook(self.path)
        table = data.sheet_by_index(0)
        # nrows存储表格数据的行数
        nrows = table.nrows

        # 按行存储excel数据到列表s1中
        s2 = []
        title = table.row_values(0)
        for i in range(nrows):
            s = table.row_values(i)[0:]
            s2.append(s)

        return s2

'''
excel = Readexcel("../original-data/data_origin/1.xlsx")
s0, s1 = excel.read_and_save_cols_excel()
print(s0, s1)

excel2 = Readexcel("../original-data/data_origin/1.xlsx")
s2 = excel2.read_and_save_rows_excel()
print(s2)
'''
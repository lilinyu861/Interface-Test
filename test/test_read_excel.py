from common.read_excel import ReadExcel
from common.write_to_excel import Writedata


class Test():
    # 测试读取excel
    def test_read_excel(self):
        excel = ReadExcel("../test/data_origin/test_read_excel.xlsx")
        s0, s1 = excel.read_and_save_cols_excel()
        print(s0, s1)

    # 测试向excel中写数据
    def test_write_xcel(self):
        s = [[1, 2], [0]]
        W = Writedata()
        W.data_write("../test/reports/test_write_excel.xls", s)


if __name__ == '__main__':
    Test().test_read_excel()
    Test().test_write_xcel()
from common.read_excel import ReadExcel

excel = ReadExcel("../data_origin/data_origin/test_read_excel.xlsx")
s0, s1 = excel.read_and_save_cols_excel()
print(s0, s1)

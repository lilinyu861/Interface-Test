from common.write_to_excel import Writedata

s =[[1,2],[0]]
W = Writedata()
W.data_write("../test/reports/test_write_excel.xls", s)
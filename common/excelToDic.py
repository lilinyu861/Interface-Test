import xlrd

'''
通用获取excel数据
返回数据列表，如：[{"name":"张三","age":23},{"name":"李四","age":23}]
'''


class ExcelToDic():
    def __init__(self):
        pass

    # 将excel中数据转换成字典
    def getExcelData(self, excel_path, sheet_name):
        bk = xlrd.open_workbook(excel_path)
        sh = bk.sheet_by_name(sheet_name)
        row_num = sh.nrows
        data_list = []
        for i in range(1, row_num):
            row_data = sh.row_values(i)
            data = {}
            for index, key in enumerate(sh.row_values(0)):
                data[key] = row_data[index]
            data_list.append(data)
        return data_list

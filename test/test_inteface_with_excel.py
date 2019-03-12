"""
接口测试
读取excel中的原始数据，经处理后生成测试用例，利用测试用例对接口进行测试，将接口测试返回结果存放到excel文件中。
"""
from common.generateTestcases import GenerateTestcases
from common.excelToDic import ExcelToDic
from common_data.interfaceUrl import Url
from common.reqMethod import RequestMethod
import xlwt


login_url = Url.login_url
# 原始数据表格位置
origin_excel_path = '../test/data_origin/test_read_excel.xlsx'
# 测试用例数据存放位置
excel_case_1 = '../test/data/test_case_01.xls'
# 测试用例解释数据存放位置
excel_case_2 = '../test/data/test_case_02.xls'
save_path = '../test/reports/report.xls'
g = GenerateTestcases()
# 生成测试用例及测试用例解释的excel文件
g.generate_testcases(origin_excel_path, excel_case_1, excel_case_2)
# 写入的excel
book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)
# 报文头
headers = {
    'Content-Type': 'application/json'
}
# 将测试用例写入excel文件中
test_cases = ExcelToDic().getExcelData(excel_case_1, 'Sheet1')
print(test_cases)
len = len(test_cases)
for i in range(len):
    print(test_cases[i])
    response = RequestMethod().post(interface_url=login_url,
                                    headers=headers,
                                    data=test_cases[i])
    print(i, response)

    # 将数据写入i行j列
    sheet.write(0, 0, 'email')
    sheet.write(0, 1, 'password')
    sheet.write(0, 2, 'response')
    sheet.write(i+1, 0, test_cases[i]['email'])
    sheet.write(i+1, 1, test_cases[i]['password'])
    sheet.write(i+1, 2, response.text)
book.save(save_path)




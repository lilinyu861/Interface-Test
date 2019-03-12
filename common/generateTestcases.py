from common.permutations import Permutations
from common.writeToExcel import Writedata
from common.readExcel import ReadExcel


class GenerateTestcases(object):
    """ read_path 读取文件路径，write_path0 写入测试用例的excel文件路径，write_path1 写入测试用例解释标签的excel路径"""

    def generate_testcases(self, read_path, write_path0, write_path1):
        # 生成排列组合的测试用例和测试用例解释标签
        excel = ReadExcel(read_path)
        s0, s1, title0 = excel.read_and_save_cols_excel()
        # 将测试用例排列组合
        datagroup = s0
        permutations = Permutations(datagroup)
        # 用ss0列表存储排列组合的测试用例
        ss0 = []
        ss0.append([title for title in title0[::2]])
        ss0[1:] = permutations.assemble()
        print(ss0)
        # 将测试用例结束排列组合
        datagroup1 = s1
        permutations1 = Permutations(datagroup1)
        # 用ss1列表存储排列组合的测试用例解释标签
        ss1 = []
        ss1.append([title1 for title1 in title0[1::2]])
        ss1[1:] = permutations1.assemble()
        print(ss1)

        # 将生成的测试用例写入excel中
        Writedata(write_path0).data_write(write_path0, ss0)
        Writedata(write_path1).data_write(write_path1, ss1)

'''
g = Generatetestcases()
g.generate_testcases("../original-data/test/1.xlsx", "../testcases/test/1.xls", '../testcases/test/2.xls')
'''
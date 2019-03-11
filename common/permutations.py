from common.readExcel import *
'''
实现测试用例的排列组合，生成排列组合后的测试用例
'''


class Permutations(object):
    """初始化"""
    def __init__(self, datagroup):
        self.datagroup = datagroup
        # 二维数组从后往前下标值
        self.counterIndex = len(datagroup)-1
        # 每次输出数组数值的下标值数组(初始化为0)
        self.counter = [0 for i in range(0, len(self.datagroup))]

    """计算数组长度"""
    def count_length(self):
        i = 0
        length = 1
        while(i < len(self.datagroup)):
            length *= len(self.datagroup[i])
            i += 1
        return length

    """递归处理输出下标"""
    def handle(self):
        # 定位输出下标数组开始从最后一位递增
        self.counter[self.counterIndex]+=1
        # 判断定位数组最后一位是否超过长度，超过长度，第一次最后一位已遍历结束
        if self.counter[self.counterIndex] >= len(self.datagroup[self.counterIndex]):
            # 重置末位下标
            self.counter[self.counterIndex] = 0
            # 标记counter中前一位
            self.counterIndex -= 1
            # 当标记位大于等于0，递归调用
            if self.counterIndex >= 0:
                self.handle()
            # 重置标记
            self.counterIndex = len(self.datagroup)-1

    """排列组合输出"""
    def assemble(self):
        # 用ss列表存储排列组合后生成的数据
        ss = []
        length = self.count_length()
        i = 0
        while(i < length):
            attrlist = []
            j = 0
            while(j<len(self.datagroup)):
                attrlist.append(self.datagroup[j][self.counter[j]])
                j += 1
            ss.append(attrlist)
            # print(attrlist)
            self.handle()
            i += 1
        return ss


'''
excel = Readexcel('../original-data/test/1.xlsx')
s0, s1 = excel.read_and_save_cols_excel()
# 将测试用例排列组合
datagroup = s0
permutations = Permutations(datagroup)
# 用ss0列表存储排列组合的测试用例
ss0 = permutations.assemble()
print(ss0)
# 将测试用例结束排列组合
datagroup1 = s1
permutations1 = Permutations(datagroup1)
# 用ss1列表存储排列组合的测试用例
ss1 = permutations1.assemble()
print(ss1)
'''
## Interface-Test
自动化接口测试框架

    开发工具：pycharm、Excel、 postman
    接口测试框架：python3+excel+request

测试人员在Excel中列出测试属性并为测试属性设计测试用例值。
各属性的测试用例值设计完成后，此框架会自动化读取excel数据并进行自由组合，
将自由组合后产生的接口测试用例数据写入Excel文件并存放在data文件夹中。

![]()

接口测试时，会去data文件夹中读取Excel中存放的接口测试数据，然后执行自动化接口测试。
并将接口的返回数据写入Excel文件中存放在reports文件夹下。

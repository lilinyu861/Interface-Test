## Interface-Test
#### 自动化接口测试框架

    开发工具：pycharm、Excel、 postman
    接口测试框架：python3+excel+requests
    
#### 自动化接口测试框架结构：
  ![Image text](https://github.com/lilinyu861/Image/blob/master/InterfaceTest/structure.png?raw=true)
  * common 存放公用的方法
  
  * common_data 存放公用的数据
  
  * data 存放测试用例的excel文件
  
  * data_origin 存放原始测试用例的excel文件
  
  * reports 存放记录接口测试用例返回报文的excel文件
  
  * test 测试测试框架的方法能否正常执行
  
  * testcase 存放接口测试编写的测试用例
  

####整个测试框架主要分为两部分：测试用例生成，接口测试执行

一、测试用例的生成：

      1. 用户将存储原始测试用例的excel文件放到data_origin文件夹中；

      2. 编辑接口测试脚本，在接口测试脚本中调用generateTestcase.py文件的generate_testcases方法，生成测试用例并将测试用例写入excel文件存储在data文件夹中。

二、接口测试执行

      1. 接口测试脚本编写，首先读取data文件中的测试用例，并将测试用例生成json格式数据

      2. 调用reqMethod里的请求方法，进行接口测试

      3. 将接口测试返回数据写入excel文件并保存在reports文件夹中。


####测试流程如下所示：
1 首先由用户设计原始的测试用例并为测试用例写用例注解，将原始测试用例写入excel文件中保存到data_origin文件夹中

示例如下：
![Image text](https://github.com/lilinyu861/Image/blob/master/InterfaceTest/origin_data.png?raw=true)

2 调用common文件夹中的generateTestcases.py中的generate_testcases()方法，
向方法中传入参数，参数内容包括原始测试用例excel文件位置，
生成测试用例excel文件后的保存位置，生成测试用例注解excel文件后的保存位置

示例如下：

生成的测试用例excel文件

![Image text](https://github.com/lilinyu861/Image/blob/master/InterfaceTest/testcase.png?raw=true)

生成测试用例注解excel文件

![Image text](https://github.com/lilinyu861/Image/blob/master/InterfaceTest/testcase_mean.png?raw=true)

3 测试用例生成之后，可以编辑接口测试代码，执行接口测试，然后将测试用例的数据写入excel文件中并存储在reports文件夹中。   

示例如下：
![Image text](https://github.com/lilinyu861/Image/blob/master/InterfaceTest/response.png?raw=true)

###common文件夹
common文件夹中写入了很多方法，其中有reqMethod.py,这个文件中存放了我目前接触到的
接口请求方法，有get、post、put、patch、delete等以及需要session验证的这些接口请求方法。

此框架在生成测试用例时，将用户定义的原始测试数据进行排列组合后生成测试用例并将测试用例写入
excel文件中，generateTestcases.py文件中的生成测试用例方法会返回已经生成json结构的测试用例数组，
写接口测试时可直接调用。

为了方便接口测试，我们将公用数据写入common_data文件夹中，例如接口地址。

####详细的框架使用可以参见test文件夹中的测试用例。
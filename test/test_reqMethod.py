from data.interfaceUrl import Url
from common.reqMethod import RequestMethod
import unittest
import warnings


class TestMethod(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.url = Url.baidu_url
        self.headers = None
        self.data = None

    def tearDown(self):
        print(self.response.text)

    def test_baidu(self):
        self.response = RequestMethod().get(interface_url=self.url)
        print(self.response.url)
        self.assertEqual(200, self.response.status_code)


if __name__ == '__main__':
    unittest.main()
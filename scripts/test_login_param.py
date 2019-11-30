"""
一个参数的参数化
"""


import pytest


class TestLogin:

    @pytest.mark.parametrize("data",[2,4])  # data参数被赋予两个值，函数会运⾏两遍
    def test_login_1(self,data):  # 参数必须和parametrize⾥⾯的参数⼀致9
        """记住密码登录"""
        print("test data:a=%d" % data)
        #assert data % 2 == 2



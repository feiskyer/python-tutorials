#coding: utf8
"""
    pip install nose

    运行测试：
        nosetests
        选项：
        -w ，指定一个目录运行测试。目录可以是相对路径或绝对路径。
        -s，不捕获输出，会让你的程序里面的一些命令行上的输出显示出来。例如print所输出的内容。
        -v，查看nose的运行信息和调试信息。例如会给出当前正在运行哪个测试。

    nose在文件中如果找到函数setup, setup_module, setUp 或者setUpModule等，
    那么会在该模块的所有测试执行之前执行该函数。
    如果找到函数 teardown,tearDown, teardown_module或者 tearDownModule等，
    那么会在该模块所有的测试执行完之后执行该函数。
"""
from nose.tools import with_setup
import nose

def setUp():
    print "function setup"


def tearDown():
    print "function teardown"


def TestFunc1():
    print "Test func1"
    assert True


def TestFunc2():
    print "Test func2"
    assert True


def func3Start():
    print "Func3 start"
    assert True


def func3End():
    print "Func3 end"
    assert True


@with_setup(func3Start, func3End)
def TestFunc3():
    print "Test func3"
    assert True


class TestClass():
    arr1 = 2
    arr2 = 2

    def setUp(self):
        self.arr1 = 1
        self.arr2 = 3
        print "MyTestClass setup"

    def tearDown(self):
        print "MyTestClass teardown"

    def TestFunc4(self):
        assert self.arr1 != self.arr2

    def TestFunc5(self):
        assert self.arr1 == 1


if __name__ == '__main__':
    nose.runmodule(argv=[__file__, '--with-doctest', '-vv'])

# encoding=utf-8

def f1():
    pass


class Test1:
    '测试类'
    staticNum = 1
    __staticNum2 = 2

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def displayTest(self):
        print self.name, self.__salary, Test1.staticNum

    @staticmethod
    def displayStatic():
        Test1.printd(Test1.__staticNum2)

    @staticmethod
    def printd(s):
        print s


# 有class object, instance object, method object, function object
print("The attr staticNum of class object ", Test1.staticNum)
test1 = Test1("david", 100000)
print("The attr name of instance object ", test1.name)
print("The attr __module__ of method object displayTest of instance object ", test1.displayTest.__module__)
print("The attr name of fucntion object ", f1.func_name)

test = Test1("d", 2)
test.displayTest();
print test.name
print Test1.staticNum
# __开头的变量为private的,不能再外部直接引用
# print Test.__staticNum2
# print test.__salary

# TypeError: unbound method displayTest() must be called with Test instance as first argument (got nothing instead),采用类名调用为unbound,则第一个参数为required
# Test.displayTest()

print test.__doc__
print Test1.__doc__

print Test1.displayStatic()


class Test2(Test1):
    t2 = 3;


print("Test2.t2", Test2.t2)
print("Test2.staticNum", Test2.staticNum)


def test3():
    # UnboundLocalError: local variable 'i' referenced before assignment   对于函数中的变量是有声明提前的预处理的类似于javascript。注意是声明提前,赋值还在原位执行。  注意i和j所报的错误是不同的
    # print(i)
    # i=0
    # NameError: global name 'j' is not defined
    # print(j)
    pass


test3()
# 全局变量是没有声明提前的预处理的
# print(z)
# z=0




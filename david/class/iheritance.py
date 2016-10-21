# encoding=utf-8
class base():
    v = "base"
    '''
    def f1(self, m):
        print(m);
    '''

    def f1(self):
        print("In class base ", self.v)


class subclass1(base):
    v = "subclass1"

    def f1(self):
        super().f1();
        print("In class subclass1 ", self.v)


class subclass2(base):
    v = "subclass2"

    def f1(self):
        super().f1();
        print("In class subclass2 ", self.v)


class subclass3(subclass1, subclass2):
    v = "subclass3"

    def f1(self):
        super().f1()  # 相当于super(subclass3, self),这种没有参数(隐式注入)的形式,只能在类内部使用
        print("In class ", self.v)


d = subclass1()
'''
d.f1(1)
TypeError: f1() takes 1 positional argument but 2 were given 后面一个定义起作用,因此报异常, python不支持overload
'''
print("1 ==========")
d.f1()
print("1 ==========")

d3 = subclass3()
print("2 ==========")
d3.f1()  # 在执行过程中是按照定义时的类签名基类生命顺序执行的. 在某个基类中如果没有super的调用则迭代终止,如果将subclass2中的f1中的super注释掉,则base中的f1不会被调用
print("2 ==========")

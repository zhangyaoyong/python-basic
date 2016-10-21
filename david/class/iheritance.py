# encoding=utf-8

i = 9
j = 9


class Base:
    v = "Base"
    '''
    def f1(self, m):
        print(m);
    '''

    def f1(self):
        print("In class Base ", self.v)


class Subclass1(Base):
    v = "Subclass1"

    def f1(self):
        super().f1();
        print("In class Subclass1 ", self.v)


class Subclass2(Base):
    v = "Subclass2"

    def f1(self):
        super().f1();
        print("In class Subclass2 ", self.v)


class Subclass3(Subclass1, Subclass2):
    v = "Subclass3"

    def f1(self):
        super().f1()  # 相当于super(Subclass3, self),这种没有参数(隐式注入)的形式,只能在类内部使用
        print("In class ", self.v)


d = Subclass1()
'''
d.f1(1)
TypeError: f1() takes 1 positional argument but 2 were given 后面一个定义起作用,因此报异常, python不支持overload
'''
print("1 ==========")
d.f1()
print("1 ++++++++++")

d3 = Subclass3()
print("2 ==========")
d3.f1()
'''
1 在执行过程中是按照定义时的类签名基类生命顺序执行的.
2 在某个基类中如果没有super的调用则迭代终止,如果将subclass2中的f1中的super注释掉,则base中的f1不会被调用
3 在super的整个调用过程中self指向的都是当前对象,不是父类的一个实例,和java是一直的,依据是各个层次的输出中self.v都是subclass3
'''
print("2 ++++++++++")

# encoding=utf-8
i = 9
j = 9


class visibility1:
    def get_global_var(self):
        global i  # 如果只是读取全局变量则直接引用即可,但是如果需要修改则先需要用global i 表明引用的是全局变量而不是生成的local变量
        i = 19
        print("in method i=", i, ", j=", j)


v = visibility1()
v.get_global_var()
print("out method i=", i, ", j=", j)


def enclosing():
    m = 10
    n = 10

    class visibility2:
        def get_enclosing_var(self):
            nonlocal m
            nonlocal n
            print("m=", m, ", n=", n)
            m = 11  # 改变了enclosing的变量的值
            n = 11

    return visibility2()


v2 = enclosing()
v2.get_enclosing_var()  # 因为v2是通过enclosing的一次执行得到的对象,与外层的enclosing变量形成的一个clousre,因此第二次调用看到的是11
v2.get_enclosing_var()
v3 = enclosing()
v3.get_enclosing_var()  # v3是enclosing的另一次执行得到的对象,有新初始化后的enclosing变量形成的一个closure,因此看到的是10

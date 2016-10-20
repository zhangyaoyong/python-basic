#!/bin/python
#encoding=utf-8
#实验结论python和java一样实质上也是按值传递


def assignBasic(arg1):
    '实验参数按引用传递还是按值传递---基础类型'
    arg1=2
    return
var1=1
assignBasic(var1)
print var1

def assignPrimum(arg1):
    '实验参数按引用传递还是按值传递---对象类型'
    arg1=[5,6,7,8]
    return
list1=[1,2,3,4]
assignPrimum(list1)
print(list1)



def returnTest():
    '多个返回值即为元组'
    return 4,5,6
returnValue=returnTest()
print type(returnValue)



lambdaFunc=lambda a,b : a+b
print(lambdaFunc(1,2))


#貌似与基础教程的相反,可以访问全局命名空间的c-----是的, 如果是引用时可以直接引用全局值的;但是如果是赋值就会产生一个新的local变量,如果不加global关键字的话
c=5
lambdaFunc2=lambda a,b : a+b+c
print(lambdaFunc2(1,2))

g1=3
g2=4
def variableVisibleTest():
    print("g1 in function is ", g1)
    g2=0
    print("g2 in functino is ", g2)
variableVisibleTest()
print(g1, g2)

#闭包的概念, fInner如果对于vOuter有修改,会被传播到fTest的多次调用中吗??

def fOuter():
    vOuter=5
    def fInner():
        print vOuter
    return fInner

fTest=fOuter()
fTest()
fTest()










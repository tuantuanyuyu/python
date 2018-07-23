#1. 程式包裝
#1.1 把九九乘法表包裝成函式，可做n1*n2乘法
def prod(a,b):
    print(a,"*",b,"=",a*b)
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
prod(a,b)

#1.2 把四則運算機包裝成函式
def cal(a,b,op):
    if op=="+":
        print(a,op,b,"=",a+b)
    elif op=="-":
        print(a,op,b,"=",a-b)
    elif op=="*":
        print(a,op,b,"=",a*b)
    elif op=="/":
        print(a,op,b,"=",a/b)
    else:
        print("運算符號錯誤")            
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
op=input("運算符號:")
cal(a,b,op)

#1.3 將以上函式包裝在你自己的模組和封包中，並在主程式成功使用
import lib.product as a
a.prod(3,5)
import lib.calculator as b
b.cal(3,5,"/")

#2. 使用系統內建的模組 random產生1~100間的亂數
import random
num=list(range(1,101))
random.shuffle(num)
print(num)
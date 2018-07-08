#四則運算
n1=int(input("Enter a Number:"))
n2=int(input("Enter a Number:"))
op=str(input("運算:+,-,*,/:"))
if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
#開根號
n=int(input("輸入一個正整數:"))
for a in range(1,10**100):
    if a*a==n:
        print("整數平方根:",a)
        break
    elif a > n:
        print("整數平方根:沒有")
        break
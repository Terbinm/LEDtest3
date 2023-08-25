# function.py

def multiply(a, b):
    return a * b

# main.py

from function import multiply

while True:
    print("運算方式：")
    print("1. 乘法")
    print("2. 退出")

    choice = input("選擇運算方式（1/2）：")

    if choice == '2':
        print("退出功能")
        break

    num1 = float(input("輸入第一個數字："))
    num2 = float(input("輸入第二個數字："))

    if choice == '1':
        print("結果：", multiply(num1, num2))
    else:
        print("輸入無效")

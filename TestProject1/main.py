from C110118142add import add
from divide import divide
from subtract import subtract
from multiply1 import multiply

#次方
def cf(x, y):
    return x ** y

    


while True:
    # 用户輸入
    print("運算方式：")
    print("1. 相加")
    print("2. 相减")
    print("3. 相乘")
    print("4. 相除")
    print("5. 次方")
    print("6. 退出")

    choice = input("選擇運算方式（1/2/3/4/5/6）：")

    if choice == '6':
        print("退出功能")
        break

    num1 = float(input("輸入第一個數字："))
    num2 = float(input("輸入第二個數字："))

    if choice == '1':
        print("結果：", add(num1, num2))
    elif choice == '2':
        print("結果：", subtract(num1, num2))
    elif choice == '3':
        print("結果：", multiply(num1, num2))
    elif choice == '4':
        print("結果：", cf(num1, num2))
    elif choice == '5':
        print("結果：", divide(num1, num2))
    else:
        print("輸入無效")
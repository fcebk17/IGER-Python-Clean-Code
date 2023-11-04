try:
    a = int(input("請輸入分母: "))
    print(10 / a)
except ValueError:
    print("請輸入數字")
except ZeroDivisionError:
    print("分母不可為0")
except:
    print("這邊發生了一些錯誤")
try:
    a = int(input("請輸入任意數字: "))
    print(a + 1)
except:
    print("Oops! 發生了一些錯誤")
else:
    print("沒有發生錯誤")
finally:
    print("不管有沒有發生錯誤，都會執行這裡")
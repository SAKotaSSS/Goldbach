import numpy as np
import random

for _ in range(6):
    # 乱数を生成し，画面に表示
    cn = 2 * random.randint(2, 10)
    print(cn)
    while True:
        # 二つの数を受け取り，素数か判定，その後足して等しいか確認
        a = int(input("素数１："))
        b = int(input("素数２："))
        for n in range(2, int(np.sqrt(a) + 1)):
            if a % n == 0:
                print(f"{a}は素数じゃない！")
                break
            if a <= 1:
                print(f"{a}は素数じゃない！")
                break
        for n in range(2, int(np.sqrt(b) + 1)):
            if b % n == 0:
                print(f"{b}は素数じゃない！")
                break
            if a <= 1:
                print(f"{a}は素数じゃない！")
                break

        if a + b == cn:
            print("正解！")
            break
        else:
            print("もう一回！")

print("おつかれさま～")
import random

def guess_number():
    # 生成一个1到100之间的随机数
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个1到100之间的数字，请猜猜是多少。")

    while guess != number_to_guess:
        try:
            guess = int(input("请输入你的猜测: "))
            attempts += 1

            if guess < number_to_guess:
                print("太低了，再试一次！")
            elif guess > number_to_guess:
                print("太高了，再试一次！")
            else:
                print(f"恭喜你，猜对了！你总共尝试了{attempts}次。")
        except ValueError:
            print("请输入一个有效的整数。")

if __name__ == "__main__":
    guess_number()
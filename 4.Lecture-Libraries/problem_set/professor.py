import random


def main():
    level = get_level()
    x, y= generate_integer(level)
    score = 0
    for i in range(10):
        mat = x[i] + y[i]
        attempts = 0
        while attempts < 3:
            ans = input("{} + {} = ".format(x[i], y[i]))
            try:
                if int(ans) == mat:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1
        if attempts == 3:
            print("{} + {} = {}".format(x[i], y[i], mat))
    print(f"{score}")



def get_level():
    levels = [1,2,3]
    while True:
        try:
            level = int(input("Level: "))
            if level in levels :
                return level
                break
        except ValueError:
            level = input("Level: ")


def generate_integer(level):
    x_num = []
    y_num = []
    if level == 1:
        ran_num1 = 0
        ran_num2 = 9
    elif level == 2:
        ran_num1 = 10
        ran_num2 = 99
    else:
        ran_num1 = 100
        ran_num2 = 999
    for i in range(10):
       x = random.randint(ran_num1,ran_num2)
       y = random.randint(ran_num1,ran_num2)
       x_num.append(int(x))
       y_num.append(int(y))
    return(x_num, y_num)


if __name__ == "__main__":
    main()

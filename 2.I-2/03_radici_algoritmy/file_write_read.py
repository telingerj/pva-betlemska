import random

def gen_nums(count):
    with open("nums", "w") as f:
        for i in range(count):
            if i > 0:
                f.write("\n")
            num = str(random.randint(1, count))
            f.write(num)


def read_nums():
    with open("nums", "r") as f:
        return list(map(int, f.read().split("\n")))

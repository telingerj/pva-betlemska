import random

def generate_nums(filename):
    with open(filename, "w") as f:
        for i in range(20000):
            if i != 0:
                f.write("\n")
            num = random.randint(1, 10000)
            f.write(str(num))


def read_nums(filename):
    with open(filename, "r") as f:
        return list(map(int, f.read().split("\n")))
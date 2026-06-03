import random;  prefix = ""; suffix = ""

def generate(numbers, amount):
    for i in range(0, amount):
        # default, custom
        global num;  num = ["1","2","3","4","5","6","7","8","9"];  num1 = ["",""]

        random.shuffle(num);  string = "";  string += prefix

        for i in range(0, numbers):
            string += num.pop()

        string += suffix;  print(f"\n{string}\n")

generate(9, 5)
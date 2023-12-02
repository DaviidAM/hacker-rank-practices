from ..common.custom_input import input2
from .tests import TEST1

# python3 -m python.nested_list.my_solution

TEST = TEST1

if __name__ == '__main__':
    for _ in range(int(input2(TEST))):
        name = input2(TEST)
        score = float(input2(TEST))
        print(name, score)
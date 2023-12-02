
from ..common.custom_input import input2
from .tests import TEST1

if __name__ == '__main__':
    for _ in range(int(input2(TEST1))):
        name = input2(TEST1)
        score = float(input2(TEST1))
        print(name, score)
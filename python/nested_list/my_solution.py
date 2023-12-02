from copy import deepcopy
from ..common.custom_input import input2
from .tests import TEST1, TEST8

# python3 -m python.nested_list.my_solution

TEST = TEST1

class ScoreNames():

    score: float
    names:list[str]

    def __init__(self):
        # Assuming max note is 100
        self.score = 100
        self.names = []

if __name__ == '__main__':
    lowest = ScoreNames()
    second = ScoreNames()
    for _ in range(int(input2(TEST))):
        
        # Read values
        name = input2(TEST)
        score = float(input2(TEST))
        
        # Solution
        if score < lowest.score:
            second = deepcopy(lowest)
            lowest.score = score
            lowest.names = [name]
        elif score == lowest.score:
            lowest.names.append(name)
        else:
            if score < second.score:
                second.score = score
                second.names = [name]
            elif score == second.score:
                second.names.append(name)

    for answer in sorted(second.names):
        print(answer)




ITERATION: int = 0

def input2 (test_list:list):
    global ITERATION
    value = test_list[ITERATION]
    ITERATION += 1
    return value
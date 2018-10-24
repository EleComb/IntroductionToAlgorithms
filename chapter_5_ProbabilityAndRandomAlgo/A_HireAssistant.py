import random


def hire_assistant(n):
    best = 0
    best_i = 0
    times = 0
    for i in range(n):
        candidate_i = random.random()
        if candidate_i > best:
            best = candidate_i
            best_i = i
            times += 1

    print('number', best_i, 'candidate get', best, 'score. interview' , times, '/', n, 'times.')


hire_assistant(10)
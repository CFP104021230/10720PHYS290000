"""
Salary Game, Apr. 9, 2019.
Copyright @ Wei-Chih Huang (noctildon2@gmail.com)
"""

import random
import matplotlib.pylab as plt


# fitler the students who are already bankrupt(game over)
def check_bankrupt(students):
    return list(filter(lambda x: x > 0, students))


# randomly pick two students, start the gamble, then return the result of the gamble
def gambling(students):
    random.shuffle(students)
    gamble = random.randint(1, 3)
    if gamble == 1:
        students[0] += bet
        students[1] -= bet
    elif gamble == 2:
        students[0] -= bet
        students[1] += bet

    return students


def plot_it(students):
    plt.hist(students, bins='auto')
    plt.xlabel('Balance')
    plt.ylabel('Student Number')
    plt.show()


if __name__ == "__main__":
    # intialize
    student_num = 10
    intial_balance = 40
    bet = 10
    times = 30
    students = [intial_balance] * student_num

    for _ in range(times):
        students = check_bankrupt(students)
        students = gambling(students)

    # print the result after the whole game
    print(students)
    # plot the result in histogram
    plot_it(students)

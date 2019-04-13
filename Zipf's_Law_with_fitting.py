"""
Word survey with fitting, Apr. 13, 2019.
Copyright @ Wei-Chih Huang (noctildon2@gmail.com)
"""

from collections import Counter
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


with open('Alice.txt', 'r', encoding='UTF-8') as f:
    def fit_func(x, c, p):
        # y = c * x^p
        return c * np.power(x, p)

    def plot_it(x, y):
        plt.plot(x, y)
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('Rank of the word')
        plt.ylabel('Number of the occurance')
        plt.show()

    f_content = f.read()
    f_content_list = f_content.split()
    # print(f_content_list)

    word_dict = Counter(f_content_list)
    sorted_word_dict = word_dict.most_common()

    word_count = [sorted_word_dict[_][1] for _ in range(len(sorted_word_dict))]
    # print(word_count)

    x_data = range(len(sorted_word_dict))
    y_data = word_count

    # print best fit value
    params, params_covariance = curve_fit(fit_func, x_data, y_data)
    print('parameters:', params)
    print('covariance of parameters:', params_covariance)

    # plot_it(x_data, y_data)

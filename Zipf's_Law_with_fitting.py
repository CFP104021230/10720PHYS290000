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
        # y1 = c * np.power(x, p)  # power law
        y2 = c + p * x  # log scale of power law
        return y2

    def plot_it(x, y):
        plt.plot(x, y)
        plt.xlabel('Rank of the word')
        plt.ylabel('Number of the occurance')
        plt.suptitle('Log scale')
        plt.show()

    def plot_fitting(x_data, y_data):
        params, params_covariance = curve_fit(fit_func, x_data, y_data)
        fit_y_data = fit_func(x_data, *params)
        plt.plot(x_data, fit_y_data)
        return params, params_covariance

    f_content = f.read()
    f_content_list = f_content.split()

    word_dict = Counter(f_content_list)
    sorted_word_dict = word_dict.most_common()
    words_numer = len(sorted_word_dict)
    word_count = [sorted_word_dict[_][1] for _ in range(words_numer)]

    # original data
    x_data = np.array(range(words_numer))
    y_data = np.array(word_count)

    # log of original data
    x_data_log = np.log(x_data + 1)  # fix log(0)
    y_data_log = np.log(y_data)

    params, params_covariance = plot_fitting(x_data_log, y_data_log)

    output_paramters_string = '''
    Parameters
        amp:   {:.3f}
        alpha: {:.3f}
    '''.format(np.exp(params[0]), params[1])

    output_covariance_string = '''
    Covariance of parameters
        amp:   {:+.3e}, {:+.3e}
        alpha: {:+.3e}, {:+.3e}
    '''.format(np.exp(params_covariance[0][0]), np.exp(params_covariance[0][1]),
               params_covariance[1][0], params_covariance[1][1])

    print(output_paramters_string)
    print(output_covariance_string)

    plot_it(x_data_log, y_data_log)

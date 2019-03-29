"""
Word survey, Mar. 28, 2019.
Copyright @ Wei-Chih Huang (noctildon2@gmail.com)
"""

# ref : https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter
import matplotlib.pyplot as plt

with open('homework/Alice.txt', 'r', encoding='UTF-8') as f:
    def plotLog(x, y):
        plt.plot(x, y)
        plt.xscale('log')
        plt.yscale('log')
        plt.show()

    f_content = f.read()
    f_content_list = f_content.split()
    # print(f_content_list)

    word_dict = Counter(f_content_list)
    sorted_word_dict = word_dict.most_common()

    word_count = [sorted_word_dict[_][1] for _ in range(len(sorted_word_dict))]
    print(word_count)

    plotLog(range(len(sorted_word_dict)), word_count)

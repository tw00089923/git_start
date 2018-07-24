"""An Example to get familiar with git and python"""
from __future__ import print_function, absolute_import, unicode_literals
import cProfile


def build_square_numbers(n):
    for i in range(n):
        yield i*i

if __name__ == '__main__':
    # 1st benchmark
    cProfile.run('build_square_numbers(10000000)')
    # 2nd benchmark
    cProfile.run('list(build_square_numbers(10000000))')
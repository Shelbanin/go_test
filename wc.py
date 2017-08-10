# coding: utf-8

import sys


def line_count(path):
    try:
        with open(path) as f:
            lines_amount = reduce(lambda acc, l: acc + 1, f, 0)
            print('{} {}'.format(lines_amount, path))
    except IOError:
        print('File {} does not exists'.format(path))


if __name__ == '__main__':
    line_count(sys.argv[1])

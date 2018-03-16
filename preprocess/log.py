# !/usr/bin/env python
# coding: utf-8

import os
import re
from os.path import join

folder = '/var/py/cache/logs'
output = './source/q1q2'

answer_feeds = []


def clean(text):
    return re.sub('[?!,.……。，！？\\\/\[\]\{\}【】：:<>《》“”""\+\-`~%\$·_——～# 。？（）、；\s]+', '', text.lower())


def walk(folder, filter=None):
    for folder, children, files in os.walk(folder):
        for file in files:
            path = '{folder}/{file}'.format(folder=folder, file=file)
            if filter:
                if filter in path:
                    yield path, file
            else:
                yield path, file


block_list = ['#Delay', '#Goodbye', '#Proactive', '#Welcome']


def block(string):
    for item in block_list:
        if item in string:
            return True
    return False


def pairs():
    for path, file in walk(folder):
        try:
            with open(path, encoding='utf-8') as f:
                last_line = None
                f.readline()
                for line in f.readlines():
                    if not last_line:
                        last_line = line
                        continue
                    q1 = last_line.split('\t')[0].strip()
                    q2 = line.split('\t')[0].strip()
                    if block(q2):
                        continue
                    if not block(q1):
                        yield clean(q1), clean(q2)
                    last_line = line
        except UnicodeDecodeError:
            print('UnicodeDecodeError')


def main():
    q1_output = open(join(output, 'log_post.txt'), 'w')
    q2_output = open(join(output, 'log_cmnt.txt'), 'w')
    for q1, q2 in pairs():
        q1_output.write('\t'.join(list(q1)) + '\n')
        q2_output.write('\t'.join(list(q2)) + '\n')
    q1_output.close()
    q2_output.close()


if __name__ == '__main__':
    main()

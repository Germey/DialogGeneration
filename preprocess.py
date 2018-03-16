import subprocess
from os.path import join
import time
from pandas import Series
import json
from config import UNK, EOS, GO

output = './dataset/q1q2'
folder = './source/q1q2'

file_pairs = [
    ('log_post.txt', 'log_cmnt.txt'),
    ('input_post.txt', 'input_cmnt.txt')
]

post_output = 'request.txt'
cmnt_output = 'response.txt'


def line_number(file, folder=folder):
    result = subprocess.Popen('wc -l ' + join(folder, file), shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
    return result.stdout.read().decode('utf-8').strip()


post_output_file = open(join(output, post_output), 'w', encoding='utf-8')
cmnt_output_file = open(join(output, cmnt_output), 'w', encoding='utf-8')

for post, cmnt in file_pairs:
    post_file = open(join(folder, post), encoding='utf-8')
    cmnt_file = open(join(folder, cmnt), encoding='utf-8')
    
    for line in post_file.readlines():
        post_output_file.write(line.strip() + '\n')
    for line in cmnt_file.readlines():
        cmnt_output_file.write(line.strip() + '\n')

time.sleep(1)

print(line_number(post_output, output))
print(line_number(cmnt_output, output))

vocabs = []

with open(join(folder, 'post_vocab.txt')) as f:
    f.readline()
    f.readline()
    for line in f.readlines():
        vocabs.append(line.strip())
    vocabs.insert(0, UNK)
    vocabs.insert(0, EOS)
    vocabs.insert(0, GO)

s = Series(range(len(vocabs)), index=vocabs)
print(s.to_dict())

with open(join(output, 'vocab.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps(s.to_dict(), ensure_ascii=False))

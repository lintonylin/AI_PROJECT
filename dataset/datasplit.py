import codecs
from tqdm import tqdm
import random

file = codecs.open("Haikus_result_manual_refine.txt", 'r', encoding='utf-8')

poems = []
poem = []
for line in tqdm(file):
    line = line.strip().replace('\n', '')
    if len(line) != 0:
        poem.append(line)
    else:
        if len(poem) != 0:
            poems.append(poem)
            poem = []

train_nums = int(len(poems) * 0.8)
valid_nums = int(len(poems) * 0.1)
test_nums = int(len(poems) * 0.1)

train = []
valid = []
test = []
while train_nums != 0:
    num = random.randint(0, len(poems)-1)
    if num not in train and num not in valid and num not in test:
        train.append(num)
    train_nums = train_nums - 1
while valid_nums != 0:
    num = random.randint(0, len(poems)-1)
    if num not in train and num not in valid and num not in test:
        valid.append(num)
    valid_nums = valid_nums - 1
while test_nums != 0:
    num = random.randint(0, len(poems)-1)
    if num not in train and num not in valid and num not in test:
        test.append(num)
    test_nums = test_nums - 1

train_file = codecs.open('Haikus_train.txt', 'w', encoding='utf-8')
valid_file = codecs.open('Haikus_valid.txt', 'w', encoding='utf-8')
test_file = codecs.open('Haikus_test.txt', 'w', encoding='utf-8')
for num in train:
    for line in poems[num]:
        train_file.write(line)
        train_file.write('\n')
    train_file.write('\n')
for num in test:
    for line in poems[num]:
        test_file.write(line)
        test_file.write('\n')
    test_file.write('\n')
for num in valid:
    for line in poems[num]:
        valid_file.write(line)
        valid_file.write('\n')
    valid_file.write('\n')
file.close()
train_file.close()
valid_file.close()
test_file.close()

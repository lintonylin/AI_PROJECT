import codecs
from tqdm import tqdm

train_output = codecs.open('haiku.txt', 'w', encoding='utf-8')
test_output = codecs.open('haiku_test.txt', 'w', encoding='utf-8')
file = codecs.open('../Haikus_train.txt', 'r', encoding='utf-8')
valid = codecs.open('../Haikus_valid.txt', 'r', encoding='utf-8')
test = codecs.open('../Haikus_test.txt', 'r', encoding='utf-8')
poem = []
for lines in tqdm(file):
    line = lines.strip().replace('\n', '')
    if len(line) != 0:
        poem.append(line)
    else:
        if len(poem) != 3:
            continue
        train_output.write(poem[0]+' + '+poem[1]+' + '+poem[2]+'\n')
        poem = []
poem = []
for lines in tqdm(valid):
    line = lines.strip().replace('\n', '')
    if len(line) != 0:
        poem.append(line)
    else:
        if len(poem) != 3:
            continue
        test_output.write(poem[0]+' + '+poem[1]+' + '+poem[2]+'\n')
        poem = []
poem = []
for lines in tqdm(test):
    line = lines.strip().replace('\n', '')
    if len(line) != 0:
        poem.append(line)
    else:
        if len(poem) != 3:
            continue
        test_output.write(poem[0]+' + '+poem[1]+' + '+poem[2]+'\n')
        poem = []

train_output.close()
test_output.close()
file.close()
valid.close()
test.close()

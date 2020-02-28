import codecs
from tqdm import tqdm
import numpy as np

seqgan = codecs.open('seqgan.txt', 'r', encoding='utf-8')

epochs = []
BLEU3 = []

for lines in seqgan:
    line = lines.strip().replace('\n', '')
    if 'ADV EPOCH' in line:
        strs = line.split(' ')
        epoch = int(strs[2])
        epochs.append(epoch)
    if 'g_loss' in line:
        strs = line.split(' ')
        BLEU3.append(strs[6].replace('[', '').replace(']', '').replace(',', ''))

print('seqGAN')
print(BLEU3)
print(max(BLEU3))
print(np.argmax(BLEU3))
print(epochs[np.argmax(BLEU3)])
print('\n\n\n')
seqgan.close()


relgan = codecs.open('relgan.txt', 'r', encoding='utf-8')

epochs = []
BLEU3 = []

for lines in relgan:
    line = lines.strip().replace('\n', '')
    if '[ADV]' in line:
        strs = line.split(' ')
        epoch = int(strs[2].replace(':', ''))
        epochs.append(epoch)
        BLEU3.append(strs[13].replace(',', ''))

print('relGAN')
print(BLEU3)
print(max(BLEU3))
print(np.argmax(BLEU3))
print(epochs[np.argmax(BLEU3)])
print('\n\n\n')
relgan.close()


leakgan = codecs.open('leakgan.txt', 'r', encoding='utf-8')

epoch = 0
BLEU3 = []

for lines in leakgan:
    line = lines.strip().replace('\n', '')
    if '[ADV-GEN]' in line:
        strs = line.split(' ')
        BLEU3.append(strs[9].replace(',', ''))

print('leakGAN')
print(BLEU3)
print(max(BLEU3))
print(np.argmax(BLEU3))
print('\n\n\n')
leakgan.close()
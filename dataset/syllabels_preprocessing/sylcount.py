from dataset.syllabels_preprocessing.syllables import sylco
import codecs
from tqdm import tqdm
'''
word = 'Worcester'

print(sylco(word))
'''

file = codecs.open('Haikus_result_manual 2.txt','r',encoding='utf-8')
output = codecs.open('Haikus_result_manual_refine.txt','w',encoding='utf-8')
output1 = codecs.open('Haikus_result_manual_syllables.txt','w',encoding='utf-8')
output2 = codecs.open('Haikus_17.txt','w',encoding='utf-8')

poem = []
poem_count = 0
count_17 = 0
syllabel = 0
for lines in tqdm(file):
    line = lines.strip()
    line = line.replace(' ', '')
    if len(line) != 0:
        poem.append(lines.replace('\n',''))
        words = line.split(' ')
        for word in words:
            syllabel = syllabel + sylco(word)
    else:
        if len(poem) != 3:
            syllabel = 0
            poem = []
            # continue
        else:
            if syllabel == 17:
                count_17 = count_17 + 1
                for sentence in poem:
                    output2.write(sentence + '\n')
                output2.write('\n')
            poem_count = poem_count + 1
            for sentence in poem:
                output.write(sentence+'\n')
            output.write('\n')
            output1.write(str(syllabel)+'\n')
            poem = []
            syllabel = 0
print(poem_count)
print(count_17)
file.close()
output1.close()
output.close()
output2.close()


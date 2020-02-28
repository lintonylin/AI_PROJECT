from nltk.translate.bleu_score import corpus_bleu, sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
import codecs
import sacrebleu
refs = [['The dog bit the man.', 'It was not unexpected.', 'The man bit him first.'],
        ['The dog had bit the man.', 'No one was surprised.', 'The man had bitten the dog.']]
#sys = [['The dog bit the man.', "It wasn't surprising.", 'The man had just bitten him.']]
smooth = SmoothingFunction()
#score = corpus_bleu(refs, sys, weights=(0, 0, 1, 0), smoothing_function=smooth.method2)
#print(score)

# multirnn = codecs.open('sample_result_multirnn.txt', 'r', encoding='utf-8')
multirnn = codecs.open('sample_result_RCNN.txt', 'r', encoding='utf-8')
haikutest = codecs.open('haiku_test.txt', 'r', encoding='utf-8')

sys = []
poem = []
for lines in multirnn:
        line = lines.strip().replace('\n', '')
        if len(line) != 0:
                poem.append(line)
        elif len(poem) != 3:
                poem = []
                continue
        else:
                sys.append(poem)
                poem = []


refs = []
poem = []
for lines in haikutest:
        line = lines.strip().replace('\n', '')
        if len(line) == 0:
                continue
        strs = line.split('+')
        if len(strs) != 3:
                continue
        for str in strs:
                poem.append(str)
        refs.append(poem)
        poem = []

print(sys)
print(len(sys))
print(refs)
print(len(refs))
score = 0.0
for sentence in sys:
        bleu = sentence_bleu(refs, sentence, weights=(0.25, 0.25, 0.25, 0.25), smoothing_function=smooth.method4)
        # bleu = sacrebleu.sentence_bleu(sentence, refs).score
        score = score + bleu
score = score / len(sys)
print(score)
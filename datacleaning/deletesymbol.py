# -*- coding: utf-8 -*-
#from langdetect import detect
import os

def is_alphabet(uchar):
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False

lines_new = []
line1 = ''
i=j=k=0
count = 0
det_flag = 0
det_count = 0
discord_flag = 0
module_path = os.path.dirname(__file__) 
with open(module_path + '/input.txt',"r",encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        s1 = str(line) #3
        for a in range(len(s1)):
            if is_alphabet(s1[a]) | (s1[a]=='\n') | (s1[a]==' '):
                line1 += s1[a]
    lines_new.append(line1)
    f.close()

with open(module_path + '/Haikus_nosymbol.txt',"w",encoding="utf8") as n:
    for line_new in lines_new:
        n.write(line_new)
    n.close()
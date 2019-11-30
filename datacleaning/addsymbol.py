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
b = 0
line_count = 0
poem_count = 0
poem_flag = 0
module_path = os.path.dirname(__file__) 
with open(module_path + '/Haikus_nosymbol.txt',"r",encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        s1 = str(line)
        if poem_flag == 1:
            line_count += 1
            s1 = s1.strip() 
            s1 = s1 + ' +\n'
        if line_count == 2:
            line_count = 0
            poem_flag = 0
        if s1[0] == '\n':
            poem_flag = 1
            poem_count += 1
        lines_new.append(s1)
    f.close()
print(poem_count)
print(b)
with open(module_path + '/Haikus_withplus.txt',"w",encoding="utf8") as n:
    for line_new in lines_new:
        n.write(line_new)
    n.close()
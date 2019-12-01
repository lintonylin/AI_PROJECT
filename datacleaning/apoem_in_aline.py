# -*- coding: utf-8 -*-
#from langdetect import detect
import os

lines_new = []
b = 0
line_count = 0
module_path = os.path.dirname(__file__) 
with open(module_path + '/Haikus_nosymbol.txt',"r",encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        s1 = str(line)
        
        line_count += 1
        if line_count == 2:
            s1 = s1.strip()
            str2 = s1 + ' + '
        if line_count == 3:
            s1 = s1.strip()
            str3 = s1 + ' + '
        if line_count == 4:
            s1 = s1.strip()
            str4 = s1 + ' + '
            s1 = str2 + str3 + str4 + '\n'
            lines_new.append(s1)
            line_count = 0

    f.close()
with open(module_path + '/Haikus_1poem_in_1line.txt',"w",encoding="utf8") as n:
    for line_new in lines_new:
        n.write(line_new)
    n.close()
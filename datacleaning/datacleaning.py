# -*- coding: utf-8 -*-
#from langdetect import detect
lines_new = []
i=j=k=0
count = 0
det_flag = 0
det_count = 0
discord_flag = 0
with open("dataclean/Haikus.txt","r",encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        s1 = str(line[0:3]) #3
        s2 = str(line[0:4]) #4
        s3 = str(line[0:6])
        s4 = str(line[0:11])
        s5 = str(line[0:2])
        if len(line)-2 > 0:
            s6 = str(line[len(line)-2])
        if line == '\n':
            if count < (len(lines)-2):
                if (lines[count+1] == '\n') & (lines[count+2] == '\n'):
                    lines_new.append(line)
                else:
                    pass
            else:
                pass
        elif s1.isdigit() :
            if det_flag != 1:
                lines_new.pop()
                lines_new.pop()
                lines_new.pop()
                print('delect_num')
                print(i)
                i+=1
            det_flag = 0
        elif s1 == 'cco' :
            lines_new.pop()
            lines_new.pop()
            lines_new.pop()
            det_flag = 1
            print('delect_cco')
            print(k)
            k += 1
        elif (s2 == 'tw :' )| (s2 =='fb :'):
            discord_flag = 1
            print('else_num')
            print(j)
            j+=1
            pass
        elif discord_flag == 1:
            discord_flag = 0
            pass
        elif (s3 =='blog :' )| (s3 =='site :' )|(s3 =='page :'):
            print('else_num')
            print(j)
            j+=1
            pass
        elif s4 == 'Webographie':
            print('else_num')
            print(j)
            j+=1
            pass
        elif len(line) > 50:
            print('else_num')
            print(j)
            j+=1
            pass
        elif s5.isdigit():
            pass
        # elif s6.isdigit():
        #     lines_new.pop()
        #     lines_new.pop()
        #     pass
        else:
            lines_new.append(line)
        count += 1
    f.close()

with open("dataclean/Haikus_result.txt","w",encoding="utf8") as n:
    for line_new in lines_new:
        n.write(line_new)
    n.close()
# -*- coding: utf-8 -*-
# 最大正向匹配
import os

def conv(string,dic):
    i = 0
    #print(type(string),string.decode("utf-8"))
    print('conv now')
    while i < len(string):
        print('len now',len(string))
        for j in range(len(string) - i, 0, -1):

            if string[i:][:j] in dic:
                t = dic[string[i:][:j]]
                string = string[:i] + t + string[i:][j:]
                i += len(t) - 1
                break
        i += 1
        print(i)
    return string

# 生成转换字典
def mdic():    
    table = open('ZhConversion.php',encoding='utf-8').readlines()
    dic = dict()
    name = []
    for line in table:
        if line[0] == '$':
            #print line.split()[0][1:]
            name.append(dic)
            dic = dict()
        if line[0] == "'":
            word = line.split("'")
            dic[word[1]] = word[3]
    name[3].update(name[1]) 
    name[4].update(name[1]) 
    name[5].update(name[2]) 
    return name[3],name[4],name[5]

if __name__=="__main__":
    #a="头发发展萝卜卜卦秒表表达 "
    #b="大衛碧咸在寮國見到了布希"
    #c="大卫·贝克汉姆在老挝见到了布什"
    path = 'C:\\Users\\zxc82\\\movie\\srt\\srt\\zh'
    for dirPath, dirNames, fileNames in os.walk(path):
        for f in fileNames:
            file=os.path.join(dirPath, f)
            a = open(file,'rb').read()
            #break
    [dic_TW,dic_HK,dic_CN] = mdic()
    str_TW = conv(a.decode('utf-8'),dic_TW)
    print (str_TW)
   # str_HK = conv(c,dic_HK)    
    #str_CN = conv(b,dic_CN)
    f_cht= 'C:\\Users\\zxc82\\\movie\\srt\\srt\\zh\\'
    para=f_cht+'test.txt'
    text_file = open(para, "w")
    text_file.write(str_TW)
    text_file.close()

    

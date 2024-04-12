import codecs
import re
import json
from hanzidict import hanzidict

def teshuzifutihuan(text):#匹配时去除特殊字符
    text = text.replace("♪", "").replace("・", "").replace("〜", "").replace("～", "").replace("?", "").replace(" ", "").replace('\u3000','').replace('\t','').replace(']','')
    text=re.sub('\[([^|\]]+)\|','',text)#删除脚本中的注音标识
    return text

def hanzitihuan(text):#按照字典替换不支持的汉字，后续通过UniversalInjectorFramework替换回去以正常显示
    replaced_string=''
    for char in text:
        replaced_string += hanzidict.get(char, char)
    return replaced_string

def fuhaotihuan(text):#替换掉译文中一些不支持的常见特殊符号形式，以正常显示
    return text.replace('—','ー').replace('～','〜').replace('“','「').replace('”','」')


transpath='WizAnniversary_transed.json'
with open(transpath,'r',encoding='utf-8') as f:
    replacement_dict=json.load(f)

with codecs.open('.\原文件\WizAnniversary.txt', 'r', encoding='shiftjis') as input_file:
    with codecs.open(".\\fvp-utf8\\WizAnniversary_transed.txt", 'w', encoding='utf8') as hime:
        with codecs.open(".\\fvp-utf8\\WizAnniversary_strings_transed.txt", 'w', encoding='utf8') as himestrings:
            for line in input_file:
                if line.startswith("\tpushstring "):
                    content = line.strip()[11:]
                    content1 = teshuzifutihuan(content)
                    sline=content
                    if content1 in replacement_dict:
                        if len(content1)>0:
                            if not re.match(r'[A-Za-z]', content1[0]):#避免对调用资源文件的代码进行替换
                                line = line.replace(content, replacement_dict[content1]["userTrans"])
                                sline= replacement_dict[content1]["userTrans"]
                    himestrings.write(fuhaotihuan(hanzitihuan(sline))+'\n')
                hime.write(fuhaotihuan(hanzitihuan(line)))

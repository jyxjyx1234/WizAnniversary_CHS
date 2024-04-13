import json
import re

with open('.\译文\WizAnniversary_transed.json','r',encoding='utf8') as f:
    yiwen=json.load(f)

yiwen_processed=[]
for dic in yiwen:
    if '<汁>' not in dic["pre_jp"]:
        if '<汗>' in dic["pre_jp"]:
            if '<汁>' in dic["post_zh_preview"]:
                dic["post_zh_preview"]=dic["post_zh_preview"].replace('<汁>','<汗>')
    if '<汗>' not in dic["pre_jp"]:
        if '<汁>' in dic["pre_jp"]:
            if '<汗>' in dic["post_zh_preview"]:
                dic["post_zh_preview"]=dic["post_zh_preview"].replace('<汗>','<汁>')
    if not re.search('<.>',dic["pre_jp"]):
        if re.search('<.>',dic["post_zh_preview"]):
            dic["post_zh_preview"]=re.sub('<.>','',dic["post_zh_preview"])
    
    yiwen_processed.append(dic)

with open('.\译文\WizAnniversary_transed_temp.json','w',encoding='utf8') as f:
    json.dump(yiwen_processed, f , ensure_ascii=False, indent=4) 
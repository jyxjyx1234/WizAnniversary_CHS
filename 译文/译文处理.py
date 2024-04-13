import json
import re

with open('.\译文\WizAnniversary_transed.json','r',encoding='utf8') as f:
    yiwen=json.load(f)
'''
        "index"
        "name": 
        "pre_jp": 
        "post_jp": 
        "pre_zh": 
        "proofread_zh":
        "trans_by": 
        "proofread_by": 
        "post_zh_preview": 
'''

yiwen_processed=[]

for dic in yiwen:
    if re.search('<.>',dic["pre_jp"]):
        if not re.search('<.>',dic["post_zh_preview"]):
            print(dic["index"])


#with open('.\译文\WizAnniversary_transed_temp.json','w',encoding='utf8') as f:
#    json.dump(yiwen_processed, f , ensure_ascii=False, indent=4) 
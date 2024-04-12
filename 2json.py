import json  
import re

# 定义输入和输出文件的名字  
input_filename = ".\原文件\hs.txt"
output_filename = ".\原文件\hs.json"

def zhuyinchuli(text):#处理注音（已经在文本编辑器中处理过了）
    text=re.sub('\[([^|\]]+)\|','',text)
    return text.replace("]","")

# 初始化一个空列表来存储消息  
messages = []
  
# 打开输入文件并逐行读取  
with open(input_filename, 'r', encoding='utf8') as file:
    i={}
    jilu=[]#去除重复语句以省钱
    for line in file:
        if "【" in line:
            i['name']=line.replace("【",'').replace("】",'')
        else:
            i['message']=line
            if i['message'] not in jilu:
                jilu.append(i['message'])
                messages.append(i)
            i={}
        
  
# 将消息列表写入JSON文件  
with open(output_filename, 'w', encoding='UTF-8') as json_file:  
    json.dump(messages, json_file, ensure_ascii=False, indent=4)  

print(f"Messages extracted and saved to {output_filename}")
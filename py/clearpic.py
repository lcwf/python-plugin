# -*- coding: utf-8 -*-
import os
import json
FILE_PATH1 = os.path.dirname(__file__)
FILE_PATH =os.path.join(FILE_PATH1,"../resrouces")
if not os.path.exists(FILE_PATH+'/qianwen'):
    os.makedirs(FILE_PATH+'/qianwen')
if not os.path.exists(FILE_PATH+'/jieqian'):
    os.makedirs(FILE_PATH+'/jieqian')
if not os.path.exists(FILE_PATH+'/enemies_info'):
    os.makedirs(FILE_PATH+'/enemies_info')
if not os.path.exists(FILE_PATH+'/cailiaodian'):
    os.makedirs(FILE_PATH+'/cailiaodian')
if not os.path.exists(FILE_PATH+'/life'):
    os.makedirs(FILE_PATH+'/life')
if not os.path.exists(FILE_PATH+'/life1'):
    os.makedirs(FILE_PATH+'/life1')
if not os.path.exists(FILE_PATH+'/today_card'):
    os.makedirs(FILE_PATH+'/today_card')
if not os.path.exists(FILE_PATH+'/atifacts'):
    os.makedirs(FILE_PATH+'/atifacts')
path=os.listdir(FILE_PATH+'/jieqian')
for i in path:
    os.remove(FILE_PATH+'/jieqian/'+i)
path=os.listdir(FILE_PATH+'/today_card')
for i in path:
    os.remove(FILE_PATH+'/today_card/'+i)

path1=os.listdir(FILE_PATH+'/enemies_info')
for j in path1:
    #清理绘制好的原魔信息
    os.remove(FILE_PATH+'/enemies_info/'+j)
path2=os.listdir(FILE_PATH+'/qianwen')
for k in path2:
    os.remove(FILE_PATH+'/qianwen/'+k)
path3=os.listdir(FILE_PATH+'/cailiaodian')
for k in path3:
    os.remove(FILE_PATH+'/cailiaodian/'+k)
path4=os.listdir(FILE_PATH+'/life')
for k in path4:
    os.remove(FILE_PATH+'/life/'+k)
path4=os.listdir(FILE_PATH+'/life1')
for k in path4:
    os.remove(FILE_PATH+'/life1/'+k)
a=dict()
if os.path.exists(FILE_PATH+'/1.png'):
    os.remove(FILE_PATH+'/1.png')
if os.path.exists(FILE_PATH+'/1.jpg'):
    os.remove(FILE_PATH+'/1.jpg')
if os.path.exists(FILE_PATH+'/tarot/torot.png'):
    os.remove(FILE_PATH+'/tarot/torot.png')
if os.path.exists(FILE_PATH+'/images/123.jpeg'):
    os.remove(FILE_PATH+'/images/123.jpeg')
if os.path.exists(FILE_PATH+'/images/123.gif'):
    os.remove(FILE_PATH+'/images/123.gif')
DATA_PATH=os.path.join(FILE_PATH1,"../data")
with open(DATA_PATH+'/qianwen.json','w') as g:
    a=json.dumps(a)
    g.write(a)

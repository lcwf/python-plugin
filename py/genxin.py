import requests
from datetime import datetime
from datetime import timedelta
import re,os,json
import pytz
tz = pytz.timezone('utc')
FILE_PATH1 = os.path.dirname(__file__)
FILE_PATH =os.path.join(FILE_PATH1,"../data")
pcr_now = datetime.now()
pcr_now = datetime.now(tz)
pcr_now+= timedelta(hours=8)
pcr_now=pcr_now.strftime(r"%Y-%m-%d %H:%M")
if not os.path.exists(FILE_PATH+'/update.json'):
    with open(FILE_PATH+'/update.json','w',encoding="UTF-8")as f:
        update=dict()
        py=dict()
        py['date']=pcr_now
        py['url']='https://gitee.com/linglinglingling-python/python-plugin'
        update['py']=py
        yunzai=dict()
        yunzai['date']=pcr_now
        yunzai['url']='https://gitee.com/yoimiya-kokomi/Yunzai-Bot'
        update['yunzai']=yunzai
        miaomiao=dict()
        miaomiao['date']=pcr_now
        miaomiao['url']='https://gitee.com/yoimiya-kokomi/miao-plugin'
        update['miaomiao']=miaomiao
        json.dump(update,f,ensure_ascii=False,indent=2)
        f.close()
        exit()

with open(FILE_PATH+'/update.json','r',encoding="UTF-8")as f:
    update=json.load(f)
    f.close()
update['yunzai']['url']=='https://gitee.com/yoimiya-kokomi/Yunzai-Bot'
for i in update:
    req=requests.get(update[i]['url'])
    text=req.text
    date1=re.findall('datetime=(.*?) title=',text)
    date1=datetime.strptime(date1[0].replace("'",''),"%Y-%m-%d %H:%M")
    date2=datetime.strptime(update[i]['date'],"%Y-%m-%d %H:%M")
    if date1>date2:
        print(i)
        update[i]['date']=pcr_now
with open(FILE_PATH+'/update.json','w',encoding="UTF-8")as f:
    json.dump(update,f,ensure_ascii=False,indent=2)
    f.close()





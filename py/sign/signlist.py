import json
import sys,os,random
from pathlib import Path
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
#import matplotlib.pyplot as plt
FILE_PATH1 = os.path.dirname(__file__)
FILE_PATH =os.path.join(FILE_PATH1,"../../resrouces")
SIGN_RESOURCE_PATH = Path(__file__).parent.parent.parent / "resrouces" / "sign_res"
SAVE_PATH=Path(__file__).parent.parent.parent / "resrouces" / 'today_card'
DATA_PATH=Path(__file__).parent.parent.parent/"data"
dataname="sign.json"
if not os.path.exists(DATA_PATH/dataname):
    abc=open(DATA_PATH/dataname,'w',encoding='utf-8')
    abc.close()
elif os.path.getsize(DATA_PATH/dataname)>0:
    with open(DATA_PATH/dataname,'r',encoding='utf-8')as f:
        abc=json.load(f)
        f.close()    
    x=[]
    y=[]
    n=0
    abc
    for i in abc:
        x.append(i)
    x.sort()
    for i in x:
        y.append(round(abc[i]['impression'],2))
    theme=[ThemeType.LIGHT,ThemeType.DARK,ThemeType.CHALK,ThemeType.ESSOS,ThemeType.INFOGRAPHIC,
           ThemeType.MACARONS,ThemeType.PURPLE_PASSION,ThemeType.ROMA,ThemeType.ROMANTIC,
           ThemeType.SHINE,ThemeType.VINTAGE,ThemeType.WALDEN,ThemeType.WESTEROS,ThemeType.WONDERLAND]
    I=random.randint(0,len(theme))
    chart=Bar(init_opts=opts.InitOpts(theme=theme[I]))
    chart.add_xaxis(x)
    chart.add_yaxis('好感',y)
    chart.render(SAVE_PATH/"haogan.html")
    exit()
print('error')
    


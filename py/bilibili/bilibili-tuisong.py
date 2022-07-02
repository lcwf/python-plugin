import requests
import time,json
import os
from hashlib import md5
from urllib.parse import urlencode
from typing import Any, Dict, Optional
DEFAULT_HEADERS = {
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"
        "Safari/537.36 Edg/87.0.664.60"
    ),
    "Referer": "https://www.bilibili.com/",
}

APPSEC = "59b43e04ad6965f34319062b478f83dd"
APPKEY = "4409e2ce8ffd12b8"

FILE_PATH1 = os.path.dirname(__file__)
DATA_PATH=os.path.join(FILE_PATH1,"../../data")

url_n='https://api.bilibili.com/x/space/acc/info'

#用户视频历史
url_d='https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history'

#用户动态历史
url_v = f"https://api.bilibili.com/x/space/arc/search"

url_m = f"https://api.bilibili.com/pgc/review/user"

url_l='https://api.live.bilibili.com/room/v1/Room/get_info'

def _encrypt_params(params: Dict[str, Any], local_id: int = 0) -> Dict[str, Any]:
    params["local_id"] = local_id
    params["appkey"] = APPKEY
    params["ts"] = int(time.time())
    params["sign"] = md5(
        f"{urlencode(sorted(params.items()))}{APPSEC}".encode("utf-8")
    ).hexdigest()
    return params

def request(
    url,
    params,
    auth=None,
    headers=DEFAULT_HEADERS,
):
    _encrypt_params(params)
    
    resp = requests.get(
        url=url, headers=headers, params=params
        )
    resp.encoding = "utf-8"
    if resp.json()["code"] != 0:
        print('requesterror')
        exit()
    if model =='media':
        return resp.json()["result"]
    return resp.json()["data"]

name1='/bilibili.json'
if not os.path.exists(DATA_PATH+name1):
    print('empty')
    exit()
with open(DATA_PATH+name1,'r',encoding='utf-8') as f:
    b=json.load(f)
    f.close()
a=dict()
for i in b:
    if b[i]['type']=='up':
        model='up'
        uid=b[i]['uid']
        params_n = {"mid": uid}
        resq=request(url_n,params_n)
        uname=resq["name"]
        params_d = {
            "host_uid": uid,
            "offset_dynamic_id": 0,
            "need_top": int(bool(False)),
            }
        dynamic=request(url_d,params_d)
        c=dict()
        if dynamic.get("cards"):
            dynamic = dynamic["cards"][0]["desc"]["timestamp"]
            uname=b[i]['uname']
            if dynamic>b[i]['dynamic']:
                c['dynamic']='true'
                c['dynamic_url']=f"{uname} 投稿了新文章啦\n https://space.bilibili.com/{uid}/dynamic"
                c['gid']=b[i]['gid']
                b[i]['dynamic']=dynamic

        params_v = {
            "mid": uid,
            "ps": 30,
            "tid": 0,
            "pn": 1,
            "keyword": "",
            "order": "pubdate"
            }
        video=request(url_v,params_v)
        if video["list"].get("vlist"):
            video1 = video["list"]["vlist"][0]
            name = b[i]["uname"]
            image=video1["pic"]
            video = video["list"]["vlist"][0]["created"]
            if video>b[i]['video']:
                c['video']='true'
                #c['cover']=image
                c['video_url']=f"{uname} 投稿了新视频啦\n标题：{video1['title']}\n Bvid：{video1['bvid']}\n https://www.bilibili.com/video/{video1['bvid']}"
                c['gid']=b[i]['gid']
                b[i]['video']=video
        if len(c)>0:
            a[i]=c
    elif b[i]['type']=='media':
        model='media'
        uid=b[i]['uid']
        params_m = {"media_id": uid}
        resq=request(url_m,params_m)
        title = resq["media"]["title"]
        new_ep = resq["media"]["new_ep"]["index"]
        c=dict()
        if b[i]['time']!=resq["media"]["new_ep"]["index"]:
            c['info']=resq["media"]["cover"]+title+'更新啦\n'+f"最新集数：{new_ep}"
            c['gid']=b[i]['gid']
        if len(c)>0:
            a[i]=c
    elif b[i]['type']=='live':
        model='live'
        uid=b[i]['uid']
        params_l = {"id": uid}
        resq=request(url_l,params_l)
        c=dict()
        title = resq["title"]
        cover = resq["user_cover"]
        live_status = resq["live_status"]
        uname=b[i]['uname']
        if b[i]['time'] != live_status:
            b[i]['time']=live_status
        if b[i]['time']=='0' and live_status == '1':
            c['gid']=b[i]['gid']
            #c['cover']=cover
            c['info']=f"{uname} 开播啦！\n标题：{title}\n直链：https://live.bilibili.com/{uid}"
        if len(c)>0:
            a[i]=c
if len(a)==0:
    print('empty')
    exit()
with open(DATA_PATH+name1,'w',encoding='utf-8') as f:
    c=json.dumps(b,ensure_ascii=False,indent=1)
    f.write(c)
    f.close
name1='/tuisong.json'
with open(DATA_PATH+name1,'w',encoding='utf-8') as f:
    c=json.dumps(a,ensure_ascii=False,indent=1)
    f.write(c)
    f.close

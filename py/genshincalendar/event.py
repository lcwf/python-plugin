# -*- coding: utf-8 -*-
import os
import json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import requests
import asyncio
import math
import functools
import re
import pytz
tz = pytz.timezone('utc')
# type 0 普通常驻任务深渊 1 新闻 2 蛋池 3 限时活动H5

event_data = {
    'cn': [],
}

event_updated = {
    'cn': '',
}

lock = {
    'cn': asyncio.Lock(),
}

ignored_key_words = [
    "修复",
    "版本内容专题页",
    "米游社",
    "调研",
    "防沉迷"
]

ignored_ann_ids = [
    495,  # 有奖问卷调查开启！
    1263,  # 米游社《原神》专属工具一览
    423,  # 《原神》玩家社区一览
    422,  # 《原神》防沉迷系统说明
    762,  # 《原神》公平运营声明
]

list_api = 'https://hk4e-api.mihoyo.com/common/hk4e_cn/announcement/api/getAnnList?game=hk4e&game_biz=hk4e_cn&lang=zh-cn&bundle_id=hk4e_cn&platform=pc&region=cn_gf01&level=55&uid=100000000'
detail_api = 'https://hk4e-api.mihoyo.com/common/hk4e_cn/announcement/api/getAnnContent?game=hk4e&game_biz=hk4e_cn&lang=zh-cn&bundle_id=hk4e_cn&platform=pc&region=cn_gf01&level=55&uid=100000000'


def cache(ttl=timedelta(hours=1), arg_key=None):
    def wrap(func):
        cache_data = {}

        @functools.wraps(func)
        async def wrapped(*args, **kw):
            nonlocal cache_data
            default_data = {"time": None, "value": None}
            ins_key = 'default'
            if arg_key:
                ins_key = arg_key + str(kw.get(arg_key, ''))
                data = cache_data.get(ins_key, default_data)
            else:
                data = cache_data.get(ins_key, default_data)

            now = datetime.now()
            if not data['time'] or now - data['time'] > ttl:
                try:
                    data['value'] = await func(*args, **kw)
                    data['time'] = now
                    cache_data[ins_key] = data
                except Exception as e:
                    raise e

            return data['value']

        return wrapped

    return wrap



def query_data(url):
    try:
        resp=requests.get(url)
        return resp.json()
    except:
        pass
    return None


def load_event_cn():
    result = query_data(url=list_api)
    detail_result =query_data(url=detail_api)
    if result and 'retcode' in result and result['retcode'] == 0 and detail_result and 'retcode' in detail_result and detail_result['retcode'] == 0:
        event_data['cn'] = []
        event_detail = {}
        for detail in detail_result['data']['list']:
            event_detail[detail['ann_id']] = detail

        datalist = result['data']['list']
        for data in datalist:
            for item in data['list']:
                # 1 活动公告 2 游戏公告
                if item['type'] == 2:
                    ignore = False
                    for ann_id in ignored_ann_ids:
                        if ann_id == item["ann_id"]:
                            ignore = True
                            break
                    if ignore:
                        continue

                    for keyword in ignored_key_words:
                        if keyword in item['title']:
                            ignore = True
                            break
                    if ignore:
                        continue

                start_time = datetime.strptime(
                    item['start_time'], r"%Y-%m-%d %H:%M:%S")
                end_time = datetime.strptime(
                    item['end_time'], r"%Y-%m-%d %H:%M:%S")
                if '万叶' in item['title']:
                    print(event_detail[item["ann_id"]]['content'])
                # 从正文中查找开始时间
                if event_detail[item["ann_id"]]:
                    content = event_detail[item["ann_id"]]['content']
                    searchObj = re.search(
                        r'(\d+)\/(\d+)\/(\d+)\s(\d+):(\d+):(\d+)', content, re.M | re.I)
                    
                    if '2.8版本更新后' in content:
                        curmon = datetime.today()
                        start_time = datetime.strptime(
                            curmon.strftime("%Y-7-13 11:00"), r"%Y-%m-%d %H:%M")
                    
                    try:
                        datelist = searchObj.groups()  # ('2021', '9', '17')
                        if datelist and len(datelist) >= 6:
                            
                            ctime = datetime.strptime(
                                f'{datelist[0]}-{datelist[1]}-{datelist[2]} {datelist[3]}:{datelist[4]}:{datelist[5]}', r"%Y-%m-%d %H:%M:%S")
                            if ctime > start_time and ctime < end_time:
                                start_time = ctime
                            #if '一斗' in content:
                            #   print(ctime)
                            
                    except Exception as e:
                        pass

                event = {'title': item['title'],
                         'start': start_time,
                         'end': end_time,
                         'forever': False,
                         'type': 0}
                if '任务' in item['title']:
                    event['forever'] = True
                if item['type'] == 1:
                    event['type'] = 1
                if '扭蛋' in item['tag_label']:
                    event['type'] = 2
                if '倍' in item['title']:
                    event['type'] = 3
                event_data['cn'].append(event)
        # 深渊提醒
        i = 0
        while i < 2:
            curmon = datetime.today() + relativedelta(months=i)
            nextmon = curmon + relativedelta(months=1)
            event_data['cn'].append({
                'title': '「深境螺旋」',
                'start': datetime.strptime(
                    curmon.strftime("%Y/%m/01 04:00"), r"%Y/%m/%d %H:%M"),
                'end': datetime.strptime(
                    curmon.strftime("%Y/%m/16 03:59"), r"%Y/%m/%d %H:%M"),
                'forever': False,
                'type': 3
            })
            event_data['cn'].append({
                'title': '「深境螺旋」',
                'start': datetime.strptime(
                    curmon.strftime("%Y/%m/16 04:00"), r"%Y/%m/%d %H:%M"),
                'end': datetime.strptime(
                    nextmon.strftime("%Y/%m/01 03:59"), r"%Y/%m/%d %H:%M"),
                'forever': False,
                'type': 3
            })
            
            
            i = i+1
        curmon = datetime.today()
        event_data['cn'].append({
            'title': '「2.7版本」',
            'start': datetime.strptime(
                curmon.strftime("%Y/5/31 11:00"), r"%Y/%m/%d %H:%M"),
            'end': datetime.strptime(
                curmon.strftime("%Y/7/13 11:00"), r"%Y/%m/%d %H:%M"),
            'forever': False,
            'type': 0
        })
        return 0
    return 1


def load_event(server):
    if server == 'cn':
        return load_event_cn()
    return 1


def get_pcr_now(offset):
    pcr_now = datetime.now()
    pcr_now = datetime.now(tz)
    pcr_now+= timedelta(hours=8)
    #pcr_now = pcr_now.replace(
    #  hour=8, minute=0, second=0, microsecond=0)
    if pcr_now.hour < 4:
       pcr_now -= timedelta(days=1)
      # 用8点做基准
    pcr_now = pcr_now + timedelta(days=offset)
    
    return pcr_now


def get_events(server, offset, days):
    events = []
    load_event_cn()
    
    
    pcr_now = datetime.now(tz).replace(tzinfo=None)
    
    pcr_now+= timedelta(hours=8)
    if pcr_now.hour < 4:
        pcr_now -= timedelta(days=1)
      # 用晚6点做基准
    

    t = pcr_now.strftime('%y%m%d')
    if event_updated[server] != t:
        if load_event(server) == 0:
            event_updated[server] = t

    start = pcr_now + timedelta(days=offset)
    end = start + timedelta(days=days)
    end -= timedelta(hours=24) # 晚上12点结束
    
    #print(event_data)
    for event in event_data[server]:
        if end > event['start'] and start < event['end']:  # 在指定时间段内 已开始 且 未结束
            event['start_days'] = math.floor(
                (event['start'] - start) / timedelta(days=1))  # 还有几天开始
            event['left_days'] = math.floor(
                (event['end'] - start) / timedelta(days=1))  # 还有几天结束
            
            start1=start+abs(timedelta(days=event['start_days']))
            end1=start+abs(timedelta(days=event['left_days']))
            event['start_hours'] = math.floor(
                (event['start'] -start1 ) / timedelta(hours=1))
            event['left_hours'] = math.floor(
                (event['end'] - end1) / timedelta(hours=1))
            start1=start1+abs(timedelta(hours=event['start_hours']))
            end1=end1+abs(timedelta(hours=event['left_hours']))
            event['start_minutes'] = math.floor(
                (event['start'] -start1 ) / timedelta(minutes=1))
            event['left_minutes'] = math.floor(
                (event['end'] - end1) / timedelta(minutes=1))
            start1=start1+abs(timedelta(minutes=event['start_minutes']))
            end1=end1+abs(timedelta(minutes=event['left_minutes']))
            
            event['start_seconds'] = math.floor(
                (event['start'] -start1 ) / timedelta(seconds=1))
            event['left_seconds'] = -math.floor(
                (event['end'] - end1) / timedelta(seconds=1))
            events.append(event)
            
    # 按type从大到小 按剩余天数从小到大
    events.sort(key=lambda item: item["type"]
                * 100 - item['left_days'], reverse=True)
    
    return events



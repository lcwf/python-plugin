import os, math,sys
from io import BytesIO
from PIL import Image
import requests


path = os.path.dirname(__file__)
def save_img(url):
    
    response = requests.get(url).content
    #none使用的话此处改为使用requests，去掉await
    image = Image.open(BytesIO(response))
    return image


def make_img(up_img, hide_img):
    #先获取两张图片中宽度较大的宽度
    max_size = (max(up_img.size[0], hide_img.size[0]), 0)
    #将图片依据较大的宽度等比例处理
    up_img = up_img.resize((max_size[0], int(up_img.size[1] * (max_size[0] / up_img.size[0]))),Image.ANTIALIAS)
    hide_img = hide_img.resize((max_size[0], int(hide_img.size[1] * (max_size[0] / hide_img.size[0]))),Image.ANTIALIAS)
    #获取处理后生成图片的大小
    max_size = (max_size[0], max(up_img.size[1],hide_img.size[1]))

    
    if max_size[1] == hide_img.size[1]: #这两个elif都是对图片进行大小补全后再转为灰度图片
        up_img_temp = Image.new('RGBA',(max_size),(255,255,255,255))
        up_img_temp.paste(up_img,(0, (max_size[1] - up_img.size[1]) // 2))
        up_img = up_img_temp
        hide_img = hide_img
    elif max_size[1] == up_img.size[1]:
        hide_img_temp = Image.new('RGBA',(max_size),(0,0,0,255))
        hide_img_temp.paste(hide_img,(0, (max_size[1] - hide_img.size[1]) // 2))
        #up_img = up_img.convert('L')
        hide_img = hide_img_temp

    hide_img=hide_img.convert('L')
    up_img=up_img.convert('L')
    out = Image.new('RGBA',(max_size),
                    (255,255,255,255)) #生成一个空的用于输出的图片
    for i in range(up_img.size[0]):
        for k in range(up_img.size[1]):
            #遍历读取每一个像素点
            la=up_img.getpixel((i,k))/512+0.5
            '''
            #ra=color[0]/512*2
            #ga=color[1]/512*2
            
            ba=color[2]/512*2
            aa=color[3]/512*2
            '''
            lb=hide_img.getpixel((i,k))/512
            '''
            rb=color[0]/512/2
            gb=color[1]/512/2
            bb=color[2]/512/2
            ab=color[3]/512/2
            rm = int(512*((ab* rb)+ (1-ab)*ra))
            gm= int(512*((ab* gb)+ (1-ab)*ga))
            bm = int(512*((ab* bb)+ (1-ab)*ba))
            am = int(512*((ab* ab)+ (1-ab)*ba))
            aa=int(color[3]/2)
            '''
            R=int((255*lb)/(1-(la-lb)))
            A=int((1-(la-lb))*255)
            #a1 = int((1 - (ra - rb)) * 256)
            #a2 = int((1 - (ga - gb)) * 256)
            #a3 = int((1 - (ba - bb)) * 256)
            #a=int((a1+a2+a3)/3)#这里是套用公式 公式可以见b站专栏 隐藏图原理(https://www.bilibili.com/read/cv9474134/)
            out.putpixel((i, k), (R,R,R,A)) #将用于输出的图片每个像素点处理成需要的颜色和透明度

    #buf = BytesIO()
    out.save(path+'/../resrouces/1.png')
    #base64_str = f'base64://{base64.b64encode(buf.getvalue()).decode()}'
    #return f'[CQ:image,file={base64_str}]'

image1=sys.argv[1]
image2=sys.argv[2]
image1=save_img(image1)
image2=save_img(image2)
make_img(image1,image2)

import random
from io import BytesIO
from PIL.Image import Image as IMG
from PIL import Image, ImageFilter, ImageDraw
from utils import *

def luxunsay(img,img2, args,nickname,sex, **kwargs):
    frame = load_image("luxunsay/0.jpg")
    text=args
    try:
        fontname = BOLD_FONT
        texts=[]
        if len(text)>13:
            texts.append(text[:13])
            texts.append(text[13:])
        else:
            texts.append(text)
        if len(texts)==2:
            if len(texts[1])>13:
                exit()
        fontsize =fit_font_size(text, frame.width - 50, 300, fontname, 40, 30)
        if not fontsize:
            fontsize=30
            #return "文字太长了哦，改短点再试吧~"
        x=[]
        if len(texts)>1:
            x.append(200+1.5*fontsize)
        x.append(200)
        font = load_font(fontname, fontsize)
        for i in range(len(texts)):
            draw_text(
                frame,
                (int(frame.width/2)-int(fontsize*len(texts[i])/2), frame.height - x[i],int(frame.width/2)+int(fontsize*len(texts[i])/2), frame.height - 100),
                texts[i],
                font=font,
                fill="white",
            )
    except ValueError:
        return
    draw_text(
        frame,
        (300,350),# frame.height - 200, frame.width - 40, frame.height - 100),
        "--鲁迅", font=font, fill="white")
    #frame.paste(luxun_text, (320, 400), alpha=True)
    return save_jpg(frame)

def marriage(img,img2, args,nickname,sex, **kwargs):
    img = img.convert("RGBA").resize((int(img.width * 1080 / img.height), 1080))
    img_w, img_h = img.size
    if img_w > 1500:
        img_w = 1500
    elif img_w < 800:
        img_h = int(img_h * img_w / 800)
    frame = img#.resize((int(img.width * 1080 / img.height), 1080))
    left = load_image("marriage/0.png")
    right = load_image("marriage/1.png")
    frame.paste(left,(0,0),left)
    frame.paste(
        right, (frame.width - right.width, 0), right
    )
    return save_jpg(frame)

def goodnews(img,img2, args,nickname,sex, **kwargs):
    fontname = BOLD_FONT
    text=args
    frame = load_image("goodnews/0.jpg")
    fontsize =fit_font_size(text, frame.width - 50, 300, fontname, 70, 15)
    font = load_font(fontname, fontsize)
    
    text=args
    try:
        draw_text(
            frame,
            (int(frame.width/2)-int(fontsize*len(text)/2), 200, int(frame.width/2)+int(fontsize*len(text)/2), frame.height - 100),
            text,
            font=font,
            fill=(238, 0, 0),
        )
    except ValueError:
        return
    return save_jpg(frame)

def psyduck(img,img2, args,nickname,sex, **kwargs):
    left_img = Image.new("RGBA", (155, 100))
    right_img = Image.new("RGBA", (155, 100))
    texts=args.split('，')
    fontname=FZSJ_QINGCRJ
    fontsize=[]
    fontsize.append(fit_font_size(texts[0], 145, 90, fontname, 80, 10))
    fontsize.append(fit_font_size(texts[1], 145, 90, fontname, 80, 10))
    font=[]
    font.append(load_font(fontname, fontsize[0]))
    font.append(load_font(fontname, fontsize[1]))
    def draw(frame, text: str,j):
        width, height = font[j].getsize_multiline(
            text, stroke_width=int(fontsize[j]*0)
        )
        draw_text(
            frame,
            (int(frame.width/2)-int(width/2), 50-fontsize[j]/2-10, int(frame.width/2)+int(width/2),50+fontsize[j]/2),
            text,            
            font[j],
            fill="black",
        )

    try:
        draw(left_img, texts[0],0)
        draw(right_img, texts[1],1)
    except ValueError:
        print('error')
        return
    """
    ("right", ((10, 0), (143, 17), (124, 104), (0, 84)), (298, 18)),
        ("right", ((13, 0), (143, 27), (125, 113), (0, 83)), (298, 30)),
        ("right", ((13, 0), (143, 27), (125, 113), (0, 83)), (298, 26)),
        ("right", ((13, 0), (143, 27), (125, 113), (0, 83)), (298, 30)),
        ("right", ((13, 0), (143, 27), (125, 113), (0, 83)), (302, 20)),
        ("right", ((13, 0), (141, 23), (120, 102), (0, 82)), (300, 24)),
        ("right", ((13, 0), (140, 22), (118, 100), (0, 82)), (299, 22)),
        ("right", ((9, 0), (128, 16), (109, 89), (0, 80)), (303, 23)),
    """
    params = [
        ("left", ((0, 11), (154, 0), (161, 89), (20, 104)), (18, 42)),
        ("left", ((0, 9), (153, 0), (159, 89), (20, 101)), (15, 38)),
        ("left", ((0, 7), (148, 0), (156, 89), (21, 97)), (14, 23)),
        None,
        ("right", ((10, 0), (143, 17), (124, 104), (0, 84)), (298, 18)),
        ("right", ((13, 0), (143, 27), (125, 113), (0, 83)), (298, 30)),
        ("right", ((13, 0), (143, 27), (125, 113), (0, 83)), (298, 26)),
        ("right", ((13, 0), (143, 27), (125, 113), (0, 83)), (298, 30)),
        ("right", ((13, 0), (143, 27), (125, 113), (0, 83)), (302, 20)),
        ("right", ((13, 0), (141, 23), (120, 102), (0, 82)), (300, 24)),
        ("right", ((13, 0), (140, 22), (118, 100), (0, 82)), (299, 22)),
        ("right", ((9, 0), (128, 16), (109, 89), (0, 80)), (303, 23)),
        None,
        ("left", ((0, 13), (152, 0), (158, 89), (17, 109)), (35, 36)),
        ("left", ((0, 13), (152, 0), (158, 89), (17, 109)), (31, 29)),
        ("left", ((0, 17), (149, 0), (155, 90), (17, 120)), (45, 33)),
        ("left", ((0, 14), (152, 0), (156, 91), (17, 115)), (40, 27)),
        ("left", ((0, 12), (154, 0), (158, 90), (17, 109)), (35, 28)),
    ]
    def perspective(peg, points):
        """
        透视变换

        :参数:
          * ``points``: 变换后点的位置，顺序依次为：左上->右上->右下->左下
        """

        def find_coeffs(pa, pb):
            matrix = []
            for p1, p2 in zip(pa, pb):
                matrix.append(
                    [p1[0], p1[1], 1, 0, 0, 0, -p2[0] * p1[0], -p2[0] * p1[1]]
                )
                matrix.append(
                    [0, 0, 0, p1[0], p1[1], 1, -p2[1] * p1[0], -p2[1] * p1[1]]
                )
            A = np.matrix(matrix, dtype=np.float32)
            B = np.array(pb).reshape(8)
            res = np.dot(np.linalg.inv(A.T * A) * A.T, B)
            return np.array(res).reshape(8)

        img_w, img_h = peg.size
        points_w = [p[0] for p in points]
        points_h = [p[1] for p in points]
        new_w = int(max(points_w) - min(points_w))
        new_h = int(max(points_h) - min(points_h))
        p = ((0, 0), (img_w, 0), (img_w, img_h), (0, img_h))
        coeffs = find_coeffs(points, p)
        return peg.transform(
                (new_w, new_h), Image.PERSPECTIVE, coeffs, Image.BICUBIC
            )
    frames: List[IMG] = []
    for i in range(18):
        frame = load_image(f"psyduck/{i}.jpg")
        param = params[i]
        if param:
            side, points, pos = param
            if side == "left":
                frame.paste(perspective(left_img,points), pos, perspective(left_img,points))
            elif side == "right":
                frame.paste(perspective(right_img,points), pos, perspective(right_img,points))
        frames.append(frame)
    return save_gif(frames, 0.2)

def petpet(img,img2, args:'圆',nickname,sex, **kwargs) -> BytesIO:
    
    frames = []
    locs = [
        (14, 20, 98, 98),
        (12, 33, 101, 85),
        (8, 40, 110, 76),
        (10, 33, 102, 84),
        (12, 20, 98, 98),
    ]
    if args=='圆':
        img = circle(img)
    for i in range(5):
        frame = Image.new("RGBA", (112, 112), (255, 255, 255, 0))
        x, y, w, h = locs[i]
        new_img = resize(img, (w, h))
        frame.paste(new_img, (x, y), mask=new_img)
        hand =load_image(f"petpet/{i}.png")
        frame.paste(hand, mask=hand)
        frames.append(frame)
    return save_gif(frames, 0.06)


def kiss(user_img,self_img,args,nickname,sex, **kwargs) -> BytesIO:

    # fmt: off
    user_locs = [
        (58, 90), (62, 95), (42, 100), (50, 100), (56, 100), (18, 120), (28, 110),
        (54, 100), (46, 100), (60, 100), (35, 115), (20, 120), (40, 96)
    ]
    self_locs = [
        (92, 64), (135, 40), (84, 105), (80, 110), (155, 82), (60, 96), (50, 80),
        (98, 55), (35, 65), (38, 100), (70, 80), (84, 65), (75, 65)
    ]
    # fmt: on
    frames = []
    for i in range(13):
        frame =load_image(f"kiss/{i}.png")
        user_head = resize(circle(user_img), (50, 50))
        frame.paste(user_head, user_locs[i], mask=user_head)
        self_head = resize(circle(self_img), (40, 40))
        frame.paste(self_head, self_locs[i], mask=self_head)
        frames.append(frame)
    return save_gif(frames, 0.05)


def rub(user_img,self_img, args,nickname,sex, **kwargs) -> BytesIO:
    # fmt: off
    user_locs = [
        (39, 91, 75, 75), (49, 101, 75, 75), (67, 98, 75, 75),
        (55, 86, 75, 75), (61, 109, 75, 75), (65, 101, 75, 75)
    ]
    self_locs = [
        (102, 95, 70, 80, 0), (108, 60, 50, 100, 0), (97, 18, 65, 95, 0),
        (65, 5, 75, 75, -20), (95, 57, 100, 55, -70), (109, 107, 65, 75, 0)
    ]
    # fmt: on
    frames = []
    for i in range(6):
        frame = load_image(f"rub/{i}.png")
        x, y, w, h = user_locs[i]
        user_head = resize(circle(user_img), (w, h))
        frame.paste(user_head, (x, y), mask=user_head)
        x, y, w, h, angle = self_locs[i]
        self_head = rotate(resize(circle(self_img), (w, h)), angle)
        frame.paste(self_head, (x, y), mask=self_head)
        frames.append(frame)
    return save_gif(frames, 0.05)


def play(img,img2 ,args,nickname,sex,**kwargs) -> BytesIO:
    locs = [
        (180, 60, 100, 100), (184, 75, 100, 100), (183, 98, 100, 100),
        (179, 118, 110, 100), (156, 194, 150, 48), (178, 136, 122, 69),
        (175, 66, 122, 85), (170, 42, 130, 96), (175, 34, 118, 95),
        (179, 35, 110, 93), (180, 54, 102, 93), (183, 58, 97, 92),
        (174, 35, 120, 94), (179, 35, 109, 93), (181, 54, 101, 92),
        (182, 59, 98, 92), (183, 71, 90, 96), (180, 131, 92, 101)
    ]
    # fmt: on
    raw_frames = []
    for i in range(23):
        raw_frame = load_image(f"play/{i}.png")
        raw_frames.append(raw_frame)
    img_frames = []
    for i in range(len(locs)):
        frame = Image.new("RGBA", (480, 400), (255, 255, 255, 0))
        x, y, w, h = locs[i]
        frame.paste(resize(img, (w, h)), (x, y))
        raw_frame = raw_frames[i]
        frame.paste(raw_frame, mask=raw_frame)
        img_frames.append(frame)
    frames = []
    for i in range(2):
        frames.extend(img_frames[0:12])
    frames.extend(img_frames[0:8])
    frames.extend(img_frames[12:18])
    frames.extend(raw_frames[18:23])
    return save_gif(frames, 0.06)


def pat(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    locs = [(11, 73, 106, 100), (8, 79, 112, 96)]
    img_frames = []
    for i in range(10):
        frame = Image.new("RGBA", (235, 196), (255, 255, 255, 0))
        x, y, w, h = locs[1] if i == 2 else locs[0]
        frame.paste(resize(img, (w, h)), (x, y))
        raw_frame = load_image(f"pat/{i}.png")
        frame.paste(raw_frame, mask=raw_frame)
        img_frames.append(frame)
    # fmt: off
    seq = [0, 1, 2, 3, 1, 2, 3, 0, 1, 2, 3, 0, 0, 1, 2, 3, 0, 0, 0, 0, 4, 5, 5, 5, 6, 7, 8, 9]
    # fmt: on
    frames = [img_frames[n] for n in seq]
    return save_gif(frames, 0.085)


def rip(
    user_img,self_img,  args:'滑稽',nickname,sex, **kwargs
) -> Union[str, BytesIO]:

    arg = "".join(args)
    if "滑稽" in arg:
        rip = load_image("rip/0.png")
    else:
        rip = load_image("rip/1.png")
    text = arg.strip("滑稽").strip()

    frame = Image.new("RGBA", rip.size, (255, 255, 255, 0))
    left = rotate(resize(user_img, (385, 385)), 24)
    right = rotate(resize(user_img, (385, 385)), -11)
    frame.paste(left, (-5, 355))
    frame.paste(right, (649, 310))
    frame.paste(resize(self_img, (230, 230)), (408, 418))
    frame.paste(rip, mask=rip)

    if text:
        fontname = BOLD_FONT
        fontsize = fit_font_size(text, rip.width - 50, 300, fontname, 150, 25)
        if not fontsize:
            return "文字太长了哦，改短点再试吧~"
        font = load_font(fontname, fontsize)
        text_w = font.getsize(text)[0]
        draw_text(
            frame,
            ((rip.width - text_w) / 2, 40),
            text,
            font=font,
            fill="#FF0000",
        )
    return save_jpg(frame)


def throw(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    img = resize(rotate(circle(img), random.randint(1, 360), expand=False), (143, 143))
    frame =load_image("throw/0.png")
    frame.paste(img, (15, 178), mask=img)
    return save_jpg(frame)


def throw_gif(img,img2, args,nickname,sex,**kwargs) -> BytesIO:
    locs = [
        [(32, 32, 108, 36)],
        [(32, 32, 122, 36)],
        [],
        [(123, 123, 19, 129)],
        [(185, 185, -50, 200), (33, 33, 289, 70)],
        [(32, 32, 280, 73)],
        [(35, 35, 259, 31)],
        [(175, 175, -50, 220)],
    ]
    frames = []
    for i in range(8):
        frame =load_image(f"throw_gif/{i}.png")
        for w, h, x, y in locs[i]:
            new_img = resize(circle(img), (w, h))
            frame.paste(new_img, (x, y), mask=new_img)
        frames.append(frame)
    return save_gif(frames, 0.1)


def crawl(img,img2, args,nickname,sex, **kwargs) -> BytesIO:
    img = resize(circle(img), (100, 100))
    crawl_total = 92
    crawl_num = random.randint(1, crawl_total)
    frame = load_image("crawl/{:02d}.jpg".format(crawl_num))
    frame.paste(img, (0, 400), mask=img)
    return save_jpg(frame)


def support(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    support = load_image("support/0.png")
    frame = Image.new("RGBA", support.size, (255, 255, 255, 0))
    img = rotate(resize(img, (815, 815)), 23)
    frame.paste(img, (-172, -17))
    frame.paste(support, mask=support)
    return save_jpg(frame)


def always(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    always = load_image("always/0.png")
    w, h = img.size
    h1 = int(h / w * 300)
    h2 = int(h / w * 60)
    height = h1 + h2 + 10

    def make(img: IMG) -> IMG:
        img = to_jpg(img)
        frame = Image.new("RGBA", (300, height), (255, 255, 255, 0))
        frame.paste(always, (0, h1 - 300 + int((h2 - 60) / 2)))
        frame.paste(resize(img, (300, h1)), (0, 0))
        frame.paste(resize(img, (60, h2)), (165, h1 + 5))
        return frame

    return make_jpg_or_gif(img, make)


def loading(img,img2, args,nickname,sex,**kwargs) -> BytesIO:
    bg = load_image("loading/0.png")
    icon = load_image("loading/1.png")
    w, h = img.size
    h1 = int(h / w * 300)
    h2 = int(h / w * 60)
    height = h1 + h2 + 10

    def make_static(img: IMG) -> IMG:
        img = to_jpg(img)
        frame = Image.new("RGBA", (300, height), (255, 255, 255, 0))
        frame.paste(bg, (0, h1 - 300 + int((h2 - 60) / 2)))
        img = resize(img, (300, h1))
        img = img.filter(ImageFilter.GaussianBlur(radius=2))
        frame.paste(img, (0, 0))
        mask = Image.new("RGBA", (300, h1), (0, 0, 0, 128))
        frame.paste(mask, (0, 0), mask=mask)
        frame.paste(icon, (100, int(h1 / 2) - 50), mask=icon)
        return frame

    frame = make_static(img)

    def make(img: IMG) -> IMG:
        new_img = frame.copy()
        new_img.paste(resize(img, (60, h2)), (60, h1 + 5))
        return new_img

    return make_jpg_or_gif(img, make)


def turn(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    img = circle(img)
    frames = []
    for i in range(0, 360, 10):
        frame = Image.new("RGBA", (250, 250), (255, 255, 255, 0))
        frame.paste(resize(rotate(img, i, False), (250, 250)), (0, 0))
        frames.append(to_jpg(frame))
    if random.randint(0, 1):
        frames.reverse()
    return save_gif(frames, 0.05)


def littleangel(
    img,img2, args,nickname,sex, **kwargs
) -> Union[str, BytesIO]:
    img = to_jpg(img).convert("RGBA")
    img = limit_size(img, (500, 500), FitSizeMode.INSIDE)
    img_w, img_h = img.size

    bg = Image.new("RGB", (600, img_h + 230), (255, 255, 255))
    bg.paste(img, (int(300 - img_w / 2), 110))
    fontname = BOLD_FONT

    font = load_font(fontname, 48)
    text = "非常可爱！简直就是小天使"
    text_w, _ = font.getsize(text)
    draw_text(
        bg, (300 - text_w / 2, img_h + 120), text, font=font, fill=(0, 0, 0)
    )

    font = load_font(fontname, 26)
    ta = "她" if sex == "male" else "他"
    text = f"{ta}没失踪也没怎么样  我只是觉得你们都该看一下"
    text_w, _ = font.getsize(text)
    draw_text(
        bg, (300 - text_w / 2, img_h + 180), text, font=font, fill=(0, 0, 0)
    )

    text = f"请问你们看到{nickname}了吗?"
    fontsize = fit_font_size(text, 560, 110, fontname, 70, 25)
    if not fontsize:
        return "名字太长了哦，改短点再试吧~"

    font = load_font(fontname, fontsize)
    text_w, text_h = font.getsize(text)
    x = 300 - text_w / 2
    y = 55 - text_h / 2
    draw_text(bg, (x, y), text, font=font, fill=(0, 0, 0))
    return save_jpg(bg)


def dont_touch(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    frame =load_image("dont_touch/0.png")
    frame.paste(resize(img, (170, 170)), (23, 231))
    return save_jpg(frame)


def alike(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    frame = load_image("alike/0.png")
    frame.paste(resize(img, (90, 90)), (131, 14))
    return save_jpg(frame)


def roll(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    frames = []
    # fmt: off
    locs = [
        (87, 77, 0), (96, 85, -45), (92, 79, -90), (92, 78, -135),
        (92, 75, -180), (92, 75, -225), (93, 76, -270), (90, 80, -315)
    ]
    # fmt: on
    for i in range(8):
        frame = Image.new("RGBA", (300, 300), (255, 255, 255, 0))
        x, y, a = locs[i]
        frame.paste(rotate(resize(img, (210, 210)), a, expand=False), (x, y))
        bg = load_image(f"roll/{i}.png")
        frame.paste(bg, mask=bg)
        frames.append(frame)
    return save_gif(frames, 0.1)


def play_game(
    img,img2, args,nickname,sex, **kwargs
) -> Union[str, BytesIO]:
    bg = load_image("play_game/1.png")
    text = args#[0] if args else "来玩休闲游戏啊"
    fontname = DEFAULT_FONT
    fontsize = fit_font_size(text, 520, 110, fontname, 35, 25)
    if not fontsize:
        return "描述太长了哦，改短点再试吧~"
    font =load_font(fontname, fontsize)
    text_w = font.getsize(text)[0]

    def make(img: IMG) -> IMG:
        img = to_jpg(img)
        frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
        points = [(0, 5), (227, 0), (216, 150), (0, 165)]
        screen = rotate(perspective(fit_size(img, (220, 160)), points), 9)
        frame.paste(screen, (161, 117))
        frame.paste(bg, mask=bg)

        draw_text(
            frame,
            (263 - text_w / 2, 430),
            text,
            font=font,
            fill="#000000",
            stroke_fill="#FFFFFF",
            stroke_width=2,
        )
        return frame

    return make_jpg_or_gif(img, make)


def worship(img,img2, args,nickname,sex,**kwargs) -> BytesIO:
    points = [(0, -30), (135, 17), (135, 145), (0, 140)]
    paint = perspective(resize(img, (150, 150)), points)
    frames = []
    for i in range(10):
        frame = Image.new("RGBA", (300, 169), (255, 255, 255, 0))
        frame.paste(paint)
        bg = load_image(f"worship/{i}.png")
        frame.paste(bg, mask=bg)
        frames.append(frame)
    return save_gif(frames, 0.04)


def eat(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    img = resize(img, (32, 32))
    frames = []
    for i in range(3):
        frame = Image.new("RGBA", (60, 67), (255, 255, 255, 0))
        frame.paste(img, (1, 38))
        bg = load_image(f"eat/{i}.png")
        frame.paste(bg, mask=bg)
        frames.append(frame)
    return save_gif(frames, 0.05)


def bite(img,img2, args,nickname,sex,**kwargs) -> BytesIO:
    raw_frames = []
    for i in range(16):
        raw_frame = load_image(f"bite/{i}.png")
        raw_frames.append(raw_frame)
    frames = []
    # fmt: off
    locs = [
        (90, 90, 105, 150), (90, 83, 96, 172), (90, 90, 106, 148),
        (88, 88, 97, 167), (90, 85, 89, 179), (90, 90, 106, 151)
    ]
    # fmt: on
    for i in range(6):
        frame = Image.new("RGBA", (362, 364), (255, 255, 255, 0))
        x, y, w, h = locs[i]
        frame.paste(resize(img, (w, h)), (x, y))
        raw_frame = load_image(f"bite/{i}.png")
        frame.paste(raw_frame, mask=raw_frame)
        frames.append(frame)
    frames.extend(raw_frames[6:])
    return save_gif(frames, 0.07)


def police(img,img2, args,nickname,sex,**kwargs) -> BytesIO:
    bg = load_image("police/0.png")
    frame = Image.new("RGBA", bg.size)
    frame.paste(resize(img, (245, 245)), (224, 46))
    frame.paste(bg, mask=bg)
    return save_jpg(frame)


def police1(img,img2, args,nickname,sex,**kwargs) -> BytesIO:
    
    img = to_jpg(img).convert("RGBA")
    bg = load_image("police/1.png")
    frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
    frame.paste(rotate(fit_size(img, (60, 75)), 16), (37, 291))
    frame.paste(bg, mask=bg)
    return save_jpg(frame)

def painter(img,img2, args,nickname,sex, **kwargs):
    #img = img.resize((int(img.width*345/img.height), 345))
    frame = load_image("painter/0.png")
    #int(frame.width/2)-int(fontsize*len(text)/2), frame.height - 50, int(frame.width/2)-int(fontsize*len(text)/2), frame.height
    def make(img):
        new_img = Image.new(frame.mode, frame.size)
        w=img.width
        h=img.height
        new_img.paste(img.resize((int(w*345/h), 345)),(245-int(w*345/h/2), 91))
        new_img.paste(frame, frame)
        return new_img
    #new_img = Image.new(frame.mode, frame.size)    
    #new_img.paste(img, (125, 91))
    #new_img.paste(frame, frame)
    return make_jpg_or_gif(img, make,0.5,5)
    #return save_jpg(new_img)

def anyasuki(img,img2, args,nickname,sex, **kwargs):
    frame = load_image("anyasuki/0.png")
    if not args:
        text="阿尼亚喜欢这个"
    else:
        text=args
    fontname = BOLD_FONT
    fontsize =fit_font_size(text, frame.width - 50, 300, fontname, 40, 20)
    font = load_font(fontname, fontsize)
    try:
        draw_text(
            frame,
            (int(frame.width/2)-int(fontsize*len(text)/2), frame.height - 50, int(frame.width/2)-int(fontsize*len(text)/2), frame.height),
            text,
            font,
            fill="white",
        )
    except ValueError:
        return

    def make(img):
        new_img = Image.new(frame.mode, frame.size)    
        new_img.paste(img.resize((305, 235)), (106, 72))
        new_img.paste(frame, frame)
        return new_img

    return make_jpg_or_gif(img, make)


def ask(
    img,img2, args,nickname,sex, **kwargs
) -> Union[str, BytesIO]:
    
    img = to_jpg(img).convert("RGBA")
    img = limit_size(img, (640, 0))
    img_w, img_h = img.size
    mask_h = 150
    start_t = 180
    gradient = Image.new("L", (1, img_h))
    for y in range(img_h):
        t = 0 if y < img_h - mask_h else img_h - y + start_t - mask_h
        gradient.putpixel((0, y), t)
    alpha = gradient.resize((img_w, img_h))
    mask = Image.new("RGBA", (img_w, img_h))
    mask.putalpha(alpha)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=3))
    img = Image.alpha_composite(img, mask)
    
    name = nickname
    ta = "他" if sex == "male" else "她"
    if not name:
        return "error~"

    font = load_font(BOLD_FONT, 25)
    start_h = img_h - mask_h
    
    text_w = font.getsize(name)[0]
    start_w = 640/2-int(text_w/2)
    line_w = text_w + 200
    draw_text(
        img,
        (start_w, start_h + 5),
        name,
        font=font,
        fill="orange",
    )
    draw = ImageDraw.Draw(img)
    start_w = 640/2-int(line_w/2)
    draw.line(
        (start_w, start_h + 45, start_w + line_w, start_h + 45), fill="orange", width=2
    )
    text_w = font.getsize(f"{name}不知道哦")[0]
    start_w = 640/2-int(text_w/2)
    draw_text(
        img,
        (start_w , start_h + 50),
        f"{name}不知道哦。",
        font=font,
        fill="white",
    )

    sep_w = 30
    sep_h = 80
    bg = Image.new("RGBA", (img_w + sep_w * 2, img_h + sep_h * 2), "white")
    font = load_font(DEFAULT_FONT, 35)
    if font.getsize(name)[0] > 600:
        return "error~"
    #text_w = font.getsize(f"让{name}告诉你吧")[0]
    #start_w = 640/2-int(text_w/2)+sep_w
    draw_text(bg, (sep_w, 10), f"让{name}告诉你吧", font=font, fill="black")
    #text_w = font.getsize(f"啊这，{ta}说不知道")[0]
    #start_w = 640/2-int(text_w/2)+sep_w
    draw_text(
        bg, (sep_w, sep_h + img_h + 10), f"啊这，{ta}说不知道", font=font, fill="black"
    )
    bg.paste(img, (sep_w, sep_h))
    return save_jpg(bg)


def prpr(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    
    bg = load_image("prpr/0.png")

    def make(img: IMG) -> IMG:
        img = to_jpg(img)
        frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
        points = [(0, 19), (236, 0), (287, 264), (66, 351)]
        screen = perspective(fit_size(img, (330, 330)), points)
        frame.paste(screen, (56, 284))
        frame.paste(bg, mask=bg)
        return frame

    return make_jpg_or_gif(img, make)


def twist(img,img2, args,nickname,sex,**kwargs) -> BytesIO:
    
    frames = []
    # fmt: off
    locs = [
        (25, 66, 0), (25, 66, 60), (23, 68, 120),
        (20, 69, 180), (22, 68, 240), (25, 66, 300)
    ]
    # fmt: on
    for i in range(5):
        frame = Image.new("RGBA", (166, 168), (255, 255, 255, 0))
        x, y, a = locs[i]
        frame.paste(rotate(resize(img, (78, 78)), a, expand=False), (x, y))
        bg = load_image(f"twist/{i}.png")
        frame.paste(bg, mask=bg)
        frames.append(frame)
    return save_gif(frames, 0.1)


def wallpaper(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    
    bg = load_image("wallpaper/0.png")

    def make(img: IMG) -> IMG:
        img = to_jpg(img)
        frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
        frame.paste(fit_size(img, (775, 496)), (260, 580))
        frame.paste(bg, mask=bg)
        return frame

    return make_jpg_or_gif(img, make, gif_zoom=0.5)


def china_flag(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    
    bg = load_image("china_flag/0.png")
    frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
    frame.paste(resize(img, bg.size))
    frame.paste(bg, mask=bg)
    return save_jpg(frame)


def make_friend(
    img,img2, args,nickname,sex, **kwargs
) -> Union[str, BytesIO]:
    
    img = to_jpg(img).convert("RGBA")
    img = limit_size(img, (1000, 0))
    img_w, img_h = img.size

    bg = load_image("make_friend/0.png")
    frame = img.copy()
    frame.paste(rotate(limit_size(img, (250, 0)), 9), (743, img_h - 155))
    frame.paste(rotate(resize(square(img), (55, 55)), 9), (836, img_h - 278))
    frame.paste(bg, (0, img_h - 1000), mask=bg)
    font = load_font(DEFAULT_FONT, 40)

    name = nickname
    if not name:
        return "找不到名字，加上名字再试吧~"
    text_frame = Image.new("RGBA", (500, 50))
    draw_text(text_frame, (0, -10), name, font=font, fill="#FFFFFF")
    text_frame = rotate(resize(text_frame, (250, 25)), 9)
    frame.paste(text_frame, (710, img_h - 340), mask=text_frame)
    return save_jpg(frame)


def back_to_work(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    
    img = to_jpg(img).convert("RGBA")
    bg = load_image("back_to_work/1.png")
    frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
    new_img = fit_size(img, (220, 310), direction=FitSizeDir.NORTH)
    frame.paste(rotate(new_img, 25), (56, 32))
    frame.paste(bg, mask=bg)
    return save_jpg(frame)


def perfect(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    
    img = to_jpg(img).convert("RGBA")
    frame = load_image("perfect/0.png")
    new_img = fit_size(img, (310, 460), mode=FitSizeMode.INSIDE)
    frame.paste(new_img, (313, 64), mask=new_img)
    return save_jpg(frame)


def follow(
    img2,img, args,nickname,sex, **kwargs
) -> Union[str, BytesIO]:
    
    img = resize(circle(img), (200, 200))

    font = load_font(DEFAULT_FONT, 60)
    ta = "女同" if sex == "female" else "男同"
    if args:
        text_name=args
    else:
        text_name = ta
    text_name_w, text_name_h = font.getsize(text_name)
    text_follow = "关注了"+nickname
    text_width = max(text_name_w, font.getsize(text_follow)[0])
    if text_width >= 1000:
        return "名字太长了哦，改短点再试吧~"

    frame = Image.new("RGBA", (300 + text_width + 50, 300), (255, 255, 255, 0))
    frame.paste(img, (50, 50), mask=img)
    text_frame = Image.new("RGBA", (text_width + 50, 300), (255, 255, 255, 0))
    draw_text(
        text_frame, (0, 135 - text_name_h), text_name, font=font, fill="black"
    )
    draw_text(text_frame, (0, 145), text_follow, font=font, fill="grey")
    frame.paste(text_frame, (300, 0), mask=text_frame)

    return save_jpg(frame)


def my_friend(
    img,img2, args,nickname,sex, **kwargs
) -> Union[str, BytesIO]:
    
    if not args:
        exit()
    else:
        name = nickname or "朋友"
        texts = args

    name_font = load_font(DEFAULT_FONT, 25)
    text_font = load_font(DEFAULT_FONT, 40)
    name_w, name_h = name_font.getsize(name)
    if name_w >= 700:
        return "名字太长了哦，改短点再试吧~"

    corner1 = load_image("my_friend/corner1.png")
    corner2 = load_image("my_friend/corner2.png")
    corner3 = load_image("my_friend/corner3.png")
    corner4 = load_image("my_friend/corner4.png")
    label =  load_image("my_friend/2.png")
    img = resize(circle(img), (100, 100))

    def make_dialog(text: str) -> IMG:
        text = "\n".join(wrap_text(text, text_font, 700))
        text_w, text_h = text_font.getsize_multiline(text)
        box_w = max(text_w, name_w + 15) + 140
        box_h = max(text_h + 103, 150)
        box = Image.new("RGBA", (box_w, box_h))
        box.paste(corner1, (0, 0))
        box.paste(corner2, (0, box_h - 75))
        box.paste(corner3, (text_w + 70, 0))
        box.paste(corner4, (text_w + 70, box_h - 75))
        box.paste(Image.new("RGBA", (text_w, box_h - 40), "#ffffff"), (70, 20))
        box.paste(Image.new("RGBA", (text_w + 88, box_h - 150), "#ffffff"), (27, 75))

        draw_text(
            box,
            (70, 15 + (box_h - 40 - text_h) / 2),
            text,
            font=text_font,
            fill="#000000",
        )
        dialog = Image.new("RGBA", (box.width + 130, box.height + 60), "#eaedf4")
        dialog.paste(img, (20, 20), mask=img)
        dialog.paste(box, (130, 60), mask=box)
        dialog.paste(label, (160, 25))
        draw_text(
            dialog, (260, 22 + (35 - name_h) / 2), name, font=name_font, fill="#868894"
        )
        return dialog
    def make_pic(pic):
        box_w = max(pic.width, name_w + 15) + 140
        box_h = max(pic.height + 103, 150)
        box = Image.new("RGBA", (box_w, box_h))
        box.paste(corner1, (0, 0))
        box.paste(corner2, (0, box_h - 75))
        box.paste(corner3, (pic.width + 70, 0))
        box.paste(corner4, (pic.width + 70, box_h - 75))
        box.paste(Image.new("RGBA", (pic.width, box_h - 40), "#ffffff"), (70, 20))
        box.paste(Image.new("RGBA", (pic.width + 88, box_h - 150), "#ffffff"), (27, 75))
        box.paste(pic, (75, 50),pic)

        dialog = Image.new("RGBA", (box.width + 130, box.height + 60), "#eaedf4")
        dialog.paste(img, (20, 20), mask=img)
        dialog.paste(box, (130, 60), mask=box)
        dialog.paste(label, (160, 25))
        draw_text(
            dialog, (260, 22 + (35 - name_h) / 2), name, font=name_font, fill="#868894"
        )
        return dialog
    dialogs = [make_dialog(texts)]#for text in texts
    frame_w = max((dialog.width for dialog in dialogs))
    frame_h = sum((dialog.height for dialog in dialogs))
    frame = Image.new("RGBA", (frame_w, frame_h), "#eaedf4")
    current_h = 0
    for dialog in dialogs:
        frame.paste(dialog, (0, current_h))
        current_h += dialog.height
    return save_jpg(frame)


def paint(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    
    img = to_jpg(img).convert("RGBA")
    bg = load_image("paint/0.png")
    frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
    frame.paste(rotate(fit_size(img, (117, 135)), 4), (95, 107))
    frame.paste(bg, mask=bg)
    return save_jpg(frame)


def shock(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    
    #img = resize(img, (300, 300))
    
    def make(img):
        for i in range(30):
            return rotate(
                    motion_blur(img.convert("RGBA"), random.randint(-90, 90), random.randint(0, 90)),
                    random.randint(-20, 20),
                    expand=False,
                )
    return make_jpg_or_gif(img, make,0.5,20)


def coupon(
    img,img2, args,nickname,sex, **kwargs
) -> Union[str, BytesIO]:
    
    bg = load_image("coupon/0.png")
    new_img = rotate(resize(circle(img), (60, 60)), 22)
    bg.paste(new_img, (164, 85), mask=new_img)

    font = load_font(DEFAULT_FONT, 30)
    text_img = Image.new("RGBA", (250, 100))
    text = f"{nickname}陪睡券"
    text += "\n（永久有效）"
    text_w = font.getsize_multiline(text)[0]
    if text_w > text_img.width:
        return "文字太长了哦，改短点再试吧~"

    draw_text(
        text_img,
        ((text_img.width - text_w) / 2, 0),
        text,
        font=font,
        align="center",
        fill="#000000",
    )
    text_img = rotate(text_img, 22)
    bg.paste(text_img, (94, 108), mask=text_img)
    return save_jpg(bg)


def listen_music(img,img2, args,nickname,sex,**kwargs) -> BytesIO:
    
    img = circle(img)
    bg = load_image("listen_music/0.png")
    frames = []
    for i in range(0, 360, 10):
        frame = Image.new("RGBA", (414, 399))
        temp_img = resize(rotate(img, -i, False), (215, 215))
        frame.paste(temp_img, (100, 100), mask=temp_img)
        frame.paste(bg, (0, 0), mask=bg)
        frames.append(to_jpg(frame))
    return save_gif(frames, 0.05)


def dianzhongdian(
    img,img2, args,nickname,sex, **kwargs
) -> Union[str, BytesIO]:
    
    img = to_jpg(img)

    if "彩" in args:
        args = args.replace('彩','')
    else:
        img = img.convert("L")

    img = limit_size(img, (500, 500), FitSizeMode.INSIDE)
    img_w, img_h = img.size
    frames: List[IMG] = [img]

    def text_frame(text: str, max_fontsize: int, min_fontsize: int) -> int:
        fontname = DEFAULT_FONT
        fontsize = fit_font_size(
            text, img_w - 20, img_h, fontname, max_fontsize, min_fontsize
        )
        if not fontsize:
            return fontsize
        font = load_font(fontname, fontsize)
        text_w, text_h = font.getsize(text)
        frame = Image.new("RGB", (img_w, text_h + 5), "#000000")
        draw_text(frame, ((img_w - text_w) / 2, 0), text, font=font, fill="white")
        frames.append(frame)
        return fontsize

    fontsize = text_frame(args, 50, 10)
    text = translate(args)
    if text:
        fontsize = max(int(fontsize / 2), 10)
        fontsize = text_frame(text, fontsize, 10)
        if not fontsize:
            return "文字太长了哦，改短点再试吧~"

    frame = Image.new("RGB", (img_w, sum((f.height for f in frames)) + 10), "#000000")
    current_h = 0
    for f in frames:
        frame.paste(f, (0, current_h))
        current_h += f.height
    return save_jpg(frame)


def funny_mirror(img,img2,args,nickname,sex,**kwargs) -> BytesIO:
    
    #img = resize(img, (500, 500))
    pic_size=0.5
    img_face=resize(img.convert("RGBA"),(500, 500))
    frames = [img_face]
    coeffs = [0.01, 0.03, 0.05, 0.08, 0.12, 0.17, 0.23, 0.3, 0.4, 0.6]
    borders = [25, 52, 67, 83, 97, 108, 118, 128, 138, 148]
    if not getattr(img, "is_animated", False):
        for i in range(10):
            new_size = 500 - borders[i] * 2
            frames.append(resize(
                cut_size(distort(img.convert("RGBA"), (coeffs[i], 0, 0, 0)), (new_size, new_size)),
                (500,500),
                ))
        frames.extend(frames[::-1])
    else:
        index = range(img.n_frames)
        ratio = img.n_frames/10
        duration = img.info["duration"] / 1000
        if ratio > 1:
            index = (int(i * ratio) for i in range(10))
            duration *= ratio
        j=0
        for i in index:
            img.seek(i)
            new_size = 500 - borders[j] * 2
            new_img1=resize(img.convert("RGBA"),(500,500))
            new_img=resize(
                cut_size(distort(new_img1, (coeffs[j], 0, 0, 0)), (new_size, new_size)),
                (500,500),
                )
            new_img1.paste(new_img,new_img)
            frames.append(new_img1)
                          
            j+=1
            if j==10:
                break

        frames.extend(frames[::-1])
    return save_gif(frames, 0.05)


def love_you(img,img2, args,nickname,sex,**kwargs) -> BytesIO:
    
    frames = []
    locs = [(68, 65, 70, 70), (63, 59, 80, 80)]
    for i in range(2):
        heart = load_image(f"love_you/{i}.png")
        frame = Image.new("RGBA", heart.size, (255, 255, 255, 0))
        x, y, w, h = locs[i]
        frame.paste(resize(img, (w, h)), (x, y))
        frame.paste(heart, mask=heart)
        frames.append(frame)
    return save_gif(frames, 0.2)


def symmetric(
    img,img2, args,nickname,sex, **kwargs
) -> Union[str, BytesIO]:
    
    img = limit_size(img, (500, 500), FitSizeMode.INSIDE)
    img_w, img_h = img.size

    boxes = {
        "left": {
            "mode": Image.FLIP_LEFT_RIGHT,
            "frame_box": (img_w // 2 * 2, img_h),
            "first_box": (0, 0, img_w // 2, img_h),
            "first_position": (0, 0),
            "second_box": (img_w // 2, 0, img_w // 2 * 2, img_h),
            "second_position": (img_w // 2, 0),
        },
        "right": {
            "mode": Image.FLIP_LEFT_RIGHT,
            "frame_box": (img_w // 2 * 2, img_h),
            "first_box": (img_w // 2, 0, img_w // 2 * 2, img_h),
            "first_position": (img_w // 2, 0),
            "second_box": (0, 0, img_w // 2, img_h),
            "second_position": (0, 0),
        },
        "top": {
            "mode": Image.FLIP_TOP_BOTTOM,
            "frame_box": (img_w, img_h // 2 * 2),
            "first_box": (0, 0, img_w, img_h // 2),
            "first_position": (0, 0),
            "second_box": (0, img_h // 2, img_w, img_h // 2 * 2),
            "second_position": (0, img_h // 2),
        },
        "bottom": {
            "mode": Image.FLIP_TOP_BOTTOM,
            "frame_box": (img_w, img_h // 2 * 2),
            "first_box": (0, img_h // 2, img_w, img_h // 2 * 2),
            "first_position": (0, img_h // 2),
            "second_box": (0, 0, img_w, img_h // 2),
            "second_position": (0, 0),
        },
    }

    mode = "left"
    if args:
        if "右" in args:
            mode = "right"
        elif "上" in args:
            mode = "top"
        elif "下" in args:
            mode = "bottom"

    first = img
    second = img.transpose(boxes[mode]["mode"])
    frame = Image.new("RGBA", boxes[mode]["frame_box"], (255, 255, 255, 0))

    first = first.crop(boxes[mode]["first_box"])
    frame.paste(first, boxes[mode]["first_position"])
    second = second.crop(boxes[mode]["second_box"])
    frame.paste(second, boxes[mode]["second_position"])

    return save_jpg(frame)


def safe_sense(
    img,img2, args,nickname,sex, **kwargs
) -> Union[str, BytesIO]:
    img = fit_size(to_jpg(img).convert("RGBA"), (215, 343))
    frame =load_image(f"safe_sense/0.png")
    frame.paste(img, (215, 135))

    ta = "她" if sex == "female" else "他"
    texts = ["你给我的安全感", f"远不及{ta}的万分之一"] if args=='安全感' else [args]
    text = "\n".join(texts)

    fontname = DEFAULT_FONT
    fontsize = fit_font_size(text, 400, 100, fontname, 70, 10)
    if not fontsize:
        return "文字太长了哦，改短点再试吧~"
    font = load_font(fontname, fontsize)
    text_w, text_h = font.getsize_multiline(text)
    draw_text(
        frame,
        ((frame.width - text_w) / 2, 30 + (45 - text_h) / 2),
        text,
        font=font,
        fill="black",
        align="center",
    )
    return save_jpg(frame)


def always_like(
    img,img2, args,nickname,sex, **kwargs
) -> Union[str, BytesIO]:
    img = to_jpg(img).convert("RGBA")
    text = "我永远喜欢" + nickname
    fontname = BOLD_FONT
    fontsize = fit_font_size(text, 800, 100, fontname, 70, 30)
    if not fontsize:
        return "名字太长了哦，改短点再试吧~"

    def random_color():
        return random.choice(
            ["red", "darkorange", "gold", "darkgreen", "blue", "cyan", "purple"]
        )

    frame = load_image(f"always_like/0.png")
    frame.paste(fit_size(img, (350, 400), FitSizeMode.INSIDE), (25, 35))
    font = load_font(fontname, fontsize)
    text_w, text_h = font.getsize(text)
    draw = ImageDraw.Draw(frame)
    start_w = (frame.width - text_w) / 2
    start_h = 470 + (100 - text_h) / 2
    draw_text(frame, (start_w, start_h), text, font=font, fill="black")
    
    return save_jpg(frame)


def interview(
    user_img,self_img, args,nickname,sex, **kwargs
) -> Union[str, BytesIO]:
    #self_img = to_jpg(load_image("interview/huaji.png"))
    self_img = resize(self_img, (124, 124))
    user_img = resize(user_img, (124, 124))

    frame = Image.new("RGB", (600, 310), "white")
    microphone = load_image("interview/microphone.png")
    frame.paste(microphone, (330, 103), mask=microphone)
    frame.paste(self_img, (419, 40))
    frame.paste(user_img, (57, 40))

    text = args#[0] if args else "采访大佬经验"
    fontname = DEFAULT_FONT
    fontsize =fit_font_size(text, 550, 100, fontname, 50, 20)
    if not fontsize:
        return "文字太长了哦，改短点再试吧~"
    font =load_font(fontname, fontsize)
    text_w, text_h = font.getsize(text)
    draw_text(
        frame,
        ((600 - text_w) / 2, 200 + (100 - text_h) / 2),
        text,
        font=font,
        fill="black",
    )
    return save_jpg(frame)


def punch(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    
    img = to_jpg(img).convert("RGBA")
    img = limit_size(img, (260, 230))
    x = int((260 - img.width) / 2)
    y = int((230 - img.height) / 2)
    frames = []
    # fmt: off
    locs = [
        (-50, 20), (-40, 10), (-30, 0), (-20, -10), (-10, -10), (0, 0),
        (10, 10), (20, 20), (10, 10), (0, 0), (-10, -10), (10, 0), (-30, 10)
    ]
    # fmt: on
    for i in range(13):
        frame = Image.new("RGBA", (260, 230), (255, 255, 255, 0))
        dx, dy = locs[i]
        frame.paste(img, (x + dx, y + dy))
        fist = load_image(f"punch/{i}.png")
        frame.paste(fist, mask=fist)
        frames.append(frame)
    return save_gif(frames, 0.03)


def cyan(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    
    img = resize(img, (500, 500))
    color = (78, 114, 184)
    img = color_mask(img, color)
    font =load_font(BOLD_FONT, 80)
    draw_text(
        img,
        (400, 50),
        "群\n青",
        font=font,
        fill="white",
        stroke_width=2,
        stroke_fill=color,
    )
    font = load_font(DEFAULT_FONT, 40)
    draw_text(
        img,
        (310, 270),
        "YOASOBI",
        font=font,
        fill="white",
        stroke_width=2,
        stroke_fill=color,
    )
    return save_jpg(img)


def pound(img,img2,args,nickname,sex,**kwargs) -> BytesIO:
    
    # fmt: off
    locs = [
        (135, 240, 138, 47), (135, 240, 138, 47), (150, 190, 105, 95), (150, 190, 105, 95),
        (148, 188, 106, 98), (146, 196, 110, 88), (145, 223, 112, 61), (145, 223, 112, 61)
    ]
    # fmt: on
    frames = []
    for i in range(8):
        bg = load_image(f"pound/{i}.png")
        frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
        x, y, w, h = locs[i]
        frame.paste(resize(img, (w, h)), (x, y))
        frame.paste(bg, mask=bg)
        frames.append(frame)
    return save_gif(frames, 0.05)


def thump(img,imag2,args,nickname,sex, **kwargs) -> BytesIO:
    #
    # fmt: off
    locs = [(65, 128, 77, 72), (67, 128, 73, 72), (54, 139, 94, 61), (57, 135, 86, 65)]
    # fmt: on
    frames = []
    for i in range(4):
        bg = load_image(f"thump/{i}.png")
        frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
        x, y, w, h = locs[i]
        frame.paste(resize(img, (w, h)), (x, y))
        frame.paste(bg, mask=bg)
        frames.append(frame)
    return save_gif(frames, 0.04)


def need(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    
    bg = load_image("need/0.png")
    frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
    frame.paste(resize(img, (115, 115)), (327, 232))
    frame.paste(bg, mask=bg)
    return save_jpg(frame)


def cover_face(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    
    bg = load_image("cover_face/0.png")
    frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
    points = [(15, 11), (448, 0), (445, 452), (0, 461)]
    screen = perspective(resize(img, (450, 450)), points)
    frame.paste(screen, (120, 154))
    frame.paste(bg, mask=bg)
    return save_jpg(frame)


def knock(img,img2, args,nickname,sex,**kwargs) -> BytesIO:
    
    # fmt: off
    locs = [(60, 308, 210, 195), (60, 308, 210, 198), (45, 330, 250, 172), (58, 320, 218, 180),
            (60, 310, 215, 193), (40, 320, 250, 285), (48, 308, 226, 192), (51, 301, 223, 200)]
    # fmt: on
    frames = []
    for i in range(8):
        bg = load_image(f"knock/{i}.png")
        frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
        x, y, w, h = locs[i]
        frame.paste(resize(img, (w, h)), (x, y))
        frame.paste(bg, mask=bg)
        frames.append(frame)
    return save_gif(frames, 0.04)


def garbage(img,img2,args,nickname,sex, **kwargs) -> BytesIO:
    
    img = resize(img, (79, 79))
    # fmt: off
    locs = [(39, 40)] * 3 + [(39, 30)] * 2 + [(39, 32)] * 10 + [(39, 30), (39, 27), (39, 32), (37, 49), (37, 64), (37, 67), (37, 67), (39, 69), (37, 70), (37, 70)]  # type: ignore
    # fmt: on
    frames = []
    for i in range(25):
        bg = load_image(f"garbage/{i}.png")
        frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
        frame.paste(img, locs[i])
        frame.paste(bg, mask=bg)
        frames.append(frame)
    return save_gif(frames, 0.04)


def whyatme(img,img2, args,nickname,sex,**kwargs) -> BytesIO:
    
    bg = load_image("whyatme/0.png")
    frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
    frame.paste(resize(img, (265, 265)), (42, 13))
    frame.paste(bg, mask=bg)
    return save_jpg(frame)


def decent_kiss(img,img2, args,nickname,sex,**kwargs) -> BytesIO:
    
    img = to_jpg(img).convert("RGBA")
    bg = load_image("decent_kiss/0.png")
    frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
    frame.paste(fit_size(img, (589, 340)), (0, 91))
    frame.paste(bg, mask=bg)
    return save_jpg(frame)

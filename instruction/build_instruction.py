# -*- coding: utf-8 -*-
"""Инструкция-карусель EWA (5 слайдов 1080x1350) для покупателя.
Палитра: чёрный #0A0A0A, маджента #D6127F, светлый розовый #F5C4E0, белый."""
import os
from PIL import Image, ImageDraw, ImageFont

SS = 2  # supersampling для сглаживания
W, H = 1080, 1350
A = os.path.dirname(os.path.abspath(__file__))
FD = os.path.join(A, "assets")
OUT = os.path.join(A, "png")
os.makedirs(OUT, exist_ok=True)

BLACK = (10, 10, 10)
MAGENTA = (214, 18, 127)
PINK = (245, 196, 224)
WHITE = (255, 255, 255)
GREEN = (46, 196, 120)
GREY = (150, 150, 150)

def font(weight, size):
    name = "Montserrat-Black.ttf" if weight == "black" else "Montserrat-SemiBold.ttf"
    return ImageFont.truetype(os.path.join(FD, name), size * SS)

def txt(d, xy, s, f, fill, anchor="la", lsp=0):
    lines = s.split("\n")
    x, y = xy[0]*SS, xy[1]*SS
    if anchor[0] == "m":
        x = xy[0]*SS
    line_h = f.size + lsp*SS
    if anchor[1] == "m":
        y = xy[1]*SS - (len(lines)*line_h)//2
    elif anchor[1] == "d":
        y = xy[1]*SS - len(lines)*line_h
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill, anchor=anchor[0]+"a")
        y += line_h

def save(img, n):
    img.resize((W, H), Image.LANCZOS).save(os.path.join(OUT, f"{n}.png"))
    print("✓", n)

def new(bg):
    img = Image.new("RGB", (W*SS, H*SS), bg)
    return img, ImageDraw.Draw(img)

# ---------- значки ----------
def icon_check(d, cx, cy, r, col):
    cx, cy, r = cx*SS, cy*SS, r*SS
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=col)
    d.line([(cx-r*0.45, cy+r*0.05), (cx-r*0.05, cy+r*0.45), (cx+r*0.55, cy-r*0.35)], fill=WHITE, width=int(8*SS))

def icon_phone(d, cx, cy, r, col):
    cx, cy, r = cx*SS, cy*SS, r*SS
    d.rounded_rectangle([cx-r*0.45, cy-r*0.75, cx+r*0.45, cy+r*0.75], radius=int(10*SS), fill=col)
    d.rounded_rectangle([cx-r*0.35, cy-r*0.6, cx+r*0.35, cy+r*0.55], radius=int(3*SS), fill=BLACK)
    d.ellipse([cx-r*0.1, cy+r*0.6, cx+r*0.1, cy+r*0.72], fill=col)

def icon_cloud(d, cx, cy, r, col):
    cx, cy, r = cx*SS, cy*SS, r*SS
    d.ellipse([cx-r*0.7, cy-r*0.3, cx-r*0.1, cy+r*0.45], fill=col)
    d.ellipse([cx-r*0.05, cy-r*0.55, cx+r*0.65, cy+r*0.35], fill=col)
    d.rectangle([cx-r*0.45, cy+r*0.05, cx+r*0.45, cy+r*0.45], fill=col)
    d.ellipse([cx-r*0.45, cy+r*0.15, cx+r*0.45, cy+r*0.55], fill=col)
    d.line([(cx, cy-r*0.1), (cx, cy+r*0.3)], fill=WHITE, width=int(6*SS))
    d.polygon([(cx-r*0.2, cy+r*0.05), (cx+r*0.2, cy+r*0.05), (cx, cy-r*0.2)], fill=WHITE)

def card_frame(d, col):
    m = 18
    d.rounded_rectangle([m, m, W*SS-m, H*SS-m], radius=40*SS, outline=col, width=3*SS)

# ================================================================ S1 ТИТУЛ
def slide1():
    img, d = new(BLACK)
    d.rectangle([0, 0, W*SS, 22*SS], fill=MAGENTA)
    for x in range(60, W, 70):
        for y in range(120, 260, 70):
            d.ellipse([x, y, x+8*SS, y+8*SS], fill=(40,40,40))
    txt(d, (90, 340), "EWA", font("black", 230), MAGENTA, anchor="la")
    txt(d, (94, 600), "как установить\nи пользоваться", font("black", 78), WHITE, anchor="la", lsp=8)
    d.rectangle([94*SS, 845*SS, 260*SS, 851*SS], fill=PINK)
    txt(d, (90, 880), "инструкция для покупателя", font("semi", 38), PINK, anchor="la")
    txt(d, (90, 940), "5 шагов · 1 минута", font("semi", 32), GREY, anchor="la")
    txt(d, (90, 1180), "работает на iPhone и Android", font("semi", 34), WHITE, anchor="la")
    save(img, "01_титул")

# ================================================================ S2 УСТАНОВКА
def slide2():
    img, d = new(PINK)
    card_frame(d, MAGENTA)
    d.rounded_rectangle([60, 60, 260, 120], radius=30*SS, fill=BLACK)
    txt(d, (155, 90), "ШАГ 1", font("black", 36), WHITE, anchor="mm")
    txt(d, (60, 165), "Установка иконки\nна телефон", font("black", 64), BLACK, anchor="la", lsp=6)

    iy = 360
    d.rounded_rectangle([60, iy, W-60, iy+400], radius=36*SS, fill=WHITE)
    icon_phone(d, 150, iy+70, 50, MAGENTA)
    txt(d, (230, iy+45), "iPhone (Safari)", font("black", 40), BLACK, anchor="la")
    steps_ip = [
        ("1", "Открой сайт в Safari", "адрес сайта"),
        ("2", "Нажми «Поделиться»", "квадрат со стрелкой ↑"),
        ("3", "«На экран Домой»", "появится иконка EWA"),
    ]
    sy = iy + 150
    for num, t1, t2 in steps_ip:
        d.ellipse([90, sy, 90+54, sy+54], fill=MAGENTA)
        txt(d, (117, sy+27), num, font("black", 30), WHITE, anchor="mm")
        txt(d, (175, sy+2), t1, font("black", 34), BLACK, anchor="la")
        txt(d, (175, sy+44), t2, font("semi", 27), GREY, anchor="la")
        sy += 78

    ay = iy + 430
    d.rounded_rectangle([60, ay, W-60, ay+360], radius=36*SS, fill=WHITE)
    icon_phone(d, 150, ay+70, 50, BLACK)
    txt(d, (230, ay+45), "Android (Chrome)", font("black", 40), BLACK, anchor="la")
    steps_ad = [
        ("1", "Открой сайт в Chrome"),
        ("2", "Меню ⋮ справа сверху"),
        ("3", "«На главный экран»"),
    ]
    sy = ay + 150
    for num, t1 in steps_ad:
        d.ellipse([90, sy, 90+54, sy+54], fill=BLACK)
        txt(d, (117, sy+27), num, font("black", 30), WHITE, anchor="mm")
        txt(d, (175, sy+12), t1, font("black", 34), BLACK, anchor="la")
        sy += 78
    save(img, "02_установка")

# ================================================================ S3 ОФЛАЙН
def slide3():
    img, d = new(BLACK)
    card_frame(d, MAGENTA)
    d.rounded_rectangle([60, 60, 260, 120], radius=30*SS, fill=GREEN)
    txt(d, (155, 90), "✓ ОФЛАЙН", font("black", 34), WHITE, anchor="mm")
    txt(d, (60, 165), "Работает БЕЗ\nинтернета", font("black", 68), WHITE, anchor="la", lsp=6)
    txt(d, (60, 330), "всё, что внутри приложения — всегда под рукой", font("semi", 30), PINK, anchor="la")

    items = [
        "создание и редактирование слайдов",
        "тексты, шрифты, стикеры",
        "фоторамки и фоны",
        "свои фото из галереи",
        "сохранение картинок PNG",
        "открытие иконки с экрана",
    ]
    sy = 440
    for t in items:
        icon_check(d, 120, sy+22, 26, GREEN)
        txt(d, (185, sy+6), t, font("semi", 38), WHITE, anchor="la")
        sy += 120
    txt(d, (60, 1200), "После первого открытия приложение\nкэшируется — интернет больше не нужен.", font("semi", 30), GREY, anchor="la", lsp=4)
    save(img, "03_офлайн")

# ================================================================ S4 ОНЛАЙН
def slide4():
    img, d = new(PINK)
    card_frame(d, MAGENTA)
    d.rounded_rectangle([60, 60, 260, 120], radius=30*SS, fill=MAGENTA)
    txt(d, (155, 90), "ОНЛАЙН", font("black", 34), WHITE, anchor="mm")
    txt(d, (60, 165), "Нужен интернет", font("black", 68), BLACK, anchor="la")
    txt(d, (60, 270), "только для двух операций:", font("semi", 32), (90,90,90), anchor="la")

    cy = 380
    d.rounded_rectangle([60, cy, W-60, cy+340], radius=36*SS, fill=WHITE)
    icon_cloud(d, 165, cy+100, 55, MAGENTA)
    txt(d, (270, cy+40), "Видео MP4", font("black", 42), BLACK, anchor="la")
    txt(d, (270, cy+98), "MP4 собирается на сервере", font("semi", 30), GREY, anchor="la")
    txt(d, (270, cy+138), "→ нужен интернет", font("semi", 28), MAGENTA, anchor="la")
    txt(d, (100, cy+210), "· GIF-экспорт видеослайда — тоже через сервер", font("semi", 27), GREY, anchor="la")
    txt(d, (100, cy+252), "· без интернета видео не сохранится", font("semi", 27), GREY, anchor="la")

    cy2 = cy + 380
    d.rounded_rectangle([60, cy2, W-60, cy2+300], radius=36*SS, fill=WHITE)
    icon_check(d, 165, cy2+80, 40, GREEN)
    txt(d, (270, cy2+30), "Первый видео-экспорт", font("black", 42), BLACK, anchor="la")
    txt(d, (270, cy2+88), "один раз грузит инструмент (~25 МБ)", font("semi", 30), GREY, anchor="la")
    txt(d, (270, cy2+128), "→ потом кэшируется, далее офлайн", font("semi", 28), GREEN, anchor="la")
    txt(d, (100, cy2+200), "· картинки PNG — всегда офлайн", font("semi", 27), GREY, anchor="la")
    txt(d, (100, cy2+242), "· всё остальное — офлайн", font("semi", 27), GREY, anchor="la")
    save(img, "04_онлайн")

# ================================================================ S5 ФОРМАТЫ
def slide5():
    img, d = new(PINK)
    card_frame(d, MAGENTA)
    d.rounded_rectangle([60, 60, 330, 120], radius=30*SS, fill=BLACK)
    txt(d, (195, 90), "ФОРМАТЫ", font("black", 34), WHITE, anchor="mm")
    txt(d, (60, 165), "Какой файл\nскачать", font("black", 68), BLACK, anchor="la", lsp=6)
    txt(d, (60, 320), "две кнопки экспорта — под разные задачи", font("semi", 30), (90,90,90), anchor="la")

    # MP4 карточка
    cy = 410
    d.rounded_rectangle([60, cy, W-60, cy+360], radius=36*SS, fill=WHITE)
    d.rounded_rectangle([100, cy+50, 220, cy+170], radius=24*SS, fill=MAGENTA)
    txt(d, (160, cy+110), "MP4", font("black", 52), WHITE, anchor="mm")
    txt(d, (260, cy+45), "видео со звуком", font("black", 42), BLACK, anchor="la")
    txt(d, (260, cy+103), "готово сразу — можно публиковать", font("semi", 29), GREY, anchor="la")
    txt(d, (260, cy+143), "→ Инстаграм · Эдитс", font("semi", 28), MAGENTA, anchor="la")
    txt(d, (100, cy+220), "для постов, сторис, рилс — туда напрямую,", font("semi", 29), (90,90,90), anchor="la")
    txt(d, (100, cy+262), "без лишней обработки", font("semi", 29), (90,90,90), anchor="la")

    # GIF карточка
    cy2 = cy + 400
    d.rounded_rectangle([60, cy2, W-60, cy2+360], radius=36*SS, fill=WHITE)
    d.rounded_rectangle([100, cy2+50, 220, cy2+170], radius=24*SS, fill=BLACK)
    txt(d, (160, cy2+110), "GIF", font("black", 52), WHITE, anchor="mm")
    txt(d, (260, cy2+45), "без звука", font("black", 42), BLACK, anchor="la")
    txt(d, (260, cy2+103), "заготовка для монтажа", font("semi", 29), GREY, anchor="la")
    txt(d, (260, cy2+143), "→ CapCut", font("semi", 28), MAGENTA, anchor="la")
    txt(d, (100, cy2+220), "закидываешь в CapCut и накладываешь", font("semi", 29), (90,90,90), anchor="la")
    txt(d, (100, cy2+262), "свой звук/музыку сверху", font("semi", 29), (90,90,90), anchor="la")
    save(img, "05_форматы")

# ================================================================ S6 ИТОГ
def slide6():
    img, d = new(BLACK)
    card_frame(d, MAGENTA)
    txt(d, (W//2, 240), "ИТОГ", font("black", 40), PINK, anchor="ma")
    txt(d, (W//2, 380), "1 раз с интернетом —", font("black", 70), WHITE, anchor="ma")
    txt(d, (W//2, 480), "работай где угодно", font("black", 70), MAGENTA, anchor="ma")
    blocks = [
        ("1", "Открой сайт\nи установи иконку", MAGENTA),
        ("2", "Дай интернет 1 раз\nна первое видео", PINK),
        ("3", "Дальше — работай\nофлайн где угодно", GREEN),
    ]
    by = 660
    bw = (W - 60*2 - 40*2) // 3
    for i, (n, t, col) in enumerate(blocks):
        bx = 60 + i*(bw+40)
        d.rounded_rectangle([bx, by, bx+bw, by+420], radius=30*SS, outline=col, width=4*SS)
        d.ellipse([bx+bw//2-45, by+60, bx+bw//2+45, by+150], fill=col)
        txt(d, (bx+bw//2, by+105), n, font("black", 50), BLACK if col!=BLACK else WHITE, anchor="mm")
        txt(d, (bx+bw//2, by+260), t, font("semi", 32), WHITE, anchor="ma", lsp=6)
    txt(d, (W//2, 1180), "вопросы — пиши в поддержку", font("semi", 34), PINK, anchor="ma")
    save(img, "06_итог")

if __name__ == "__main__":
    slide1(); slide2(); slide3(); slide4(); slide5(); slide6()
    print("готово:", OUT)

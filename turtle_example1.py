"""
🎨 Uşaqlar üçün Python Turtle - Əyləncəli Rəsm Dünyası!
Advanced səviyyəli Turtle nümunəsi:
  - Rəngli spiral çiçəklər
  - Göy qurşağı spiral
  - Parıldayan ulduz
  - Rəngli fraktal ağac
  - İnteraktiv klik ilə rəsm
"""

import turtle
import math
import random

# ── Ekran quraşdırması ────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.title("🎨 Uşaqlar üçün Turtle Sehrli Dünya!")
screen.bgcolor("#0d0d2b")          # gecə göyü fonu
screen.setup(width=900, height=700)
screen.tracer(0)                   # animasiyanı sürətləndiririk

# ── Kömək funksiyaları ────────────────────────────────────────────────────────
def new_pen(x=0, y=0, speed=0, hide=True):
    """Hazır qurğularla yeni qələm qaytarır."""
    t = turtle.Turtle()
    t.speed(speed)
    t.penup()
    t.goto(x, y)
    t.pendown()
    if hide:
        t.hideturtle()
    return t


# ══════════════════════════════════════════════════════════════════════════════
# 1. GÖY QURŞAĞI SPİRALI
# ══════════════════════════════════════════════════════════════════════════════
def draw_rainbow_spiral(cx, cy, max_size=120):
    colors = ["#FF4C4C","#FF9F45","#FFE04A","#6BFF6B","#4CA9FF","#8B5CF6","#FF6BDA"]
    t = new_pen(cx, cy)
    t.setheading(0)
    length = 4
    for i in range(130):
        t.pencolor(colors[i % len(colors)])
        t.pensize(2)
        t.forward(length)
        t.left(31)
        length += 1.5
        if length > max_size:
            break
    t.penup()


# ══════════════════════════════════════════════════════════════════════════════
# 2. SPIRAL ÇİÇƏK
# ══════════════════════════════════════════════════════════════════════════════
def draw_flower(cx, cy, petals=12, petal_len=90, color1="#FF6BDA", color2="#FFE04A"):
    t = new_pen(cx, cy)
    for i in range(petals):
        # hər ləçəyin rəngi azca fərqli — 0-255 arasında clamp edilir
        r = max(0, min(255, int(255 * (0.5 + 0.5 * math.sin(i * 0.6)))))
        g = max(0, min(255, int(100 * (0.4 + 0.6 * math.cos(i * 0.5)))))
        b = max(0, min(255, int(200 * (0.6 + 0.4 * math.sin(i * 0.4)))))
        t.pencolor(r, g, b)
        t.pensize(2)
        # yarım dairə şəklində ləçək
        for _ in range(60):
            t.forward(petal_len / 60)
            t.left(3)
        t.left(180 - 3 * 60)
        for _ in range(60):
            t.forward(petal_len / 60)
            t.left(3)
        t.left(180 + 360 / petals)
    # mərkəz
    t.penup(); t.goto(cx, cy - 10)
    t.pendown()
    t.pencolor("#FFE04A"); t.fillcolor("#FFE04A")
    t.begin_fill()
    t.circle(10)
    t.end_fill()


# ══════════════════════════════════════════════════════════════════════════════
# 3. PARILDAYAn ULDUZ (doldurulmuş, dərin rəngli)
# ══════════════════════════════════════════════════════════════════════════════
def draw_star(cx, cy, points=8, outer=70, inner=28, color="#FFD700", outline="#FF9F45"):
    t = new_pen(cx, cy)
    angle = 360 / points
    coords = []
    for i in range(points * 2):
        r = outer if i % 2 == 0 else inner
        a = math.radians(i * angle / 2 - 90)
        coords.append((cx + r * math.cos(a), cy + r * math.sin(a)))

    t.pencolor(outline)
    t.fillcolor(color)
    t.pensize(2)
    t.penup(); t.goto(coords[0]); t.pendown()
    t.begin_fill()
    for x, y in coords[1:]:
        t.goto(x, y)
    t.goto(coords[0])
    t.end_fill()


# ══════════════════════════════════════════════════════════════════════════════
# 4. FRAKTAL AĞAC (rekursiv)
# ══════════════════════════════════════════════════════════════════════════════
def draw_tree(t, length, angle, depth, color_shift=0):
    if depth == 0 or length < 4:
        # yarpaq
        t.pencolor("#6BFF6B")
        t.pensize(1)
        t.forward(6)
        t.backward(6)
        return
    # budağın rəngi dərinliyə görə dəyişir
    g = max(50, 200 - depth * 18)
    r = min(255, 80 + depth * 10)
    t.pencolor(r, g, 40)
    t.pensize(max(1, depth * 0.8))
    t.forward(length)

    # sol budaq
    t.left(angle + random.randint(-5, 5))
    draw_tree(t, length * 0.72, angle, depth - 1)
    t.right(angle * 2 + random.randint(-5, 5))
    # sağ budaq
    draw_tree(t, length * 0.68, angle, depth - 1)
    t.left(angle + random.randint(-3, 3))

    t.backward(length)


def draw_fractal_tree(cx, cy, length=95, angle=25, depth=9):
    t = new_pen(cx, cy)
    t.setheading(90)               # yuxarıya bax
    t.pencolor("#8B5A2B")
    t.pensize(depth)
    draw_tree(t, length, angle, depth)


# ══════════════════════════════════════════════════════════════════════════════
# 5. İNTERAKTİV KLIK — hər kliklə kiçik spiral çiçək əmələ gəlir
# ══════════════════════════════════════════════════════════════════════════════
_click_colors = ["#FF4C4C","#FF9F45","#FFE04A","#6BFF6B","#4CA9FF","#8B5CF6","#FF6BDA","#FFFFFF"]
_click_idx = [0]

def on_click(x, y):
    c = _click_colors[_click_idx[0] % len(_click_colors)]
    t = new_pen(x, y)
    t.pencolor(c)
    for i in range(36):
        t.pensize(max(1, 3 - i // 15))
        t.forward(i * 2.5)
        t.right(137.5)          # altın açı – gözəl spiral
    screen.update()
    _click_idx[0] += 1

screen.onclick(on_click)


# ══════════════════════════════════════════════════════════════════════════════
# 6. BAŞLIQ MƏTNİ
# ══════════════════════════════════════════════════════════════════════════════
def draw_title():
    t = new_pen(0, 300)
    t.pencolor("#FFFFFF")
    t.write("🎨  Sehrli Turtle Dünyası  ✨",
            align="center",
            font=("Arial", 18, "bold"))
    t2 = new_pen(0, -320)
    t2.pencolor("#aaaaaa")
    t2.write("💡  Ekrana klik et — sehrli spiral əmələ gəlir!",
             align="center",
             font=("Arial", 11, "normal"))


# ══════════════════════════════════════════════════════════════════════════════
# ANA RƏSM
# ══════════════════════════════════════════════════════════════════════════════
turtle.colormode(255)   # RGB rəng rejimi

print("🎨 Çəkilir... bir az gözlə!")

draw_title()

# sol üst: göy qurşağı spiral
draw_rainbow_spiral(-310, 180)

# sağ üst: parıldayan ulduz
draw_star(280, 210, points=8, outer=75, inner=30, color="#FFD700", outline="#FF9F45")

# mərkəz aşağı: fraktal ağac
draw_fractal_tree(0, -320, length=95, angle=26, depth=9)

# sol alt: çiçək
draw_flower(-290, -180, petals=10, petal_len=80)

# sağ alt: kiçik spiral
draw_rainbow_spiral(300, -180, max_size=80)

# mərkəz: böyük çiçək
draw_flower(0, 60, petals=14, petal_len=100)

screen.update()
print("✅ Hazır! Ekrana klik edərək yeni sehrli spirallar yarat!")

turtle.done()

import Tkinter

top = Tkinter.Tk()

top.wm_title("Christmas Tree :)")
top.wm_minsize(500, 500)

background = Tkinter.Canvas(top, height=500, width=500, bg="firebrick")

# All for floor:
floor = background.create_rectangle(0, 400, 505, 510, fill="chocolate")

y = 420
while y < 510:
    floor_line1 = background.create_line(0, y, 505, y, fill="#000000")
    y += 20

x = 30
y1 = 400
y2 = 420
for y in range(15):
    if x == 530:
        x = 30
        y1 += 40
        y2 += 40
    floor_line2 = background.create_line(x, y1, x, y2, fill="#000000")
    x += 100

x = 80
y1 = 420
y2 = 440
for y in range(100):
    if x == 580:
        x = 80
        y1 += 40
        y2 += 40
    floor_line3 = background.create_line(x, y1, x, y2, fill="#000000")
    x += 100

# All for bricks:
y = 10
while y <= 371:
    brick_line1 = background.create_line(0, y, 505, y, fill="navajo white", width=5)
    y += 30

x = 10
y1 = -20
y2 = 10
for y in range(63):
    if x == 550:
        x = 10
        y1 += 60
        y2 += 60
    brick_line2 = background.create_line(x, y1, x, y2, fill="navajo white", width=5)
    x += 60

x = 40
y1 = 10
y2 = 40
for y in range(56):
    if x == 520:
        x = 40
        y1 += 60
        y2 += 60
    brick_line3 = background.create_line(x, y1, x, y2, fill="navajo white", width=5)
    x += 60

# All for fireplace:
fireplace_tube = background.create_rectangle(380, 0, 450, 400, fill="gray26")
fireplace_compartment = background.create_rectangle(330, 330, 500, 450, fill="gray26")
fireplace_opening = background.create_rectangle(350, 350, 480, 430, fill="LightSteelBlue2")
x1 = 380
x2 = 400
y1 = 380
y2 = 400
for x in range(24):
    wood1circle = background.create_oval(x1, y1, x2, y2, fill="sienna4")
    x1 -= 1
    x2 -= 1
    y1 += 1
    y2 += 1
wood1inner_circle = background.create_oval(x1, y1, x2, y2, fill="burlywood3")
x1 = 430
x2 = 450
y1 = 380
y2 = 400
for x in range(24):
    wood2circle = background.create_oval(x1, y1, x2, y2, fill="sienna4")
    x1 += 1
    x2 += 1
    y1 += 1
    y2 += 1
wood2inner_circle = background.create_oval(x1, y1, x2, y2, fill="burlywood3")
x1 = 400
x2 = 420
y1 = 380
y2 = 400
for x in range(14):
    wood3circle = background.create_oval(x1, y1, x2, y2, fill="sienna4")
    x1 -= 1
    x2 -= 1
    y1 += 2
    y2 += 2
wood3inner_circle = background.create_oval(x1, y1, x2, y2, fill="burlywood3")
x1 = 410
x2 = 430
y1 = 380
y2 = 400
for x in range(14):
    wood4circle = background.create_oval(x1, y1, x2, y2, fill="sienna4")
    x1 += 1
    x2 += 1
    y1 += 2
    y2 += 2
wood4inner_circle = background.create_oval(x1, y1, x2, y2, fill="burlywood3")


# All for the tree:
x1 = 150
y1 = 430
x2 = 200
y2 = 460
for x in range(55):
    log_circle = background.create_oval(x1, y1, x2, y2, fill="sienna4")
    y1 -= 3
    y2 -= 3
tree_leaves = background.create_polygon(175, 25, 220, 75, 200, 75, 250, 125, 225, 125, 270, 200, 250, 200, 300, 310,
                                        55, 310, 105, 200, 80, 200, 125, 125, 100, 125, 150, 75, 130, 75,
                                        fill="forest green")
# TODO Ornaments + moving circle animations + spinning star animation

# All for the presents:
present1 = background.create_rectangle(50, 360, 100, 450, fill="yellow")
present1ribbon = background.create_rectangle(70, 355, 80, 450, fill="blue")
present1bow1 = background.create_oval(60, 340, 80, 360, fill="blue")
present1bow2 = background.create_oval(70, 340, 90, 360, fill="blue")
present2 = background.create_rectangle(220, 400, 310, 470, fill="green")
present2ribbon = background.create_rectangle(250, 390, 280, 470, fill="red")
present2bow1 = background.create_oval(235, 370, 265, 400, fill="red")
present2bow2 = background.create_oval(265, 370, 295, 400, fill="red")

background.pack()

top.mainloop()

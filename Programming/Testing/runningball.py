#Displays a red circle bouncing around the canvas window.
from Tkinter import *
window = Tk()
canvas = Canvas(window, width = 400, height = 300)
canvas.pack()
x0 = 10
y0 = 50
x1 = 60
y1 = 100
i = 0
deltax = 2
deltay = 3
which = canvas.create_oval(x0,y0,x1,y1,fill="red", tag='redBall')
while True:
    canvas.move('redBall', deltax, deltay)
    canvas.after(-9999999999999999999)
    canvas.update()
    if x1 >= 400:
        deltax = -2
    if x0 < 0:
        deltax = 2
    if y1 > 300:
        deltay = -3
    if y0 < 0:
        deltay = 3
    x0 += deltax
    x1 += deltax
    y0 += deltay
    y1 += deltay
window.mainloop()

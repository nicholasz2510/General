from Tkinter import *


def reset_points():
    print "Points reset"
    # TODO write code for resetting points


def save_points():
    print "Points saved"
    # TODO write code for saving points to a file

top = Tk()
w = top.winfo_screenwidth()
h = top.winfo_screenheight()
top.overrideredirect(1)
top.geometry("%dx%d+0+0" % (w, h))


separator = Canvas(top, height=775, width=50)
separator_line = separator.create_rectangle(24, 0, 26, 775)


menu_bar = Menu(top)
options_menu = Menu(menu_bar, tearoff=0)
options_menu.add_command(label="Reset", command=reset_points)
options_menu.add_command(label="Save points in a file", command=save_points)

options_menu.add_separator()

options_menu.add_command(label="Close program", command=top.quit)
menu_bar.add_cascade(label="Options", menu=options_menu)


player_1_name = Label(top, text="Player 1:")
player_1_name.pack(side=LEFT, anchor=NW)
player_1_textbox = Entry(top, width=90)
player_1_textbox.pack(side=LEFT, anchor=NW)

player_2_textbox = Entry(top, width=90)
player_2_textbox.pack(side=RIGHT, anchor=NE)
player_2_name = Label(top, text="Player 2:")
player_2_name.pack(side=RIGHT, anchor=NE)


separator.pack()
top.config(menu=menu_bar)
top.mainloop()

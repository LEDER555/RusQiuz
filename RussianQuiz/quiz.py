from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from time import *

from click import command

def click_button():
    btn["text"] = "Нет"


def show_main_menu():
    global btn
    canvas.delete(ALL)
    canvas.create_image(0, 0, image=back, anchor="nw")
    canvas.create_text(512, 50, text="Добро пожаловать на квиз!", font=("Arial", 20, "bold"), fill="white")
    about_btn = ttk.Button(root, text="О программе", command=about)
    btn = Button(root, text="Начать", command=click_button, font=("Arial", 12))
    canvas.create_window(950, 570, window=about_btn, anchor="se")
    canvas.create_window(512, 340, window=btn)


def about():
    canvas.delete(ALL)
    canvas.create_image(0, 0, image=back, anchor="nw")
    canvas.create_text(512, 50, text="Сделано Трегубовым Александром", font=("Arial", 20, "bold"), fill="white")
    back_btn = ttk.Button(root, text="Назад", command=show_main_menu)
    canvas.create_window(950, 570, window=back_btn, anchor="se")





root = Tk()
root.title("Russian Quiz")
root.geometry("1024x600+430+200")
root.iconbitmap(default="logo.ico")

back_image = Image.open("./back.jpeg")
opened_image = Image.open("./newlogo.png")
logo = ImageTk.PhotoImage(opened_image)
back = ImageTk.PhotoImage(back_image)

background_label = Label(root, image=back)
background_label.place(x=0, y=0, width=1, height=1)


canvas = Canvas(root, width=1024, height=600, highlightthickness=0)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, image=back, anchor="nw")

canvas.create_text(512, 50, text="Добро пожаловать на квиз!", font=("Arial", 20, "bold"), fill="white")


about_btn = ttk.Button(root, text="О программе", command=about)
btn = Button(root, text="Начать", command=click_button, font=("Arial", 12))


canvas.create_window(950, 570, window=about_btn, anchor="se")
canvas.create_window(512, 340, window=btn)


root.resizable(False, False)
root.mainloop()

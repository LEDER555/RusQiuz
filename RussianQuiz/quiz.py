from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 

def about():
    label = Label(text="Создано Трегубовым Александром")

    label.pack()
 
def click_button():
    btn["text"] = "Нет"      
 
root = Tk()
root.title("Russian Quiz")
root.geometry("1024x600+430+200")
root.iconbitmap(default="logo.ico")

back_image = Image.open("./back.jpeg")
opened_image = Image.open("./newlogo.png")
logo = ImageTk.PhotoImage(opened_image)
back = ImageTk.PhotoImage(back_image)


label = ttk.Label(text="Добро пожаловать на квиз!", font=("Arial", 14),image=back, compound="bottom")
label.pack()

about = ttk.Button(text="О программе", command=about)
about.pack(side="bottom", anchor="se")

btn = ttk.Button(text="Начать", command=click_button)
btn.pack(expand=True)

root.resizable(False, False)
root.mainloop()

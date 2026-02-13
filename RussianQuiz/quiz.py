from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random





questions = [
    "Этот народ отмечает праздник «Вороний день» (Вурна хатл), символизирующий приход весны. О ком речь?",
]


answers = [
    "ханты и манси",
    "сабантуй",
    "сурхарбан",
    "осуохай",
    "семык",
    "гербер",
    "святой георгий",
    "масленица",
    "тун-пайрам",
    "хэбденек"
]


hints = [
    "Эти народы проживают в ХМАО и ЯНАО, а ворона у них считается покровительницей матерей и детей.",
    "На этом празднике обязательны соревнования по борьбе на поясах — куреш.",
    "Название праздника буквально означает «стрельба в сур» (кожаную мишень).",
    "Этот танец символизирует жизненный круг и может длиться много часов подряд.",
    "Праздник начинается в среду (через семь недель после Пасхи) и посвящен поминовению предков.",
    "Название праздника — Гербер. В этот день также существовал обряд купания недавно вышедших замуж девушек.",
    "Этот святой считается покровителем мужчин, путников и защитником слабых.",
    "Главное угощение этого праздника символизирует солнце.",
    "Название праздника — Тун-пайрам. Его отмечают в начале лета, когда появляется первый надой.",
    "Название праздника — Хэбденек. Он начинается с обряда очищения через дым можжевельника."
]


facts = [
    "До XVIII века праздник отмечали в разное время, но позже дату закрепили за 7 апреля — Благовещением.",
    "Первое упоминание этого праздника датируется 921 годом в записках багдадского посла Ибн Фадлана.",
    "Раньше этот праздник был военным смотром, на котором отбирали самых метких воинов для ополчения.",
    "Во время Ысыаха принято пить кумыс из ритуальных кубков «чорон» и окроплять землю этим напитком.",
    "Марийцы считаются отличными пчеловодами, поэтому на этом празднике всегда проводят дегустацию меда.",
    "Каша на Гербере олицетворяет будущий урожай, ее варят в огромных котлах на костре.",
    "Во время Джеоргубы на стол ставят три традиционных осетинских пирога и произносят ритуальные молитвы.",
    "После принятия христианства праздник стал предварять Великий пост, а его длительность — одну неделю.",
    "На Тун-пайраме первым айраном окропляют землю и ритуальную березу, чтобы год был плодородным.",
    "Ленточки, которые повязывают на березу, называются «салама». Они доносят просьбы людей до добрых духов."
]

def get_ques():
    return questions[0]


def select_answer(index):
    global selected_answer
    selected_answer = index

    # Очищаем все кружки
    for i in range(4):
        canvas.itemconfig(f"circle_{i}", fill="", outline="white")

    # Закрашиваем выбранный кружок
    canvas.itemconfig(f"circle_{index}", fill="white")

def question():
    global selected_answer
    canvas.delete(ALL)
    canvas.create_image(0, 0, image=back, anchor="nw")
    canvas.create_text(512, 50, text="Вопрос 1:", font=("Arial", 20, "bold"), fill="white")
    canvas.create_text(512, 100, text=get_ques(), font=("Arial", 16), fill="white", width=900)

    selected_answer = -1
    y_position = 200

    for i in range(4):
        # Рисуем кружок и текст
        canvas.create_oval(450, y_position - 10, 470, y_position + 10,
                           outline="white", width=2, tags=f"circle_{i}")
        canvas.create_text(490, y_position, text=answers[i],
                           font=("Arial", 14, "bold"), fill="white",
                           anchor="w", tags=f"answer_{i}")

        # Привязываем клик к выбору ответа
        canvas.tag_bind(f"circle_{i}", "<Button-1>", lambda e, idx=i: select_answer(idx))
        canvas.tag_bind(f"answer_{i}", "<Button-1>", lambda e, idx=i: select_answer(idx))

        y_position += 40

    check_btn = Button(root, text="Проверить", font=("Arial", 12))
    canvas.create_window(512, y_position + 30, window=check_btn)

def click_button():
    question()


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

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

points = 0



quiz_data = [
    {
        "question": "Этот народ отмечает праздник «Вороний день» (Вурна хатл), символизирующий приход весны. О ком речь?",
        "options": ["Ханты и манси", "Татары", "Якуты", "Чукчи"],
        "correct": 0,
        "hint": "Эти народы проживают в ХМАО и ЯНАО, а ворона у них считается покровительницей матерей и детей.",
        "fact": "До XVIII века праздник отмечали в разное время, но позже дату закрепили за 7 апреля — Благовещением."
    },
    {
        "question": "Какой праздник татар и башкир отмечается после окончания весенних полевых работ?",
        "options": ["Гербер", "Сабантуй", "Семык", "Ысыах"],
        "correct": 1,
        "hint": "На этом празднике обязательны соревнования по борьбе на поясах — куреш.",
        "fact": "Первое упоминание этого праздника датируется 921 годом в записках багдадского посла Ибн Фадлана."
    },
    {
        "question": "На каком празднике бурят проводятся «три игры мужей» (борьба, стрельба из лука и скачки)?",
        "options": ["Наадам", "Сурхарбан", "Хэбденек", "Шагаа"],
        "correct": 1,
        "hint": "Название праздника буквально означает «стрельба в сур» (кожаную мишень).",
        "fact": "Раньше этот праздник был военным смотром, на котором отбирали самых метких воинов для ополчения."
    },
    {
        "question": "Как называется массовый круговой хоровод якутов на празднике Ысыах?",
        "options": ["Осуохай", "Луд", "Кочари", "Хоровод"],
        "correct": 0,
        "hint": "Этот танец символизирует жизненный круг и может длиться много часов подряд.",
        "fact": "Во время Ысыаха принято пить кумыс из ритуальных кубков «чорон» и окроплять землю этим напитком."
    },
    {
        "question": "На каком празднике марийская молодежь традиционно «хулиганит» (заколачивает ворота или дымоходы)?",
        "options": ["Джеоргуба", "Семык", "Гербер", "Тун-пайрам"],
        "correct": 1,
        "hint": "Праздник начинается в среду через семь недель после Пасхи и посвящен предкам.",
        "fact": "Марийцы считаются отличными пчеловодами, поэтому на этом празднике всегда проводят дегустацию меда."
    },
    {
        "question": "Какой праздник удмуртов посвящен окончанию полевых работ и обрядовой ячменной каше?",
        "options": ["Сабантуй", "Ысыах", "Гербер", "Семык"],
        "correct": 2,
        "hint": "В этот день также существовал обряд шуточного «купания» недавно вышедших замуж девушек.",
        "fact": "Каша на Гербере олицетворяет будущий урожай, ее варят в огромных котлах на костре прямо на поле."
    },
    {
        "question": "В честь какого святого (Уастырджи) осетины празднуют Джеоргубу целую неделю в ноябре?",
        "options": ["Николай Чудотворец", "Святой Георгий", "Святой Пантелеймон", "Илья Пророк"],
        "correct": 1,
        "hint": "Этот святой считается покровителем мужчин, путников и защитником слабых.",
        "fact": "Во время Джеоргубы на стол обязательно ставят три традиционных осетинских пирога."
    },
    {
        "question": "Какое женское чучело, символизирующее зиму и холод, сжигают славяне на Масленицу?",
        "options": ["Лада", "Морена", "Жива", "Леля"],
        "correct": 1,
        "hint": "Эта богиня в мифологии отвечала за мрак, холод и увядание природы.",
        "fact": "После принятия христианства языческие традиции Масленицы сохранились, но праздник стал предварять Великий пост."
    },
    {
        "question": "Как называется хакасский праздник «первого молока»?",
        "options": ["Тун-пайрам", "Хэбденек", "Сурхарбан", "Луд"],
        "correct": 0,
        "hint": "Его отмечают в начале лета, когда появляется первый надой молока для айрана.",
        "fact": "На Тун-пайраме первым айраном окропляют землю и ритуальную березу, чтобы год был благополучным."
    },
    {
        "question": "На каком празднике эвенки повязывают ленточки «салама» на березу для исполнения желаний?",
        "options": ["Ысыах", "Хэбденек", "Вороний день", "Масленица"],
        "correct": 1,
        "hint": "Это эвенкийский Новый год, который празднуется в день летнего солнцестояния.",
        "fact": "Праздник начинается рано утром с обряда очищения через дым священного можжевельника."
    }
]

current_question = 0
hint_shown = False



def get_ques():
    return quiz_data[current_question]["question"]


def select_answer(index):
    global selected_answer, points
    selected_answer = index

    for i in range(4):
        canvas.itemconfig(f"circle_{i}", fill="", outline="grey")

    canvas.itemconfig(f"circle_{index}", fill="white")


def question():
    global selected_answer, hint_shown
    canvas.delete(ALL)
    canvas.create_image(0, 0, image=back, anchor="nw")
    canvas.create_text(512, 50, text=f"Вопрос {current_question + 1}:", font=("Arial", 20, "bold"), fill="grey26")
    canvas.create_text(512, 100, text=get_ques(), font=("Arial", 16), fill="grey26", width=900)

    selected_answer = -1
    hint_shown = False
    y_position = 200
    options = quiz_data[current_question]["options"]

    for i in range(len(options)):
        canvas.create_rectangle(420, y_position - 15, 900, y_position + 15,
                                outline="", fill="", tags=f"clickarea_{i}")

        canvas.create_oval(450, y_position - 10, 470, y_position + 10, outline="grey", width=2, fill="", tags=f"circle_{i}")

        canvas.create_text(490, y_position, text=options[i], font=("Arial", 14, "bold"), fill="grey26", anchor="w", tags=f"answer_{i}")

        canvas.tag_bind(f"clickarea_{i}", "<Button-1>", lambda e, idx=i: select_answer(idx))
        canvas.tag_bind(f"circle_{i}", "<Button-1>", lambda e, idx=i: select_answer(idx))
        canvas.tag_bind(f"answer_{i}", "<Button-1>", lambda e, idx=i: select_answer(idx))

        canvas.tag_bind(f"clickarea_{i}", "<Enter>", lambda e: canvas.config(cursor="hand2"))
        canvas.tag_bind(f"clickarea_{i}", "<Leave>", lambda e: canvas.config(cursor=""))
        canvas.tag_bind(f"circle_{i}", "<Enter>", lambda e: canvas.config(cursor="hand2"))
        canvas.tag_bind(f"circle_{i}", "<Leave>", lambda e: canvas.config(cursor=""))
        canvas.tag_bind(f"answer_{i}", "<Enter>", lambda e: canvas.config(cursor="hand2"))
        canvas.tag_bind(f"answer_{i}", "<Leave>", lambda e: canvas.config(cursor=""))

        y_position += 40

    hint_btn = Button(root, text="Подсказка", font=("Arial", 12), command=show_hint)
    canvas.create_window(412, y_position + 30, window=hint_btn, tags="hint_button")

    check_btn = Button(root, text="Проверить", font=("Arial", 12), command=check_answer)
    canvas.create_window(612, y_position + 30, window=check_btn, tags="check_button")
    back_btn = ttk.Button(root, text="В главное меню", command=show_main_menu)
    canvas.create_window(950, 570, window=back_btn, anchor="se")


def show_hint():
    global hint_shown, points
    if not hint_shown:
        hint_text = quiz_data[current_question]["hint"]
        canvas.create_text(512, 430, text=f"Подсказка: {hint_text}", font=("Arial", 13), fill="DarkOrange4", width=900, tags="hint")
        hint_shown = True
        points -= 0.5


def check_answer():
    global current_question, points

    if selected_answer == -1:
        canvas.delete("result")
        canvas.create_text(512, 500, text="Выберите ответ!", font=("Arial", 16, "bold"), fill="white", tags="result")
        return

    canvas.delete("check_button")
    canvas.delete("hint_button")
    canvas.delete("hint")

    correct_index = quiz_data[current_question]["correct"]

    if selected_answer == correct_index:
        canvas.create_text(512, 400, text="Правильно! ", font=("Arial", 16, "bold"), fill="green4", tags="result")
        fact_text = quiz_data[current_question]["fact"]
        canvas.create_text(512, 430, text=f"Факт: {fact_text}", font=("Arial", 13), fill="grey0", width=900, tags="result")
        points += 1
    else:
        correct_answer = quiz_data[current_question]["options"][correct_index]
        canvas.create_text(512, 400, text=f"Неправильно! Правильный ответ: {correct_answer}", font=("Arial", 14, "bold"), fill="#A60707", width=900, tags="result")
        points -= 1

    if current_question < len(quiz_data) - 1:
        next_btn = Button(root, text="Следующий вопрос", font=("Arial", 12), command=next_question)
        canvas.create_window(512, 530, window=next_btn)
    else:
        canvas.create_text(512, 510, text=f"Вы набрали: {points} из 10", font=("Arial", 16, "bold"), fill="grey26", tags="result")
        finish_btn = Button(root, text="Завершить квиз", font=("Arial", 12), command=show_main_menu)
        canvas.create_window(512, 550, window=finish_btn)


def next_question():
    global current_question, points
    current_question += 1
    question()

def click_button():
    global current_question, points
    current_question = 0
    question()

def rules():
    canvas.delete(ALL)
    canvas.create_image(0, 0, image=back, anchor="nw")
    canvas.create_text(512, 300, text="Правила:\n1: За один правильный ответ начисляется 1 балл\n2: За один неправильный ответ списывается 1 балл\n3: За использование подсказки списывается полбалла\n", font=("Arial", 20, "bold"), fill="grey26")
    canvas.create_text(380, 400, text="Сделано для фестиваля «Компьютерная страна»\nhttps://samlit.net/samlit/ks/", font=("Arial", 15, "bold"), fill="grey26")
    back_btn = ttk.Button(root, text="Назад", command=show_main_menu)
    canvas.create_window(950, 570, window=back_btn, anchor="se")

def about():
    canvas.delete(ALL)
    canvas.create_image(0, 0, image=back, anchor="nw")
    canvas.create_text(512, 300, text="Сделано Трегубовым Александром из\nШколы № 149 имени Героя Российской Федерации А.И.Баранова", font=("Arial", 20, "bold"), fill="grey26")
    back_btn = ttk.Button(root, text="Назад", command=show_main_menu)
    canvas.create_window(950, 570, window=back_btn, anchor="se")



def show_main_menu():
    global btn, points
    canvas.delete(ALL)
    canvas.create_image(0, 0, image=back, anchor="nw")
    canvas.create_text(512, 200, text="Добро пожаловать на квиз!", font=("Arial", 20, "bold"), fill="grey26")
    about_btn = ttk.Button(root, text="О программе", command=about)
    rules_btn = ttk.Button(root, text="Правила", command=rules)
    btn = Button(root, text="Начать", command=click_button, font=("Arial", 12))
    canvas.create_window(950, 570, window=about_btn, anchor="se")
    canvas.create_window(74, 570, window=rules_btn, anchor="sw")
    canvas.create_window(512, 340, window=btn)
    points = 0


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

canvas.create_text(512, 200, text="Добро пожаловать на квиз!", font=("Arial", 20, "bold"), fill="grey26")


about_btn = ttk.Button(root, text="О программе", command=about)
rules_btn = ttk.Button(root, text="Правила", command=rules)
btn = Button(root, text="Начать", command=click_button, font=("Arial", 12))


canvas.create_window(950, 570, window=about_btn, anchor="se")
canvas.create_window(74, 570, window=rules_btn, anchor="sw")
canvas.create_window(512, 340, window=btn)


root.resizable(False, False)
root.mainloop()

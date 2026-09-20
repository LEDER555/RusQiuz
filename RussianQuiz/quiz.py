#https://github.com/LEDER555/RusQiuz/
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

points = 10



quiz_data = [
    {
        "question": "Представители какого народа отмечают «Вороний день» (Вурна хатл), символизирующий приход весны?",
        "options": ["Ханты и манси", "Татары", "Якуты", "Чукчи"],
        "correct": 0,
        "hint": "Этот народ проживает в ХМАО и ЯНАО.",
        "hint_2": "Ворона у них считается покровительницей матерей и детей.",
        "fact": "Традиционно эти северные народы жили в чумах и берестяных юртах. Ворона для них — символ обновления жизни, пробуждающий природу своим криком."
    },
    {
        "question": "Какой народ ежегодно празднует Сабантуй («праздник плуга») после завершения весенних полевых работ?",
        "options": ["Чуваши", "Марийцы", "Удмурты", "Татары"],
        "correct": 3,
        "hint": "На этом празднике обязательны соревнования по борьбе на поясах — куреш.",
        "hint_2": "Это крупнейший по численности тюркский народ России.",
        "fact": "Культура этого народа знаменита своей кулинарией, например, эчпочмаком и чак-чаком. Сабантуй сегодня празднуется настолько масштабно, что имеет статус государственного праздника."
    },
    {
        "question": "Для какого народа главным праздником является Сурхарбан, где проводятся «три игры мужей»?",
        "options": ["Калмыки", "Буряты", "Тувинцы", "Алтайцы"],
        "correct": 1,
        "hint": "Название праздника буквально означает «стрельба в сур» (кожаную мишень).",
        "hint_2": "Большинство представителей этого народа живут в Восточной Сибири и исповедуют буддизм.",
        "fact": "Этот народ является наследником великой кочевой цивилизации Центральной Азии. Сурхарбан издревле служил военным смотром для отбора самых метких и сильных воинов."
    },
    {
        "question": "Представители какого народа во время своего главного праздника водят массовый круговой хоровод Осуохай?",
        "options": ["Якуты", "Эвенки", "Коряки", "Буряты"],
        "correct": 0,
        "hint": "Этот танец символизирует жизненный круг и может длиться много часов подряд.",
        "hint_2": "Во время праздника они пьют кумыс из ритуальных кубков «чорон».",
        "fact": "Этот народ смог адаптировать разведение скота к экстремальным морозам Якутии. Их праздник Ысыах отмечает начало лета и встречу Нового года в день солнцестояния."
    },
    {
        "question": "Какой народ традиционно отмечает Семык, поминая предков и совершая обряды в священных рощах?",
        "options": ["Мордва", "Марийцы", "Коми", "Карелы"],
        "correct": 1,
        "hint": "В праздничную ночь их молодежь традиционно «хулиганит» (заколачивает ворота).",
        "hint_2": "Этот народ часто называют «последними язычниками Европы».",
        "fact": "Марийцы сохранили древнюю веру и традицию молений в священных рощах. Семык открывает летний праздничный цикл и посвящен укреплению связей между поколениями."
    },
    {
        "question": "У какого народа праздник Гербер посвящен окончанию полевых работ и обрядовой ячменной каше?",
        "options": ["Башкиры", "Ненцы", "Удмурты", "Чуваши"],
        "correct": 2,
        "hint": "В этот день существовал обряд шуточного «купания» молодых жен.",
        "hint_2": "Столицей этого народа является город Ижевск.",
        "fact": "Этот финно-угорский народ славится своими песнями и мастерством ткачества. Обрядовая каша на Гербере варится на костре и символизирует благодарность земле за урожай."
    },
    {
        "question": "Какой народ в ноябре празднует неделю Джеоргуба в честь покровителя мужчин и путников?",
        "options": ["Черкесы", "Осетины", "Ингуши", "Чеченцы"],
        "correct": 1,
        "hint": "На праздничный стол они обязательно ставят три традиционных пирога.",
        "hint_2": "Это единственный ираноязычный народ на Кавказе.",
        "fact": "Этот народ является прямым потомком древних скифов и алан. Три пирога на праздничном столе символизируют единство Бога, Солнца и Земли."
    },
    {
        "question": "Для какого народа праздник Тун-пайрам является «праздником первого молока»?",
        "options": ["Ногайцы", "Калмыки", "Тувинцы", "Хакасы"],
        "correct": 3,
        "hint": "Его отмечают в начале лета, когда появляется первый надой для приготовления айрана.",
        "hint_2": "Они живут в предгорьях Саян и говорят на тюркском языке.",
        "fact": "Хакасы издревле почитают горы и устанавливают священные каменные изваяния. На Тун-пайраме первым свежим айраном окропляют землю, чтобы задобрить духов природы."
    },
    {
        "question": "Какой народ празднует Хэбденек (Новый год) в день летнего солнцестояния?",
        "options": ["Юкагиры", "Чукчи", "Эвенки", "Долганы"],
        "correct": 3,
        "hint": "Они повязывают ленточки «салама» на березу для исполнения желаний.",
        "hint_2": "В прошлом этот народ был известен под названием «тунгусы».",
        "fact": "Этот народ расселен на огромных территориях от Енисея до Охотского моря. Праздник Хэбденек начинается с обряда очищения дымом можжевельника перед встречей солнца."
    },
    {
        "question": "У какого самого многочисленного народа России весенний праздник проводов зимы называется Масленица?",
        "options": ["Мордва", "Карелы", "Коми", "Русские"],
        "correct": 3,
        "hint": "Символом праздника являются блины, олицетворяющие солнце.",
        "hint_2": "В конце праздника они традиционно сжигают соломенное чучело.",
        "fact": "Масленица — это древний славянский праздник, знаменующий победу тепла над холодом. Сжигание чучела символизирует прощание со всем старым и обновление природы."
    }
]

current_question = 0
hint_count = 0

#https://github.com/LEDER555/RusQiuz/

def get_ques():
    return quiz_data[current_question]["question"]


def select_answer(index):
    global selected_answer, points
    selected_answer = index

    for i in range(4):
        canvas.itemconfig(f"circle_{i}", fill="", outline="grey")

    canvas.itemconfig(f"circle_{index}", fill="white")


def question():
    global selected_answer, hint_count
    canvas.delete(ALL)
    canvas.create_image(0, 0, image=back, anchor="nw")
    canvas.create_text(512, 50, text=f"Вопрос {current_question + 1}:", font=("Arial", 20, "bold"), fill="grey26")
    canvas.create_text(512, 100, text=get_ques(), font=("Arial", 16), fill="grey26", width=900)

    selected_answer = -1
    hint_count = 0
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
    global hint_count, points
    if hint_count == 0:
        hint_text = quiz_data[current_question]["hint"]
        canvas.create_text(512, 430, text=f"Подсказка 1: {hint_text}", font=("Arial", 13), fill="DarkOrange4", width=900, tags="hint")
        hint_count = 1
        points -= 2
    elif hint_count == 1:
        hint_text_2 = quiz_data[current_question]["hint_2"]
        canvas.create_text(512, 455, text=f"Подсказка 2: {hint_text_2}", font=("Arial", 13), fill="DarkOrange3", width=900, tags="hint")
        hint_count = 2
        points -= 2


def check_answer():
    global current_question, points

    if selected_answer == -1:
        canvas.delete("result")
        canvas.create_text(512, 500, text="Выберите ответ!", font=("Arial", 16, "bold"), fill="white", tags="result")
        return
    canvas.delete("result")
    canvas.delete("check_button")
    canvas.delete("hint_button")
    canvas.delete("hint")

    correct_index = quiz_data[current_question]["correct"]

    if selected_answer == correct_index:
        canvas.create_text(512, 400, text="Правильно! ", font=("Arial", 16, "bold"), fill="green4", tags="result")
        fact_text = quiz_data[current_question]["fact"]
        canvas.create_text(512, 450, text=f"Факт: {fact_text}", font=("Arial", 13), fill="grey0", width=900, tags="result")
        points += 10
    else:
        correct_answer = quiz_data[current_question]["options"][correct_index]
        canvas.create_text(512, 400, text=f"Неправильно! Правильный ответ: {correct_answer}", font=("Arial", 14, "bold"), fill="#A60707", width=900, tags="result")
        fact_text = quiz_data[current_question]["fact"]
        canvas.create_text(512, 450, text=f"Факт: {fact_text}", font=("Arial", 13), fill="grey0", width=900, tags="result")
        points -= 10

    if current_question < len(quiz_data) - 1:
        next_btn = Button(root, text="Следующий вопрос", font=("Arial", 12), command=next_question)
        canvas.create_window(512, 530, window=next_btn)
    else:
        if points <= 0:
            points = 0
            canvas.create_text(512, 510, text=f"Вы набрали: {points} из 100 баллов", font=("Arial", 16, "bold"), fill="grey26", tags="result")
            finish_btn = Button(root, text="Завершить квиз", font=("Arial", 12), command=show_main_menu)
            canvas.create_window(512, 550, window=finish_btn)
        else:
            canvas.create_text(512, 510, text=f"Вы набрали: {points} из 100 баллов", font=("Arial", 16, "bold"), fill="grey26", tags="result")
            finish_btn = Button(root, text="Завершить квиз", font=("Arial", 12), command=show_main_menu)
            canvas.create_window(512, 550, window=finish_btn)
#https://github.com/LEDER555/RusQiuz/

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
    canvas.create_text(512, 300, text="Правила:\nВам даётся 10 баллов.\n1: За один правильный ответ начисляется 10 баллов\n2: За один неправильный ответ списывается 10 баллов\n3: За каждое использование подсказки списывается 2 балла\n", font=("Arial", 20, "bold"), fill="grey26")
    canvas.create_text(380, 400, text="Сделано для фестиваля «Компьютерная страна»\nhttps://samlit.net/samlit/ks/", font=("Arial", 15, "bold"), fill="grey26")
    back_btn = ttk.Button(root, text="Назад", command=show_main_menu)
    canvas.create_window(950, 570, window=back_btn, anchor="se")

def about():
    canvas.delete(ALL)
    canvas.create_image(0, 0, image=back, anchor="nw")
    canvas.create_text(512, 300, text="Программа сделана Трегубовым Александром Ивановичем,\nучеником 7Г класса,\nШколы № 149 имени Героя Российской Федерации А.И.Баранова,\nг.Самара", font=("Arial", 20, "bold"), fill="grey26")
    back_btn = ttk.Button(root, text="Назад", command=show_main_menu)
    canvas.create_window(950, 570, window=back_btn, anchor="se")

#https://github.com/LEDER555/RusQiuz/

def show_main_menu():
    global btn, points
    canvas.delete(ALL)
    canvas.create_image(0, 0, image=back, anchor="nw")
    canvas.create_text(512, 200, text="Игра - викторина", font=("Arial", 20, "bold"), fill="grey26")
    canvas.create_text(512, 250, text="Угадай, о каком коренном народе России идет речь?", font=("Arial", 20, "bold"), fill="grey26")
    about_btn = ttk.Button(root, text="О программе", command=about)
    rules_btn = ttk.Button(root, text="Правила", command=rules)
    btn = Button(root, text="Начать викторину", command=click_button, font=("Arial", 12))
    canvas.create_window(950, 570, window=about_btn, anchor="se")
    canvas.create_window(74, 570, window=rules_btn, anchor="sw")
    canvas.create_window(512, 340, window=btn)
    points = 0


root = Tk()
root.title("Интерактивная викторина о народах России - Компьютерная страна 2026")
root.geometry("1024x600+430+200")

root.iconbitmap(default=resource_path("logo.ico"))
back_image = Image.open(resource_path("back.jpeg"))
opened_image = Image.open(resource_path("newlogo.png"))
logo = ImageTk.PhotoImage(opened_image)
back = ImageTk.PhotoImage(back_image)
background_label = Label(root, image=back)
background_label.place(x=0, y=0, width=1, height=1)
#https://github.com/LEDER555/RusQiuz/
#https://github.com/LEDER555/RusQiuz/
#https://github.com/LEDER555/RusQiuz/
#https://github.com/LEDER555/RusQiuz/
canvas = Canvas(root, width=1024, height=600, highlightthickness=0)
canvas.pack(fill="both", expand=True)
#https://github.com/LEDER555/RusQiuz/
canvas.create_image(0, 0, image=back, anchor="nw")
canvas.create_text(512, 200, text="Игра - викторина", font=("Arial", 20, "bold"), fill="grey26")
canvas.create_text(512, 250, text="Угадай, о каком коренном народе России идет речь?", font=("Arial", 20, "bold"), fill="grey26")
#https://github.com/LEDER555/RusQiuz/
#https://github.com/LEDER555/RusQiuz/
about_btn = ttk.Button(root, text="О программе", command=about)
rules_btn = ttk.Button(root, text="Правила", command=rules)
btn = Button(root, text="Начать викторину", command=click_button, font=("Arial", 15))
#https://github.com/LEDER555/RusQiuz/
#https://github.com/LEDER555/RusQiuz/
canvas.create_window(950, 570, window=about_btn, anchor="se")
canvas.create_window(74, 570, window=rules_btn, anchor="sw")
canvas.create_window(512, 340, window=btn)


root.resizable(False, False)
root.mainloop()

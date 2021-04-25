#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, 
    QWidget, 
    QVBoxLayout, 
    QHBoxLayout, 
    QGroupBox, 
    QRadioButton,
    QButtonGroup, 
    QPushButton, 
    QLabel)

from random import randint, shuffle

class Question():
    def __init__ (self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Бразилии?', 
'Португальский','Бразильский', 'Английский', 'Испанский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёного', 'Синего', 'Красного', 'Белого'))
questions_list.append(Question('Нацианальные хижины Якутов?', 'Ураса', 'Мамбет', 'Иглу', 'Сарай'))

app = QApplication([])

question_123 = QLabel('Какой национальности не существует?')
button = QPushButton('Ответь')
RadioGroupBox = QGroupBox('Варианты ответов')

answer1 = QRadioButton('Энцы')
answer2 = QRadioButton('Чулымцы')
answer3 = QRadioButton('Смурфы')
answer4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(answer1)
layout2.addWidget(answer3)
layout3.addWidget(answer2)
layout3.addWidget(answer4)

layout1.addLayout(layout2)
layout1.addLayout(layout3)

RadioGroupBox.setLayout(layout1)

AnsGroupBox = QGroupBox('Результат теста')
frue = QLabel('Правильно/Неправильно')
talse = QLabel('Правильный ответ')

layout2_1 = QVBoxLayout()

layout2_1.addWidget(frue, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout2_1.addWidget(talse, alignment=Qt.AlignHCenter)

AnsGroupBox.setLayout(layout2_1)
layout_main1 = QHBoxLayout()
layout_main2 = QHBoxLayout()
layout_main3 = QHBoxLayout()

layout_main1.addWidget(question_123, alignment = (Qt.AlignHCenter | Qt.AlignHCenter))
layout_main2.addWidget(RadioGroupBox)
layout_main2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_main3.addStretch(1)
layout_main3. addWidget(button, stretch = 2)
layout_main3.addStretch(1)

layout_main = QVBoxLayout()
layout_main.addLayout(layout_main1, stretch = 2)
layout_main.addLayout(layout_main2, stretch = 8)
layout_main.addLayout(layout_main3, stretch = 1)

layout_main.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [answer1, answer2, answer3, answer4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question_123.setText(q.question)
    talse.setText(q.right_answer)
    show_question()
    
def show_correct(res):
    frue.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правельный ответ!')
        window.score += 1
        print('Статистика:Всего вопросов - ', window.total, 'Правельных ответов - ', window.score)
        print('Рейтинг:', (window.score / window.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправельно!')
            print('Статистика:Всего вопросов - ', window.total, 'Правельных ответов - ', window.score)
            print('Рейтинг:', (window.score / window.total * 100), '%')

def next_question():
    window.total += 1
    print('Статистика:Всего вопросов - ', window.total, 'Правельных ответов - ', window.score)
    cur_question = randint(0, len (questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_main)
window.setWindowTitle('Memory Card')
button.clicked.connect(click_OK)

window.score = 0
window.total = 0

next_question()
window.resize(400,300)
window.show()
app.exec()
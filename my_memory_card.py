from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])

window = QWidget()
ButtonGroup = QButtonGroup()
window.setWindowTitle('Memory Card')
btn_ok = QPushButton('Ответить')
lb_question = QLabel('Продолжи фразу: "Крутите...."')

question_list = []
question_list.append(Question('Продолжи фразу: "Крутите..."', 'барабан', 'головой', 'от сюда', 'банки, товарищи'))
question_list.append(Question('Что делают когда порезался?', 'обрабатывают', 'зализывают', 'молятся', 'гадают'))
question_list.append(Question('Продолжи фразу: Шла Саша по шоссе и сосала...', 'сушку', 'леденец', 'молоко', 'палец'))
question_list.append(Question('Что надо делать если за вами гонятся?', 'бежать', 'поприветствовать', 'преложить чаю', 'сыграть в нарды'))
question_list.append(Question('Когда вышел фильм ирония судьбы?', '1976', '3000', '1982', '1969'))
question_list.append(Question('Что из этого НЕ парнокопытное?', 'носорог', 'верблюд', 'жираф', 'свинья'))
question_list.append(Question('Сколько всего было создано работ в серии видеоигр "Angry birds"?', '59', '21', '43', '33'))
question_list.append(Question('Какой орган не могут заболеть раком?', 'волосы', 'селезёнка', 'легкие', 'кожа'))
question_list.append(Question('Арбуз это...', 'ягода', 'банан', 'овощ', 'арбуз'))

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('барабан')
rbtn_2 = QRadioButton('головой')
rbtn_3 = QRadioButton('от сюда')
rbtn_4 = QRadioButton('банки, товарищи')

ButtonGroup.addButton(rbtn_1)
ButtonGroup.addButton(rbtn_2)
ButtonGroup.addButton(rbtn_3)
ButtonGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('Прав ты или нет?')
lb_correct = QLabel('Ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.show()
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)

layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)

def question_show():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_ok.setText('Ответить')
    ButtonGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    ButtonGroup.setExclusive(True)

def result_show():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Следующий вопрос")  

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(q.right_answer)
    question_show()

def correct_show(res):
    lb_result.setText(res)
    result_show()

def check_answer():
    if answers[0].isChecked():
        correct_show('Правильно!')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            correct_show('Неверно!')
    

def next_question():
    cur_question = randint(0, len(answers) - 1)
    if cur_question >= len(question_list):
        cur_question = 0
    q = question_list[cur_question]
    ask(q)
    window.total += 1

def start_test():
    if btn_ok.text() == 'Ответить':
        check_answer()
        print('Статистика:')
        print('Всего вопросов:', window.total)
        print('Правильных ответов:', window.score)
        print('Рейтинг:', window.score / window.total * 100, '%')
    else:
        next_question()
        
       

window.setLayout(layout_card)
window.setWindowTitle('Memory card')
btn_ok.clicked.connect(start_test)
window.score = 0
window.total = 0
next_question()
window.resize(400, 200)
window.show()
app.exec_()
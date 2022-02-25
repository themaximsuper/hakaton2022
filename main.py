from time import sleep
import tkinter

#Список команд
commands = [
    (
        {
            "Общие сведения.":"Выберите одно из интересующих вас сведений:",
            "Контакты.":"Выберите один из представленных основных контактов:",
            "Достижения.":"c.", 
            "Создатели бота.":"Для большей информации выберите одну из команд. Бота создали Малинкович Максим и Бобовников Арсений.", 
            "Общая контактная информация.":"Выберите одну из команд:"
         },
    ),

    (
        {
            "Дата основания.":"Лицей№14 был образован в 1992 году.", 
            "Количество учащихся.":"На данный момент в нашем лицее учатся"\
                "около 300 человек.",
            "Количество учителей.":"На даннный момент в лицее преподает" \
                "25 учителей."
        },
    ),

    (
        {
            "Директор Пилипенко Надежда Михайловна.":"Телефон: 8 496 577 00 82.",
            "Заместитель директора Николева Светлана Генадьевна.":"Телефон: 8 496 574 34 84.",
            "Заместитель директора по безопасности Новиков Александр Александрович.":"Телефон: +7 496 574 21 57."
        },
    ),

    (
        {"1.3.1":"ca.", "1.3.2":"cb.", "1.3.3":"cc."},
    ),
            
    (
        {
            "Эл.Почта.":'\n' "Максим: malinkovichmax@gmail.com, \nАрсений: arseniy.bobovnikov@gmail.com.",
            "Номер телефона.":'\n' "Максим: +7 916 454 92 91, \nАрсений: +7 962 913 09 33.",
            "Класс.":'\n'"Максим: 8а. \nАрсений: 8в."
        },
    ),

    (
        
        {
            "Адрес.":"144000, Московская обл., г.Электросталь, проезд Чернышевского, д.22.",
            "Адрес сайта.":"https://estalsch14.edumsko.ru/",
            "Телефон.":"8 496 577 00 82."
        },
    )
]  
#Создаем основное окно.
global win
win = tkinter.Tk()
h = 540
w = 800
global number
number = 0
win.geometry(f"{w}x{h}")
win.title('Бот Валера.')
win.resizable(False, True)

#Создаем вспомогательное окно.
class instruction(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.text1 = tkinter.Text(self, width = 35, height = 15, font = 'Arial', wrap = 'word')
        self.text1.config(yscrollcommand = 'scroll.set', state = 'disabled')
        self.text1.grid(row = 1, column = 1)
        self.button5 = tkinter.Button(self, text="Закрыть", command=self.destroy)
        self.button5.grid(row = 3, column = 2)
        self.scroll1 = tkinter.Scrollbar(self)
        self.scroll1.grid(row = 0, column = 2, rowspan = 3, stick = 'ns')
        
        




#Функция считывания ввода пользователя.
def get_entry():
    global number
    to_send = message.get()
    text.config(state = 'normal')
    if to_send:
        text.insert(1.0, '\n' f'Вы: {to_send}''\n')
        
        #Просчет разветвлений
        if number == 0:
            if to_send == "Общие сведения.":
                text.insert(1.0, "Валера: "+commands[0][0][to_send]+"\n")
                number = 1
                for key in commands[number][0]:
                    text.insert(1.0, key+"\n")
                text.config(state = 'disabled')
            elif to_send == "Контакты.":
                text.insert(1.0, "Валера: "+commands[0][0][to_send]+"\n")
                number = 2
                for key in commands[number][0]:
                    text.insert(1.0, key+"\n")
                text.config(state = 'disabled')
            elif to_send == "Достижения.":
                text.insert(1.0, "Валера: "+commands[0][0][to_send]+"\n")
                number = 3
                for key in commands[number][0]:
                    text.insert(1.0, key+"\n")
                text.config(state = 'disabled')
            elif to_send == "Создатели бота.":
                text.insert(1.0, "Валера: "+commands[0][0][to_send]+"\n")
                number = 4
                for key in commands[number][0]:
                    text.insert(1.0, key+"\n")
                text.config(state = 'disabled')
            elif to_send == "Общая контактная информация.":
                text.insert(1.0, "Валера: "+commands[0][0][to_send]+"\n")
                number = 5
                for key in commands[number][0]:
                    text.insert(1.0, key+"\n")
                text.config(state = 'disabled')
            else:
                text.insert(1.0, 'Валера: Введите правильную команду!\n')
                text.config(state = 'disabled')
        #Проверка правильности ввода.
        else:
            try:
                text.insert(1.0, "Валера: "+commands[number][0][to_send]+"\n")
            except KeyError:
                text.insert(1.0, 'Валера: Введите правильную команду!\n')
        text.config(state = 'disabled')
        message.delete(0, 'end')
    else:
        text.insert(1.0,  f'Валера: Введите команду!''\n')
        text.config(state = 'disabled')
        message.delete(0, 'end')

#Очистка чата.
def delete_everything():
    global number
    number = 0
    button3.config(state = 'normal')
    text.config(state = 'normal')
    text.delete(1.0, 'end')
    text.config(state = 'disabled')
    button1.config(state = 'disabled')

#Начало диалога.
def greeting():
    button3.config(state = 'disabled')
    button1.config(state = 'normal')
    text.config(state = 'normal')
    
    text.insert(1.0, 
                '\n' 'Валера: Приветствую! Я - Валерий, помощник-секретарь МОУ "Лицей №14".'\
                '\n' 'Список команд вы можете найти по кнопке "Иструкция" слева от чата со мной :) \n'\
                '\n' 'Вводите точки обязательно, а то я могу не разобраться!''\n'
                '\n' 'Чтобы начать диалог заново, нажмите "Очистить чат"'
                )
    for key in commands[0][0]:
            text.insert(1.0, key + "\n")
    global number
    number = 0
    text.config(state = 'disabled')

#Функционал кнопки вызова доп. окна.
def instr_button():
    global win
    instr_win = instruction(win)
    instr_win.grab_set()

    
 
#Все надписи, кнопки, поля ввода и текстовые поля.
label1 = tkinter.Label(win, text = 'Сообщение:')
label1.grid(row = 0, column = 0)

message = tkinter.Entry(win)
message.grid(row = 0, column = 1, columnspan = 9, stick = 'we')

button1 = tkinter.Button(win, text = 'Отправить.', command = get_entry, state = 'disabled')
button1.grid(row = 0, column = 10, columnspan = 2, stick = 'we')
                                                                                                                                                                                                        
button2 = tkinter.Button(win, text = 'Очистить чат.', command = delete_everything)
button2.grid(row = 5, column = 1, columnspan = 1, stick = 'we')

button3 = tkinter.Button(win, text = 'Начать диалог.', command = greeting)
button3.grid(row = 5, column = 0, stick = 'we')

button4 = tkinter.Button(win, text = 'Инструкция.', command = instr_button)
button4.grid(row = 1, column = 0, columnspan = 1, stick = 'ns')

text = tkinter.Text(win, width = 55, height = 25, font = 'Arial', wrap = 'word')
text.config(state = 'disabled')
text.grid(row = 1, column = 1)

scroll = tkinter.Scrollbar(win)
scroll.grid(row = 1, column = 3, rowspan = 3,  stick = 'ns')
text.config(yscrollcommand = 'scroll.set')

win.mainloop()

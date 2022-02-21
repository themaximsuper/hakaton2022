from time import sleep
import tkinter

win = tkinter.Tk()
h = 540
w = 700

win.geometry(f"{w}x{h}")
win.title('Бот Валера')
win.resizable(False, True)

def get_entry():
    to_send = message.get()
    text.config(state = 'normal')
    if to_send:
        text.insert(1.0, '\n' f'Вы: {to_send}')
        #if to_send in iteration.call.commands:

        text.config(state = 'disabled')
        message.delete(0, 'end')
    else:
        text.insert(1.0, '\n' f'Валера: Введите команду!')
        text.config(state = 'disabled')
        message.delete(0, 'end')

def delete_everything():
    button3.config(state = 'normal')
    text.config(state = 'normal')
    text.delete(1.0, 'end')
    text.config(state = 'disabled')


def greeting():
    button3.config(state = 'disabled')
    text.config(state = 'normal')
    text.insert(1.0, '\n' 'Валера: Приветствую! Я - Валерий, помощник-секретарь МОУ "Лицйей№14.'\
        '\n' 'Вот список того, что я умею:'\
            '\n' '- Введите ')
    text.tag_add('Color', 1.0, "1.6")
    text.tag_config('Color', foreground = 'green', font = ('Courier', 14, 'bold'))
 

label1 = tkinter.Label(win, text = 'Сообщение')
label1.grid(row = 0, column = 0)

message = tkinter.Entry(win)
message.grid(row = 0, column = 1, columnspan = 9, stick = 'we')

button1 = tkinter.Button(win, text = 'Отправить!', command = get_entry)
button1.grid(row = 0, column = 10, columnspan = 2, stick = 'we')
                                                                                                                                                                                                        
button2 = tkinter.Button(win, text = 'Очистить чат', command = delete_everything)
button2.grid(row = 5, column = 1, columnspan = 1, stick = 'we')

button3 = tkinter.Button(win, text = 'Начать диалог!', command = greeting)
button3.grid(row = 5, column = 0, stick = 'we')

text = tkinter.Text(win, width = 55, height = 25, font = 'Arial', wrap = 'word')
text.config(state = 'disabled')
text.grid(row = 1, column = 1)



scroll = tkinter.Scrollbar(win)
scroll.grid(row = 1, column = 3, rowspan = 3,  stick = 'ns')

text.config(yscrollcommand = scroll.set)
class iteration():

    #То, что было изначально
    def __init__(self):
        pass

        def __call__(self, number):
        
            self.number = number
            self.commands = [
            (
                """blablabla""",
                {"1.1":"a", "1.2":"b", "1.3":"c", "1.4":"d", "1.5":"e"}
            ),

            (
                """bleblebe""",
                {"1.1.1":"aa", "1.1.2":"ab", "1.1.3":"ac"}
            ),

            (
                """blublublu""",
                {"1.2.1":"ba", "1.2.2":"bb", "1.2.3":"bc"}
            ),

            (
                """blyblybly""",
                {"1.3.1":"ca", "1.3.2":"cb", "1.3.3":"cc"}
            ),
            
            (
                """blobloblo""",
                {"1.4.1":"da", "1.4.2":"db", "1.4.3":"dc"}
            ),

            (
                """bliblibli""",
                {"1.5.1":"ea", "1.5.2":"eb", "1.5.3":"ec"}
            )
        ]

            self.obj = self.commands[self.number]
            print(self.obj[0]+ '\n')
            for key in self.obj[1]:
                print(key)
            while True:
                self.answer = input("Введите команду: ")
                try:
                    print(self.obj[1][self.answer])
                except KeyError:
                    print("Ошибка! Введите нужную команду из списка.")
                    continue
                break
            if self.number == 0:
                if self.answer == "1.1":
                    self.output = 1
                elif self.answer == "1.2":
                    self.output = 2
                elif self.answer == "1.3":
                    self.output = 3
                elif self.answer == "1.4":
                    self.output = 4
                elif self.answer == "1.5":
                    self.output = 5
            else:
                self.output = self.answer
            return self.output

main = iteration()
main(main(0))
sleep(180)
win.mainloop()

from time import sleep
import tkinter
from unittest import expectedFailure

commands = [
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

win = tkinter.Tk()
h = 540
w = 800
global number
number = 0
win.geometry(f"{w}x{h}")
win.title('Бот Валера')
win.resizable(False, True)

def get_entry():
    global number
    to_send = message.get()
    text.config(state = 'normal')
    if to_send:
        text.insert(1.0, '\n' f'Вы: {to_send}')
        #if to_send in iteration.call.commands:
        
        if number == 0:
            if to_send == "1.1":
                text.insert(1.0, "Валерий: "+commands[0][1][to_send]+"\n")
                number = 1
                text.insert(1.0, "Валерий: "+commands[number][0]+"\n")
                text.insert(1.0, "Валера: выберите нужную команду:\n")
                for key in commands[number][1]:
                    text.insert(1.0, key+"\n")
            elif to_send == "1.2":
                text.insert(1.0, "Валерий: "+commands[0][1][to_send]+"\n")
                number = 2
                text.insert(1.0, "Валерий: "+commands[number][0]+"\n")
                text.insert(1.0, "Валера: выберите нужную команду:\n")
                for key in commands[number][1]:
                    text.insert(1.0, key+"\n")
            elif to_send == "1.3":
                text.insert(1.0, "Валерий: "+commands[0][1][to_send]+"\n")
                number = 3
                text.insert(1.0, "Валерий: "+commands[number][0]+"\n")
                text.insert(1.0, "Валера: выберите нужную команду:\n")
                for key in commands[number][1]:
                    text.insert(1.0, key+"\n")
            elif to_send == "1.4":
                text.insert(1.0, "Валерий: "+commands[0][1][to_send]+"\n")
                number = 4
                text.insert(1.0, "Валерий: "+commands[number][0]+"\n")
                text.insert(1.0, "Валера: выберите нужную команду:\n")
                for key in commands[number][1]:
                    text.insert(1.0, key+"\n")
            elif to_send == "1.5":
                text.insert(1.0, "Валерий: "+commands[0][1][to_send]+"\n")
                number = 5
                text.insert(1.0, "Валерий: "+commands[number][0]+"\n")
                text.insert(1.0, "Валера: выберите нужную команду:\n")
                for key in commands[number][1]:
                    text.insert(1.0, key+"\n")
            else:
                text.insert(1.0, 'Валера: Введите правльную команду!\n')
        else:
            text.insert(1.0, "Валерий: "+commands[number][1][to_send]+"\n")
            number = 0

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
    
    text.insert(1.0, "Валера: выберите нужную команду:\n")
    for key in commands[0][1]:
            text.insert(1.0, key+"\n")
    text.insert(1.0, '\n' 'Валера: Приветствую! Я - Валерий, помощник-секретарь МОУ "Лицей №14.'\
        '\n' 'Вот список того, что я умею:'\
            '\n' '- Введите ')
    global number
    number = 0
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

#main = iteration()
#print(iteration.commands)
#main = iteration()
#main(main(0))
#sleep(180)
win.mainloop()
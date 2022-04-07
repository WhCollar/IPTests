from tkinter import *
from tkinter.ttk import Combobox
from widgets import *
from generator_of_tasks import *

root = Tk()
root.title("TestGenerate")
root.geometry("500x500")
root.resizable(width=False, height=False)
values = []
for keys, value in type_of_tasks.items():
    text = f'{keys}) {value[0]}'
    values.append(text)

Label(text="Тип задачи:").place(x=8, y=8)
selector = Combobox(root, values=values, width=60, state="readonly")
selector.place(x=75, y=8)

widget_text_result = Text(root, wrap=WORD, width=60, height=45)


def button_generate():
    widget_text_result.delete('1.0', END)
    widget_text_result.insert(index='1.0', chars=generator(selector.current()))


def button_copy_task():
    if not widget_text_result.get("1.0", END) == "\n":
        root.clipboard_clear()
        task_text = widget_text_result.get("1.0", END).split('\n')[0]
        root.clipboard_append(task_text)
        root.update()
        show_message("Текст задачи скопирован")


def button_copy_answer():
    if not widget_text_result.get("1.0", END) == "\n":
        root.clipboard_clear()
        answer_text = widget_text_result.get("1.0", END).split(' ')[-1]
        root.clipboard_append(answer_text)
        root.update()
        show_message("Ответ скопирован")


Button(root, text="Сгенерировать", command=button_generate).place(x=75, y=35)
Button(root, text="Скопировать задачу", command=button_copy_task).place(x=196, y=35)
Button(root, text="Скопировать ответ", command=button_copy_answer).place(x=343, y=35)

widget_text_result.place(x=8, y=70)

root.mainloop()


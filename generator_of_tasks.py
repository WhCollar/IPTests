from tasks.task_1 import task_1
from tasks.task_2 import task_2
from tasks.task_3 import task_3


type_of_tasks = {1: ("Определение количества доступных хостов", task_1),
                 2: ("Определение колсичества подсетей", task_2),
                 3: ("Определение октета адреса хоста в одной из подсетей", task_3)}


def generator(type_of_task):
    if type_of_task == -1:
        return 'Вы не выбрали тип задачи!'
    return type_of_tasks[type_of_task+1][1]()

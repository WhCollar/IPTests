from config import *
from random import randint


def ip_generator(type_of_ip='C'):
    if type_of_ip in network_class.keys():
        ip_list = list()
        if type_of_ip == 'C':
            ip_list.append(randint(network_class['C'][0], network_class['C'][1]))
            ip_list.append(randint(0, 255))
            ip_list.append(randint(0, 255))
            ip_list.append(0)
        return '.'.join(str(el) for el in ip_list)


def host_subnet_num_generator(type_of_ip='C'):
    if type_of_ip == 'C':
        num = randint(24, 31)
        return all_mask[num]["addresses"], all_mask[num]["subnets"]


def task_2():
    ip = ip_generator()
    host_num, subnet_num = host_subnet_num_generator()

    task_text = f'Кокое максимальное количество хостов при разбиении сети {ip} на {int(subnet_num)} подсетей? \n \n' \
                f'Ответ: {host_num}'

    return task_text

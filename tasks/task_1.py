import random
from config import *
from random import randint


def ip_generator():
    type_of_ip = random.choice(list(network_class.keys()))
    ip_list = list()
    if type_of_ip == 'C':
        ip_list.append(randint(network_class['C'][0], network_class['C'][1]))
        ip_list.append(randint(0, 255))
        ip_list.append(randint(0, 255))
        ip_list.append(0)
    elif type_of_ip == 'B':
        ip_list.append(randint(network_class['B'][0], network_class['B'][1]))
        ip_list.append(randint(0, 255))
        ip_list.append(0)
        ip_list.append(0)
    elif type_of_ip == 'A':
        ip_list.append(randint(network_class['A'][0], network_class['A'][1]))
        ip_list.append(0)
        ip_list.append(0)
        ip_list.append(0)
    return '.'.join(str(el) for el in ip_list), type_of_ip


def host_subnet_num_generator(type_of_ip):
    if type_of_ip == 'C':
        num = randint(24, 31)
        return all_mask[num]["addresses"], all_mask[num]["subnets"]
    elif type_of_ip == 'B':
        num = randint(16, 23)
        return all_mask[num]["addresses"], all_mask[num]["subnets"]
    elif type_of_ip == 'A':
        num = randint(9, 15)
        return all_mask[num]["addresses"], all_mask[num]["subnets"]


def task_1():
    ip, type_of_ip = ip_generator()
    host_num, subnet_num = host_subnet_num_generator(type_of_ip)

    task_text = f'На какое максимальное количество подсетей должна быть разбита сеть {ip}, ' \
                f'чтобы в каждой могло быть до {int(host_num)} хостов? \n \n' \
                f'Ответ: {subnet_num}'

    return task_text

import random
from math import log2

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
        return all_mask[num]["addresses"], all_mask[num]["subnets"], all_mask[num]["decimal notation"]
    elif type_of_ip == 'B':
        num = randint(16, 23)
        return all_mask[num]["addresses"], all_mask[num]["subnets"], all_mask[num]["decimal notation"]
    elif type_of_ip == 'A':
        num = randint(9, 15)
        return all_mask[num]["addresses"], all_mask[num]["subnets"], all_mask[num]["decimal notation"]


def binary_notation_str(mask_list):
    result = ''
    for el in mask_list:
        if int(el) != 0:
            result += f".{int(el):b}"
        else:
            result += ".00000000"
    return result[1:]


def solution(decimal_notation, subnet_num, type_of_ip, host_num):
    decimal_notation_list = decimal_notation.split('.')
    num_octet_0 = 1
    for el in decimal_notation_list:
        if int(el) == 0:
            num_octet_0 = num_octet_0 + 1

    result = f"Класс подсети {type_of_ip} следовательно дефолтная маска подсети будет: " \
             f"{binary_notation_str(default_mask[type_of_ip])}\n\n"
    result += f"{int(host_num)} + 2 = {int(host_num) + 2} - максимальное количество хостов в подсети\n\n" \
              f"{int(host_num) + 2} = 2^{int(log2(int(host_num) + 2))} Следовательно:\n" \
              f"{int(log2(int(host_num) + 2))} - количесвто битов занятых для адреса хоста\n" \
              f"{8 * num_octet_0} - количество свободных битов\n" \
              f"{8 * num_octet_0}-{int(log2(int(host_num) + 2))}={8 * num_octet_0 - int(log2(int(host_num) + 2))}" \
              f" - количесвто битов занятых для определения сети\n\n"
    result += f"Заполнив биты отведённые для определения подсети, маска подсети примет иметь вид: " \
              f"{binary_notation_str(decimal_notation_list)}\n" \
              f"2^{int(log2(int(subnet_num)))}={subnet_num} - количесвто подсетей на которое разбита сеть"
    return result


def task_1():
    ip, type_of_ip = ip_generator()
    host_num, subnet_num, decimal_notation = host_subnet_num_generator(type_of_ip)

    task_text = f'На какое максимальное количество подсетей должна быть разбита сеть {ip}, ' \
                f'чтобы в каждой могло быть до {int(host_num)} хостов? \n \n' \
                f'Решение: \n {solution(decimal_notation, subnet_num, type_of_ip, host_num)} \n \n' \
                f'Ответ: {subnet_num}'

    return task_text

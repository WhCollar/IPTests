import math
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
        num = randint(25, 31)
        return all_mask[num]["addresses"], all_mask[num]["subnets"], all_mask[num]["decimal notation"]
    elif type_of_ip == 'B':
        num = randint(17, 23)
        return all_mask[num]["addresses"], all_mask[num]["subnets"], all_mask[num]["decimal notation"]
    elif type_of_ip == 'A':
        num = randint(9, 15)
        return all_mask[num]["addresses"], all_mask[num]["subnets"], all_mask[num]["decimal notation"]


def calculation_last_octet(type_of_ip, subnet_num, subnet, host):
    if type_of_ip == 'C':
        subnet_step = 256 / subnet_num
        subnet_octet = subnet_step * (subnet - 1)
        subnet_host = subnet_octet + host
        return int(subnet_host)
    elif type_of_ip == 'B':
        if host > 256:
            subnet_host = host % 256
            return subnet_host
        else:
            return host
    elif type_of_ip == 'A':
        if host > 256:
            subnet_host = host % 256
            if host > (256 * 256):
                subnet_host = host % 65536
                if subnet_host > 256:
                    return host % 256
                return subnet_host
            return subnet_host
        else:
            return host


def binary_notation_str(mask_list):
    result = ''
    for el in mask_list:
        if int(el) != 0:
            text = f"{int(el):b}"
            if len(text) < 8:
                txt_0 = '0' * (8 - len(text))
                text = txt_0 + text
            result += f'.{text}'
        else:
            result += ".00000000"
    return result[1:]

#
# def under_solution(type_of_ip, host, ip):
#     result = ''
#     res_ip_bin_str = binary_notation_str([ip[0]])
#     res_ip_decimal_list = [ip[0]]
#     if type_of_ip == 'C':
#         pass
#     elif type_of_ip == 'B':
#         pass
#     elif type_of_ip == 'A':
#         if host > 256:
#             if host > 65536:
#                 num = int(host) // int(65536)
#                 host = host % 65536
#                 result += f"Так как номер хоста больше чем 65536(256*256), мы делим нацело номер хоста на 65536 и " \
#                           f"получаем {num}, переводим в двоичный вид ({num:b}) и прибавляем ко второму октету.\n" \
#                           f"Второй октет + Результат деления = Второй октет адреса хоста\n" \
#                           f"{ip[1]:b} + {num:b} = {ip[1] + num:b}\n\n"
#                 res_ip_bin_str += f".{ip[1] + num:b}"
#                 res_ip_decimal_list.append(int(f"{ip[1] + num:b}", 2))
#                 text_bool = 1
#                 if host > 256:
#                     if text_bool == 1:
#                         num = host // 256
#                         num_bin_str = f"{num:b}"
#                         if len(num_bin_str) < 8:
#                             txt_0 = '0' * (8 - len(num_bin_str))
#                             num_bin_str = txt_0 + num_bin_str
#                         result += f"Остаток от целочисленного деления на 65536 равен {host} и всё ещё больше 256, "
#                         host = host % 256
#                         result += f"следовательно, мы делим его нацело на 256, получаем {num} и сотаток {host}." \
#                                   f"Теперь переводим результат целочисленного деления в двоичный вид ({num:b}) и " \
#                                   f"прибавляем к третьему октету.\n" \
#                                   f"Третий октет + Результат деления = Третий октет адреса хоста\n" \
#                                   f"00000000 + {num:b} = {num_bin_str}\n\n"
#                         res_ip_bin_str += f".{num_bin_str}"
#                         res_ip_decimal_list.append(int(num_bin_str, 2))
#                         host_bin_str = f"{host:b}"
#                         if len(host_bin_str) < 8:
#                             txt_0 = '0' * (8 - len(host_bin_str))
#                             host_bin_str = txt_0 + host_bin_str
#                         result += f"Последним шагом будет расчёт четвёртого октета, для этого переведём остаток в " \
#                                   f"двоичный вид ({host:b}) и прибавим к четвёртому откету.\n" \
#                                   f"Четвёртый октет + Результат деления = Третий октет адреса хоста\n" \
#                                   f"00000000 + {host:b} = {host_bin_str}\n\n"
#                         res_ip_bin_str += f".{host_bin_str}"
#                         res_ip_decimal_list.append(int(host_bin_str, 2))
#                         result += f"IP адрес хоста в двоичном виде: \n{res_ip_bin_str}\n" \
#                                   f"IP адрес хоста в десятичном виде: \n{'.'.join(map(str, res_ip_decimal_list))}\n"
#         else:
#             pass
#     return result


def solution(subnet_num, type_of_ip, host, ip, subnet):
    result = ''
    result += f"Класс подсети класса {type_of_ip} следовательно дефолтная маска подсети будет: " \
              f"{binary_notation_str(default_mask[type_of_ip])}\n\n"
    if type_of_ip == "A":
        result += f"Сначала расчитаем адрес подстеи:\n" \
                  f"256/{subnet_num}={int(256/int(subnet_num))} - шаг адреса подсети\n"
        if int(subnet_num) < 4:
            result += f"1: {ip.split('.')[0]}.{0}.0.0\n" \
                      f"2: {ip.split('.')[0]}.{128}.0.0\n"
        else:
            result += f"1: {ip.split('.')[0]}.{0}.0.0\n" \
                      f"2: {ip.split('.')[0]}.{int(256/int(subnet_num))}.0.0\n" \
                      f"n: ...\n" \
                      f"{subnet}: {ip.split('.')[0]}.{int(256/int(subnet_num))*(int(subnet) - 1)}.0.0\n"
        result += f"В двоичном виде адрес подсети будет выглядеть следующим образом: " \
                  f"{binary_notation_str([ip.split('.')[0], int(256/int(subnet_num))*(int(subnet) - 1), '0', '0'])}\n\n" \
                  f"{universal_solution(binary_notation_str([ip.split('.')[0], int(256/int(subnet_num))*(int(subnet) - 1), '0', '0']), host)}"

    elif type_of_ip == "B":
        result += f"Сначала расчитаем адрес подстеи:\n" \
                  f"256/{subnet_num}={int(256 / int(subnet_num))} - шаг адреса подсети\n"
        if int(subnet_num) < 4:
            result += f"1: {ip.split('.')[0]}.{ip.split('.')[1]}.{0}.0\n" \
                      f"2: {ip.split('.')[0]}.{ip.split('.')[1]}.{128}.0\n"
        else:
            result += f"1: {ip.split('.')[0]}.{ip.split('.')[1]}.0.0\n" \
                      f"2: {ip.split('.')[0]}.{ip.split('.')[1]}.{int(256 / int(subnet_num))}.0\n" \
                      f"n: ...\n" \
                      f"{subnet}: {ip.split('.')[0]}.{ip.split('.')[1]}.{int(256 / int(subnet_num)) * (int(subnet) - 1)}.0\n"
        result += f"В двоичном виде адрес подсети будет выглядеть следующим образом: " \
                  f"{binary_notation_str([ip.split('.')[0], ip.split('.')[1], int(256 / int(subnet_num)) * (int(subnet) - 1), '0'])}\n\n" \
                  f"{universal_solution(binary_notation_str([ip.split('.')[0], ip.split('.')[1], int(256 / int(subnet_num)) * (int(subnet) - 1), '0']), host)}"
    elif type_of_ip == "C":
        result += f"Сначала расчитаем адрес подстеи:\n" \
                  f"256/{subnet_num}={int(256 / int(subnet_num))} - шаг адреса подсети\n"
        if int(subnet_num) < 4:
            result += f"1: {ip.split('.')[0]}.{ip.split('.')[1]}.{ip.split('.')[2]}.{0}\n" \
                      f"2: {ip.split('.')[0]}.{ip.split('.')[1]}.{ip.split('.')[2]}.{128}\n"
        else:
            result += f"1: {ip.split('.')[0]}.{ip.split('.')[1]}.{ip.split('.')[2]}.{0}\n" \
                      f"2: {ip.split('.')[0]}.{ip.split('.')[1]}.{ip.split('.')[2]}.{int(256 / int(subnet_num))}\n" \
                      f"n: ...\n" \
                      f"{subnet}: {ip.split('.')[0]}.{ip.split('.')[1]}.{ip.split('.')[2]}.{int(256 / int(subnet_num)) * (int(subnet) - 1)}\n"
        result += f"В двоичном виде адрес подсети будет выглядеть следующим образом: " \
                  f"{binary_notation_str([ip.split('.')[0], ip.split('.')[1], ip.split('.')[2], int(256 / int(subnet_num)) * (int(subnet) - 1)])}\n\n" \
                  f"{universal_solution(binary_notation_str([ip.split('.')[0], ip.split('.')[1], ip.split('.')[2], int(256 / int(subnet_num)) * (int(subnet) - 1)]), host)}"

    return result


def universal_solution(ip_str, host):
    ip_list = list(''.join(ip_str.split('.')))
    res = 'Теперь расчитываем IP.\n'
    while host > 0:
        index = -abs(math.floor(log2(host))) - 1
        ip_list[index] = '1'
        none_1 = host
        none_2 = ''.join(ip_list[:8]) + '.' + ''.join(ip_list[8:16]) + '.' + ''.join(ip_list[16:24]) + '.' + ''.join(ip_list[24:32])
        host = host - pow(2, int(log2(host)))
        res += f'\nБлижайшая степень двойки к {none_1} это {pow(2, int(log2(none_1)))}=2^{int(log2(none_1))}, ' \
               f'следовательно заменяем {int(log2(none_1))} бит ' \
               f'на 1 в двоичном IP подсети, ведя отсчёт с права на лево, начиная с 0.\n' \
               f'Получим: {none_2}\n'
    ip = ''.join(ip_list[:8]) + '.' + ''.join(ip_list[8:16]) + '.' + ''.join(ip_list[16:24]) + '.' + ''.join(ip_list[24:32])
    ip_decimal = str(int(''.join(ip_list[:8]), 2)) + '.' + str(int(''.join(ip_list[8:16]), 2)) + '.' + str(int(''.join(ip_list[16:24]), 2)) + '.' + str(int(''.join(ip_list[24:32]), 2))
    answer = str(int(''.join(ip_list[24:32]), 2))
    res += f'\n{ip}\n' \
           f'{ip_decimal}\n\n' \
           f'Ответ: {answer}'
    return res


def task_3():
    ip, type_of_ip = ip_generator()
    host_num, subnet_num, decimal_notation = host_subnet_num_generator(type_of_ip)
    subnet = randint(1, int(subnet_num))
    host = randint(1, int(host_num))

    return f"Сеть {ip} разбита на {subnet_num} подсети(ей). " \
           f"Каким будет последний октет {host} выданного IP-адреса в " \
           f"{subnet} подсети? \n \n" \
           f"Решение:\n{solution( subnet_num, type_of_ip, host, ip, subnet)}\n" \
           f"Ответ: {calculation_last_octet(type_of_ip, int(subnet_num), subnet, host)}"

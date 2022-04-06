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
        num = randint(25, 30)
        return all_mask[num]["addresses"], all_mask[num]["subnets"], all_mask[num]["decimal notation"]
    elif type_of_ip == 'B':
        num = randint(17, 23)
        return all_mask[num]["addresses"], all_mask[num]["subnets"], all_mask[num]["decimal notation"]
    elif type_of_ip == 'A':
        num = randint(9, 15)
        return all_mask[num]["addresses"], all_mask[num]["subnets"], all_mask[num]["decimal notation"]


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


def mask(bite_num, default_mask):
    binary_mask = binary_notation_str(default_mask)
    binary_mask = binary_mask.split('.')
    binary_mask = f'{binary_mask[0]}{binary_mask[1]}{binary_mask[2]}{binary_mask[3]}'
    binary_mask = list(binary_mask)
    while bite_num > 0:
        for i in range(len(binary_mask)):
            if binary_mask[i] == '0':
                binary_mask[i] = '1'
                bite_num = bite_num - 1
                break
    bite_1_in_musk = 0
    for i in range(len(binary_mask)):
        if binary_mask[i] == '0':
            bite_1_in_musk = bite_1_in_musk + 1
    return ''.join(binary_mask[:8]) + '.' + ''.join(binary_mask[8:16]) + '.' + ''.join(binary_mask[16:24]) + '.' + ''.join(binary_mask[24:32]), bite_1_in_musk


def solution(subnet_num, type_of_ip, host, ip, subnet):
    result = ''
    bite_num = int(log2(int(subnet_num)))
    mask_, bite_1_in_musk = mask(bite_num, default_mask[type_of_ip])
    host_num = pow(2, int(bite_1_in_musk))-2
    result += f"Класс {type_of_ip} следовательно дефолтная маска подсети будет: " \
              f"{binary_notation_str(default_mask[type_of_ip])}\n" \
              f"{subnet_num}=2^{bite_num} n={bite_num}\n" \
              f"Маска: {mask_}\n" \
              f"M=2^m-2 m={bite_1_in_musk}\n" \
              f"M=2^{bite_1_in_musk}-2={pow(2, int(bite_1_in_musk))}-2={host_num}\n\n" \
              f"{universal_solution(binary_notation_str(ip.split('.')), subnet, type_of_ip, host, int(subnet_num), host_num)}\n\n"

    return result


def universal_solution(ip_str, subnet, type_of_ip, host, subnet_num, host_num):
    ip_list = list(''.join(ip_str.split('.')))
    res = ''
    if type_of_ip == 'C':
        last_octet_1 = int((256 / subnet_num * (subnet - 1)) + 1)
        last_octet_2 = int((256 / subnet_num * (subnet - 1)) + host_num)
        subnet_ip_range = f"Диапазон адресов для подсети {int(''.join(ip_list[:8]), 2)}.{int(''.join(ip_list[8:16]), 2)}.{int(''.join(ip_list[16:24]), 2)}.{int((256 / subnet_num * (subnet - 1)))}:\n" \
                          f"{int(''.join(ip_list[:8]), 2)}.{int(''.join(ip_list[8:16]), 2)}.{int(''.join(ip_list[16:24]), 2)}.{last_octet_1} - " \
                          f"{int(''.join(ip_list[:8]), 2)}.{int(''.join(ip_list[8:16]), 2)}.{int(''.join(ip_list[16:24]), 2)}.{last_octet_2}\n\n" \
                          f"Ответ: {int((256 / subnet_num * (subnet - 1)) + host)}"
    else:
        while subnet > 0:
            index = -abs(math.floor(log2(subnet))) - 1
            ip_list[index] = '1'
            subnet = subnet - pow(2, math.floor(log2(subnet)))
        subnet_ip_range = f"Диапазон адресов для подсети {int(''.join(ip_list[:8]), 2)}.{int(''.join(ip_list[8:16]), 2)}.{int(''.join(ip_list[16:24]), 2)}.{int(''.join(ip_list[24:32]), 2)}:\n" \
                          f"{int(''.join(ip_list[:8]), 2)}.{int(''.join(ip_list[8:16]), 2)}.{int(''.join(ip_list[16:24]), 2)}.{int(''.join(ip_list[24:32]), 2) + 1} - " \
                          f"{int(''.join(ip_list[:8]), 2)}.{int(''.join(ip_list[8:16]), 2)}.{int(''.join(ip_list[16:24]), 2)}.{int(''.join(ip_list[24:32]), 2) + host_num}\n\n" \
                          f"Ответ: {int(''.join(ip_list[24:32]), 2) + host}"
    return subnet_ip_range


def task_3():
    ip, type_of_ip = ip_generator()
    host_num, subnet_num, decimal_notation = host_subnet_num_generator(type_of_ip)
    subnet = 0
    host = 0
    if type_of_ip == 'A':
        subnet_num = pow(2, randint(17, 22))
        subnet = randint(pow(2, 17), pow(2, 22))
        host = randint(1, 3)
    elif type_of_ip == 'B':
        subnet_num = pow(2, randint(9, 14))
        subnet = randint(pow(2, 9), pow(2, 14))
        host = randint(1, 3)
    else:
        subnet = randint(1, int(subnet_num))
        host = randint(1, int(host_num))

    return f"Сеть {ip} разбита на {subnet_num} подсети(ей). " \
           f"Каким будет последний октет {host} выданного IP-адреса в " \
           f"{subnet} подсети? \n \n" \
           f"Решение:\n{solution(subnet_num, type_of_ip, host, ip, subnet)}\n"

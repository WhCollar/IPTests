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
        num = randint(24, 29)
        return all_mask[num]["addresses"], all_mask[num]["subnets"]


def calculation_last_octet(subnet_num, subnet, host):
    subnet_step = 256 / subnet_num
    subnet_octet = subnet_step * (subnet-1)
    subnet_host = subnet_octet + host
    return int(subnet_host)


def task_3():
    ip = ip_generator()
    host_num, subnet_num = host_subnet_num_generator()
    subnet = randint(1, int(subnet_num))
    host = randint(1, int(host_num))
    answer = calculation_last_octet(int(subnet_num), subnet, host)

    task_text = f"Сеть {ip} разбита на {subnet_num} подсети(ей). " \
                f"Каким будет последний октет {host} выданного IP-адреса в " \
                f"{subnet} подсети? \n \n" \
                f"Ответ: {answer}"

    return task_text

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
        num = randint(25, 30)
        return all_mask[num]["addresses"], all_mask[num]["subnets"]
    elif type_of_ip == 'B':
        num = randint(17, 23)
        return all_mask[num]["addresses"], all_mask[num]["subnets"]
    elif type_of_ip == 'A':
        num = randint(9, 15)
        return all_mask[num]["addresses"], all_mask[num]["subnets"]


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


def task_3():
    ip, type_of_ip = ip_generator()
    host_num, subnet_num = host_subnet_num_generator(type_of_ip)
    subnet = randint(1, int(subnet_num))
    host = randint(1, int(host_num))
    answer = calculation_last_octet(type_of_ip, int(subnet_num), subnet, host)

    return f"Сеть {ip} разбита на {subnet_num} подсети(ей). " \
           f"Каким будет последний октет {host} выданного IP-адреса в " \
           f"{subnet} подсети? \n \n" \
           f"Ответ: {answer}"

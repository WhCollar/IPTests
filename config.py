network_class = {
    'A': (1, 126),
    'B': (128, 191),
    'C': (192, 223)
}

default_mask = {
    'A': (255, 0, 0, 0),
    'B': (255, 255, 0, 0),
    'C': (255, 255, 255, 0)
}

all_mask = {
    9: {"decimal notation": "255.128.0.0", "subnets": '', "addresses": "8388606", "class": "128A"},
    10: {"decimal notation": "255.192.0.0", "subnets": '', "addresses": "4194302", "class": "64A"},
    11: {"decimal notation": "255.224.0.0", "subnets": '', "addresses": "2097150", "class": "32A"},
    12: {"decimal notation": "255.240.0.0", "subnets": '', "addresses": "1048574", "class": "16A"},
    13: {"decimal notation": "255.248.0.0", "subnets": '', "addresses": "524286", "class": "8A"},
    14: {"decimal notation": "255.252.0.0", "subnets": '', "addresses": "262142", "class": "4A"},
    15: {"decimal notation": "255.254.0.0", "subnets": '', "addresses": "131070", "class": "2A"},
    16: {"decimal notation": "255.255.0.0", "subnets": '', "addresses": "65534", "class": "1B"},
    17: {"decimal notation": "255.255.128.0", "subnets": '2', "addresses": "32766", "class": "128B"},
    18: {"decimal notation": "255.255.192.0", "subnets": '4', "addresses": "16382", "class": "64B"},
    19: {"decimal notation": "255.255.224.0", "subnets": '8', "addresses": "8190", "class": "32B"},
    20: {"decimal notation": "255.255.240.0", "subnets": '16', "addresses": "4094", "class": "16B"},
    21: {"decimal notation": "255.255.248.0", "subnets": '32', "addresses": "2046", "class": "8B"},
    22: {"decimal notation": "255.255.252.0", "subnets": '64', "addresses": "1022", "class": "4B"},
    23: {"decimal notation": "255.255.254.0", "subnets": '128', "addresses": "510", "class": "2B"},
    24: {"decimal notation": "255.255.255.0", "subnets": '256', "addresses": "254", "class": "1C"},
    25: {"decimal notation": "255.255.255.128", "subnets": '2', "addresses": "126", "class": "1/2C"},
    26: {"decimal notation": "255.255.255.192", "subnets": '4', "addresses": "62", "class": "1/4C"},
    27: {"decimal notation": "255.255.255.224", "subnets": '8', "addresses": "30", "class": "1/8"},
    28: {"decimal notation": "255.255.255.240", "subnets": '16', "addresses": "14", "class": "1/16C"},
    29: {"decimal notation": "255.255.255.248", "subnets": '32', "addresses": "6", "class": "1/32C"},
    30: {"decimal notation": "255.255.255.252", "subnets": '64', "addresses": "2", "class": "1/64C"},
    31: {"decimal notation": "255.255.255.254", "subnets": '128', "addresses": "0", "class": "1/128C"}
}

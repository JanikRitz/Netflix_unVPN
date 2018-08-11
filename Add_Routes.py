import subprocess

mask_map = {
    4: '240.0.0.0',
    5: '248.0.0.0',
    6: '252.0.0.0',
    7: '254.0.0.0',
    8: '255.0.0.0',
    9: '255.128.0.0',
    10: '255.192.0.0',
    11: '255.224.0.0',
    12: '255.240.0.0',
    13: '255.248.0.0',
    14: '255.252.0.0',
    15: '255.254.0.0',
    16: '255.255.0.0',
    17: '255.255.128.0',
    18: '255.255.192.0',
    19: '255.255.224.0',
    20: '255.255.240.0',
    21: '255.255.248.0',
    22: '255.255.252.0',
    23: '255.255.254.0',
    24: '255.255.255.0',
    25: '255.255.255.128',
    26: '255.255.255.192',
    27: '255.255.255.224',
    28: '255.255.255.240',
    29: '255.255.255.248',
    30: '255.255.255.252',
}


def ip_addresses():
    addresses = []
    with open('IP_adresses.txt') as file:
        for line in file:
            line = line.strip('\n')
            addresses.append(tuple(line.split('/')))
    return addresses


def add_route(address, gateway):
    ip_address = address[0]
    mask = mask_map[int(address[1])]
    command = f'route -p ADD {ip_address} MASK {mask} {gateway}'
    process = subprocess.Popen(["powershell", command], stdout=subprocess.PIPE);
    result = process.communicate()[0]
    return result


if __name__ == '__main__':
    gateway = '192.168.1.101'
    for address in ip_addresses():
        print(add_route(address, gateway))

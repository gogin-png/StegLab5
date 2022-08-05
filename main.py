from scapy.all import *
from scapy.layers.inet import IP


def write_to_file(byte):
    print(byte)
    a = chr(byte)
    #a = str(byte)
    print(a)
    with open(r'D:\StegLab5\output.txt', 'a') as f:
        f.write(a)
        # f.write(bytes(char))


def start():
    secret_tos = 0xD
    dest = '192.168.1.123'
    i = 0
    time_start = time.time()
    filename = r"D:\StegLab5\hello.exe"
    with open(filename, "rb") as f:
        text = f.read()
    print(text)
    for byte in text:
        print(byte)
        send(IP(tos=secret_tos, len=byte, dst=dest, flags='DF'))
        i += 1
    t = time.time() - time_start
    print("Время передачи: ", t)
    print("Пропускная способность канала:", len(text) * 16 / t)
    if i != len(text):
        raise ValueError(f'Ошибка! Было передано {i} первых символов')


start()

#pkt = sniff(filter='ip[1]=0xD', prn=lambda x: write_to_file(x[IP].len))

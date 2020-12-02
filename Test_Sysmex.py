# Test_Sysmex 2020-10-02
import socket
import argparse
import sys
from argparse import ArgumentParser

# host = '127.0.0.1'
# port = 20350  # моделирую отправку от SYSMEX XN-350 :)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', nargs='?', default='192.168.12.55')
    parser.add_argument('port', nargs='?', default=20550)
    parser.add_argument('message', nargs='?', default='QkrQ')
    return parser


def send_message(mes) -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(mes)


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    host = namespace.host
    port = int(namespace.port)
    mess = namespace.message
    print(namespace)
    print(f'type host:{type(host)}, host={host}')
    print(f'type port:{type(port)}, port={port}')
    print(f'type mess:{type(mess)}, mess={mess}')

    # print(f'Run Client mode.Testing HOST={host}:{port}')
    # message = "Qkrq - тест анализатора."
    msg = mess.encode('utf-8')
    print(f'type msg:{type(msg)}, msg={msg}')

    send_message(msg)
    print(f'send {msg}')
    print(f'send {msg.decode()}')

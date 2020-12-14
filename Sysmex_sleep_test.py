# Sysmex_sleep_test 2020-12-14
import sys
import socket
HOST = '127.0.0.1'
PORT = 20550  # моделирую отправку от SYSMEX XN-550
BUFFER_SIZE = 1024 * 20


def sendmes(mes) -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(mes)


print(f'Run Client mode.Testing HOST={HOST}:{PORT}')
msg = b'qkrq'

if __name__ == '__main__':
    args = sys.argv
    # args = ['Sysmex_aleep_test.py', '1234', 'qwer', 'кукуas32']
    # args = ['Sysmex_aleep_test.py']
    parm = args[1:]
    lst = ' '.join(parm)
    # print(lst)
    # print(type(lst))
    # print(len(lst))
    msg2 = msg + lst.encode()
    # print(bb)
    sendmes(msg2)

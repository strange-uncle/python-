from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime
from time import sleep
from threading import Thread
from json import dumps
from base64 import b64encode


def time_service():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('192.168.0.187', 12345))
    server.listen(123)
    print('time server started.')
    while True:
        client, addr = server.accept()
        print(str(addr) + ' connected to time service')
        client.send('get the datetime is:'.encode('utf-8'))
        client.send(str(datetime.now()).encode('utf-8'))
        # single threading will block other connection
        sleep(10)
        client.close()


def time_service_multi_threading():
    class FileTransferHandler(Thread):

        def __init__(self, c: 'socket') -> None:
            super().__init__()
            self.client = c
        
        def run(self) -> None:
            data = dict()
            data['name'] = 'a.png'
            data['data'] = file_data
            json_content = dumps(data)
            self.client.send(json_content.encode('utf-8'))
            # won't block other connections
            sleep(10)
            self.client.close()
    
    server = socket()
    server.bind(('192.168.0.187', 12345))
    server.listen(123)
    print('start time service listening with multi-threading...')
    with open('./read_pic/a.png', 'rb') as f:
        # why need decode('utf-8')??? still don't know
        file_data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        FileTransferHandler(client).start()

   
if __name__ == '__main__':
    # get the datetime is:2019-07-22 20:56:18.318955
    # 遗失对主机的连接。
    # time_service()
    time_service_multi_threading()


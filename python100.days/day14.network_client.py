from socket import socket
from json import loads
from base64 import b64decode


def main():
    client = socket()
    client.connect(('192.168.0.187', 12345))
    print(client.recv(1024).decode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
    client.close()


def pic_reader_multi_threading():
    client = socket()
    client.connect(('192.168.0.187', 12345))
    b = bytes()
    data = client.recv(1024)
    while data:
        b += data
        data = client.recv(1024)
    
    result_dict = loads(b.decode('utf-8'))
    pic_name = result_dict['name']
    pic_data = result_dict['data'].encode('utf-8')
    with open('./write_pic/' + pic_name, 'wb') as f:
        f.write(b64decode(pic_data))
    print('pic saved.')
    

if __name__ == '__main__':
    # main()
    pic_reader_multi_threading()

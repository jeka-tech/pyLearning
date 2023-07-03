import socket
import json
import time
from threading import Thread

import select

import variables_list

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 8000))
serv_sock.listen(2)

serv_key = True

def serv_forever():

    while serv_key:
        # Бесконечно обрабатываем входящие подключения
        client_sock, client_addr = serv_sock.accept()
        client_sock.settimeout(0.3)
        print('Connected by', client_addr)

        while serv_key:
            try:
                print('trying...')
                data = client_sock.recv(1024)
                data_string = str(data)
                print(data_string)
                if 'GET / ' in str(data):
                    client_sock.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
                    client_sock.sendall(b'lol kek 4eburek\r\n')
                elif 'Temp01' in data_string:
                    client_sock.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
                    decoded_answer = json.loads(data_string)
                    variables_list.temp_01 = float(decoded_answer["Temp01"])
                    print(variables_list.temp_01)
                else:
                    client_sock.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
                    client_sock.sendall(b'Bad request\r\n')
                if not data:
                    print('no data')
                    client_sock.close()
                    break
                client_sock.close()
            except Exception as err:
                print(err)
                print('timing')
                client_sock.close()
                break



        # print(err)
        # def read_message():
        #     while serv_key:
        #         try:
        #             data = client_sock.recv(1024)
        #             print(data)
        #         except Exception as err:
        #             print(err)
        #
        #
        # thread_1 = Thread(target=read_message)
        # thread_1.start()



            # try:
            #
            #     data = client_sock.recv(1024)
            #
            #     if not data:
            #         break
            # except Exception as err:
            #     print(err)


            # try:
            #     # client_sock.settimeout(1)
            #     try:
            #         data = client_sock.recv(1)
            #         print(data)
            #     except Exception as err:
            #         client_sock.close()
            #         print(err)
            #         break
            #     data_string = data.decode('utf-8')
            #     if 'Temp01' in data_string:
            #         decoded_hand = json.loads(data_string)
            #         variables_list.temp_01 = float(decoded_hand["Temp01"])
            #         print(variables_list.temp_01)
            #         client_sock.sendall(b'HTTP/1.1 200 OK\r\n')
            #     elif 'GET / ' in data_string:
            #         client_sock.sendall(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: 2Connection: close\r\n\r\nOK\r\n')
            #     else:
            #         client_sock.sendall(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: 5Connection: close\r\n\r\nnotOK\r\n')
            #     if not data:
            #         # Клиент отключился
            #         break
            #     # client_sock.sendall(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: 2Connection: close\r\n\r\nOK\r\n')
            # except Exception as err:
            #     print(err)


if __name__ == '__main__':
    serv_forever()
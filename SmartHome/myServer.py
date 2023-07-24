import json
import select
import socket

temp_01 = 0.0
hum_01 = 0.0

serv_key = True

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 8000))
serv_sock.listen(2)

def serv_forever():

    while True:

        while serv_key:
            client_sock, client_addr = serv_sock.accept()
            client_sock.settimeout(0.3)
            print('Connected by', client_addr)

            r, _, _ = select.select([client_sock], [], [], 1)

            while r:
                try:
                    global temp_01, hum_01
                    data = client_sock.recv(1024)
                    data_string = str(data)
                    print(data_string)
                    if 'GET / ' in data_string:
                        client_sock.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
                        client_sock.sendall(b'lol kek 4eburek\r\n')

                    elif 'Temp01' in data_string:
                        client_sock.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
                        decoded_answer = json.loads(data)
                        temp_01 = float(decoded_answer["Temp01"])
                        hum_01 = float(decoded_answer["Hum01"])
                    if not data:
                        client_sock.close()
                        break
                except Exception as err:
                    print(err)
                    client_sock.close()
                    break


if __name__ == '__main__':
    serv_forever()
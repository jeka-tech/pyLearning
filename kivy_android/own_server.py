import socket
import json


serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 8000))
serv_sock.listen(3)

serv_key = True
def serv_forever():

    while serv_key:
        # Бесконечно обрабатываем входящие подключения
        client_sock, client_addr = serv_sock.accept()
        print('Connected by', client_addr)

        while serv_key:
            # Пока клиент не отключился, читаем передаваемые
            # им данные и отправляем их обратно
            try:
                client_sock.settimeout(1)
                try:
                    data = client_sock.recv(1024)
                except Exception as err:
                    client_sock.close()
                    print(err)
                    break
                data_string = data.decode('utf-8')
                if 'Temp01' in data_string:
                    decoded_hand = json.loads(data_string)
                    print(decoded_hand["Temp01"])
                if not data:
                    # Клиент отключился
                    break
                client_sock.sendall(data)

            except Exception as err:
                print(err)

        client_sock.close()
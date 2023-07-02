import socket
import json

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 8000))
serv_sock.listen(10)

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)
        data_string = data.decode('utf-8')
        if 'Temp01' in data_string:
            decoded_hand = json.loads(data_string)
            print(decoded_hand["Temp01"])
        if not data:
            # Клиент отключился
            break
        client_sock.sendall(data)

    client_sock.close()
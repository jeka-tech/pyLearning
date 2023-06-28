import time

import serial, time

s = serial.Serial('COM6', 115200)

while True:
    time.sleep(2)

    try:
        if s.isOpen() == True:
            a = s.readline().decode('utf-8')
            print(f'Ответ от контроллера: {a}')
        else:
            s.open()

    except Exception as err:
        print(err)
        s.close()


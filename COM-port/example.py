import serial
import time

s = serial.Serial('COM4', 115200)


while True:

    try:
        if (s.isOpen() == False):
            s.open()
            print('Порт закрыт')
        a = s.readline().decode('utf-8')
        print(f'Ответ от устройства: {a}')

    except Exception as err:
        print(err)
        s.close()

    time.sleep(2)

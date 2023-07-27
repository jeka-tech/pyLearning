import threading
import time
from threading import Thread
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.properties import StringProperty
import myServer
from bs4 import BeautifulSoup
import requests

import cv2
cap = cv2.VideoCapture('rtsp://admin:@192.168.0.111/1')

temp_01 = 0.0

Builder.load_string("""

<Test>:
    do_default_tab: False
    
    TabbedPanelItem:
        text: 'Панель'

        GridLayout:
            height: 1000
            cols: 2

            
            BoxLayout: 
                padding: 10
                canvas.before:
                    Color:
                        rgba: 39/255, 204/255, 245/255, 1
                    Line:
                        width: 1
                        rectangle: self.x, self.y, self.width, self.height
                
                GridLayout:
                    cols: 4
                    spacing: 10
                    Label:
                        text: 'Кабинет'
                    ToggleButton:
                        id: cab_1
                        text: 'Свет 1'
                    ToggleButton:
                        id: cab_2
                        text: 'Свет 2'
                    Label:
                    
                    Label:
                        text: 'Детская'
                    ToggleButton:
                        id: det_1
                        text: 'Свет 1'
                    ToggleButton:
                        id: det_2
                        text: 'Свет 2'
                    Label:
                    
                    Label:
                        text: 'Зал'
                    ToggleButton:
                        id: zal_1
                        text: 'Свет 1'
                    ToggleButton:
                        id: zal_2
                        text: 'Свет 2'
                    Label:
                    
                    Label:
                        text: 'Кухня'
                    ToggleButton:
                        id: kuh_1
                        text: 'Свет 1'
                    ToggleButton:
                        id: kuh_2
                        text: 'Свет 2'
                    Label:
                        id: lab1
                        text: 'woooooh' if kuh_1.state == 'down' else ''
                    
                    Label:
                        text: 'Ванная'
                    ToggleButton:
                        text: 'Свет'
                    ToggleButton:
                        text: 'Пол'
                    ToggleButton:
                        text: 'Вент.'
                    
                    Label:
                        text: 'Туалет'
                    ToggleButton:
                        text: 'Свет'
                    ToggleButton:
                        text: 'Пол'
                    ToggleButton:
                        text: 'Вент.'
                    
                    Label:
                        text: 'Коридор'
                    ToggleButton:
                        text: 'Свет'
                    Label:
                    Label:
                    
                    Label:
                        text: 'Прачечная'
                    ToggleButton:
                        text: 'Свет'
                    ToggleButton:
                        text: 'Утюг'
                    Label:
                    
            
            BoxLayout:
                size_hint: .6, 1
                orientation: 'vertical'
                padding: 10
                spacing: 10
                canvas.before:
                    Color:
                        rgba: 39/255, 204/255, 245/255, 1
                    Line:
                        width: 1
                        rectangle: self.x, self.y, self.width, self.height
                
                  
                # Label:
                #     font_name: 'seguiemj'
                #     text: "🌶️"     
                Button:
                    size_hint: 1, .15
                    text: 'Прогноз погоды:'
                    on_release: root.manual_update_forecast()
                
                Label:
                    text_size: self.size
                    valign: 'top'
                    text: root.forecast    
                        
                GridLayout:
                    cols: 2
                    Label:
                        halign: 'center'
                        text: 'Температура\\nна улице'
                    Label:
                        text: root.streetTemp
                    
                    Label:
                        halign: 'center'
                        text: 'Влажность\\nна улице'
                    Label:
                        text: root.streetHum
                    
                    Label:
                        halign: 'center'
                        text: 'Атм.\\nдавление'
                    Label:
                        text: '755'
            
                    
    TabbedPanelItem:
        text: 'Видео'
        BoxLayout:
            orientation: 'vertical'
            ToggleButton:
                text: 'Male'
                group: 'sex'
            Switch:
                active: True
            Label:
                text: 'Second tab content area'
            Button:
                text: 'Button that does nothing'
    TabbedPanelItem:
        text: 'Настройки'
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: 'Запустить сервер'
                on_press: root.manage_server('Start server')
            Button:
                text: 'Остановить сервер'
                on_press: root.manage_server('Stop server')
            Label:
                text: root.serverStatus

""")


class Test(TabbedPanel):
    streetTemp = StringProperty()
    streetHum = StringProperty()
    forecast = StringProperty()
    serverStatus = StringProperty()
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

        self.thread_1 = Thread(target=myServer.serv_forever, daemon=True)
        self.thread_2 = Thread(target=self.update_variables, daemon=True)
        self.thread_3 = Thread(target=self.update_forecast, daemon=True)
        self.thread_1.start()
        self.thread_2.start()
        self.thread_3.start()
    def manage_server(self, instance):

        if instance == 'Start server':
            myServer.serv_key = True
            print(threading.enumerate())
            self.serverStatus = f"The server is running {myServer.serv_key}"

        elif instance == 'Stop server':
            myServer.serv_key = False
            self.serverStatus = f"The server is running {myServer.serv_key}"

    def manual_update_forecast(self):
        try:
            page = requests.get('https://rp5.ru/Погода_в_Самаре,_Самарская_область')
            soup = BeautifulSoup(page.text, "html.parser")
            temp = soup.find('div', id='forecastShort-content')
            for match in temp.findAll('span', class_="t_1"):
                match.clear()
            self.forecast = temp.text[1:]
        except Exception as err:
            print(err)
            self.forecast = 'Не удалось загрузить прогноз погоды'

    def update_forecast(self):
        while True:
            try:
                page = requests.get('https://rp5.ru/Погода_в_Самаре,_Самарская_область')
                soup = BeautifulSoup(page.text, "html.parser")
                temp = soup.find('div', id='forecastShort-content')

                for match in temp.findAll('span', class_="t_1"):
                    match.clear()

                self.forecast = temp.text[1:]
            except Exception as err:
                print(err)
                self.forecast = 'Не удалось загрузить прогноз погоды'
            time.sleep(3600)
    def update_variables(self):
        while True:
            self.streetTemp = f'{myServer.temp_01:.1f}'
            self.streetHum = f'{myServer.hum_01:.1f}'
            time.sleep(1)
class TabbedPanelApp(App):

    def build(self):
        return Test()



if __name__ == '__main__':
    TabbedPanelApp().run()
import threading
import time
from threading import Thread
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.properties import StringProperty
import myServer

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
                    Button:
                        id: cab_1
                        text: 'Свет 1'
                    Button:
                        id: cab_2
                        text: 'Свет 2'
                    Label:
                    
                    Label:
                        text: 'Детская'
                    Button:
                        id: det_1
                        text: 'Свет 1'
                    Button:
                        id: det_2
                        text: 'Свет 2'
                    Label:
                    
                    Label:
                        text: 'Зал'
                    Button:
                        id: zal_1
                        text: 'Свет 1'
                    Button:
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
                        text: 'Вентилятор'
                    
                    Label:
                        text: 'Туалет'
                    ToggleButton:
                        text: 'Свет'
                    ToggleButton:
                        text: 'Пол'
                    ToggleButton:
                        text: 'Вентилятор'
                    
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
                padding: 10
                canvas.before:
                    Color:
                        rgba: 39/255, 204/255, 245/255, 1
                    Line:
                        width: 1
                        rectangle: self.x, self.y, self.width, self.height
                GridLayout:
                    cols: 2
                    Label:
                        text: 'Температура\\n на улице'
                    Label:
                        text: root.streetTemp
                    
                    Label:
                        text: 'Влажность\\n на улице'
                    Label:
                        text: root.streetHum
                    
                    Label:
                        text: 'Атмосферное\\n давление'
                    Label:
                        text: '755 мм.рт.ст.'
            
                    
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
                text: 'Serv ...'

""")


class Test(TabbedPanel):
    streetTemp = StringProperty()
    streetHum = StringProperty()
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        # Clock.schedule_interval(self.update, 5)

        self.thread_1 = Thread(target=myServer.serv_forever, daemon=True)
        self.thread_2 = Thread(target=self.update_variables, daemon=True)
        self.thread_1.start()
        self.thread_2.start()
    def manage_server(self, instance):

        if instance == 'Start server':
            myServer.serv_key = True
            print(threading.enumerate())
            # self.label_1.text = f"The server is running {myServer.serv_key}"

        elif instance == 'Stop server':
            myServer.serv_key = False
            # self.label_1.text = f"The server is stopped {myServer.serv_key}"
    # def update(self, *args):
    #     print(type(temp_01))
    #     self.random_number = f'{temp_01:.1f}'
    #     print(f'{temp_01:.1f}')

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
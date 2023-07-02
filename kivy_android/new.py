import time

from kivy.app import  App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from threading import Thread
import own_server
import threading
import variables_list

Builder.load_file('theme.kv')
class MyApp(App):
    Window.clearcolor = (1, 1, 1, 1)
    label_1 = Label(text='...')
    label_2 = Label(text='...')
    def build(self):

        self.thread_1 = Thread(target=own_server.serv_forever, daemon=True)
        self.thread_2 = Thread(target=self.update_variables, daemon=True)
        self.thread_2.start()

        main_layout = BoxLayout()
        main_layout.add_widget(Button(text = 'Start server', on_press = self.manage_server))
        main_layout.add_widget(Button(text = 'Stop server', on_release = self.manage_server))

        main_layout.add_widget(self.label_1)
        main_layout.add_widget(self.label_2)

        return main_layout

    def update_variables(self):
        while True:
            self.label_2.text = f'Температура: {variables_list.temp_01:.1f}'
            time.sleep(1)

    def manage_server(self, instance):

        if instance.text == 'Start server' and not self.thread_1.is_alive():
            own_server.serv_key = True
            self.thread_1 = Thread(target=own_server.serv_forever, daemon=True)
            self.label_1.text = "starting..."
            self.thread_1.start()
            print(threading.enumerate())
            self.label_1.text = "The server is running"

        elif instance.text == 'Stop server':
            self.label_1.text = "stoping..."
            own_server.serv_key = False
            self.label_1.text = "The server is stopped"










if __name__ == '__main__':

    MyApp().run()
    # thread_1.join()

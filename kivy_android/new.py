from kivy.app import  App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from threading import Thread
import own_server
import threading


Builder.load_file('theme.kv')
class MyApp(App):
    Window.clearcolor = (1, 1, 1, 1)
    label_1 = Label(text='...')

    def build(self):

        self.thread_1 = Thread(target=own_server.serv_forever, daemon=True)

        main_layout = BoxLayout()
        main_layout.add_widget(Button(text = 'Start server', on_press = self.manage_server))
        main_layout.add_widget(Button(text = 'Stop server', on_release = self.manage_server))

        main_layout.add_widget(self.label_1)

        return main_layout

    def manage_server(self, instance):

        if instance.text == 'Start server' and not self.thread_1.is_alive():
            own_server.serv_key = True
            self.thread_1 = Thread(target=own_server.serv_forever, daemon=True)
            self.label_1.text = "starting..."
            self.thread_1.start()
            print(threading.enumerate())

        elif instance.text == 'Stop server':
            self.label_1.text = "stoping..."

            def stopping():
                own_server.serv_key = False

            self.thread_2 = Thread(target=stopping, daemon=True)
            self.thread_2.start()










if __name__ == '__main__':

    MyApp().run()
    # thread_1.join()

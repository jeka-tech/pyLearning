from threading import Thread
from http.server import HTTPServer

from kivy.graphics import Rectangle, Color


import serv

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout




def serving():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, serv.ServerHandler)
    try:

        httpd.serve_forever()

    except KeyboardInterrupt:
        pass
    httpd.server_close()


def gui():
    from kivy.core.window import Window
    Window.clearcolor = (1, 1, 1, 1)

    class MyApp(App):

        # cam = Camera()
        def build(self):
            layout_1 = BoxLayout(orientation='vertical', padding=50)
            layout_1.add_widget(Button(text="Play", on_press=self.foo))
            layout_1.add_widget(Button(text="Start server", on_press=self.start_server_thread))
            layout_1.add_widget(Button(text="Stop server", on_press=self.stop_server_thread))
            layout_1.add_widget(Label(text="Play"))

            # layout_1.add_widget(self.cam)

            return layout_1

            # return Camera(play=True)

            # return Button(
            #     text="First button",
            #     font_size = 20,
            #     on_press = self.foo,
            #     background_color = [1,1,0,1],
            #     background_normal = ""
            # )

        # def play_cam(self, inst):
        #     self.cam.play = not self.cam.play
        def foo(self, inst):
            inst.text = "hi"
            print("test")

        def start_server_thread(self, inst):
            t1.start()

        def stop_server_thread(self, inst):
            t1.join()


    MyApp().run()



if __name__ == '__main__':
    t1 = Thread(target=serving)
    t2 = Thread(target=gui)
    # t1.start()
    t2.start()
    print("123")
    # t1.join()
    t2.join()
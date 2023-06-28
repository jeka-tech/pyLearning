from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
class MyApp(App):

    cam = Camera()
    def build(self):

        layout_1 = BoxLayout(orientation='vertical')
        layout_1.add_widget(Button(text="Play", on_press = self.play_cam))
        layout_1.add_widget(self.cam)

        return layout_1

        # return Camera(play=True)

        # return Button(
        #     text="First button",
        #     font_size = 20,
        #     on_press = self.foo,
        #     background_color = [1,1,0,1],
        #     background_normal = ""
        # )
    def play_cam(self, inst):
        self.cam.play = not self.cam.play
    def foo(self, inst):
        inst.text = "hi"
        print("test")

if __name__ == '__main__':
    MyApp().run()
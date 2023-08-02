from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

Builder.load_string("""

<OtherMethod>:
    do_default_tab: False
    TabbedPanelItem:
        text: 'Вкладка 1'
        BoxLayout:
            Button:
                text: "First button"
            Button:
                text: "Second button"
                on_press: root.foo(self)
    
    TabbedPanelItem:
        text: 'Вкладка 2'
        KivyCamera:
""")

class KivyCamera(Image):
    def __init__(self, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = cv2.VideoCapture('rtsp://admin:@192.168.0.111')
        Clock.schedule_interval(self.update, 1.0 / 30)
    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # convert it to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tobytes()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture

class OtherMethod(TabbedPanel):
    def foo(self, inst):
        inst.text = "new label"
class MyApp(App):
    def build(self):

        return OtherMethod()

if __name__ == '__main__':
    MyApp().run()
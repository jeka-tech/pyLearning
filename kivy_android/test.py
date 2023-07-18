from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

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
                        text: '25.63 °С'
                    
                    Label:
                        text: 'Влажность\\n на улице'
                    Label:
                        text: '35 %'
                    
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
        RstDocument:
            text:
                '\\n'.join(("Hello world", "-----------",
                "You are in the third tab."))

""")


class Test(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        return Test()



if __name__ == '__main__':
    TabbedPanelApp().run()
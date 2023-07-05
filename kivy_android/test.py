from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

Builder.load_string("""

<Test>:
    do_default_tab: False
    
    TabbedPanelItem:
        text: 'Панель'
        Label:
            text: 'First tab content area'
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
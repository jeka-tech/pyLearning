from kivy.app import App                        # base Class of your App inherits from the App class.
from kivy.uix.gridlayout import GridLayout      # GridLayout arranges children in a matrix.
from kivy.uix.label import Label                # Label is used to label something
from kivy.uix.textinput import TextInput        # used to take input from users
from kivy.uix.button import Button

class LoginScreen(GridLayout):
	def __init__(self, **var_args):
		super(LoginScreen, self).__init__(**var_args)
		self.cols = 2	 # You can change it accordingly

		self.add_widget(Label(text='User Name'))

		self.username = TextInput(multiline=True)
		self.add_widget(self.username)

		# self.add_widget(Label(text='password'))

		# self.password = TextInput(password=True, multiline=False)
		self.add_widget(Label(text='Comfirm password'))

		self.password = TextInput(password=True, multiline=False)
		self.add_widget(self.password)

		self.add_widget(Button(text='Comfirm'))
		self.add_widget(Label(text='...'))

# the Base Class of our Kivy App
class MyApp(App):
	def build(self):
		# return a LoginScreen() as a root widget
		return LoginScreen()


if __name__ == '__main__':
	MyApp().run()

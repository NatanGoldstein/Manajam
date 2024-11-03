from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.button import Button

class DefaultLabel(Label):
    pass

class DefaultText(TextInput):
    pass

class SubHeader(Label):
    pass

class DefaultButton(Button):
    pass

class DefaultSpinner(Spinner):
    def __init__(self, **kwargs):
        super(DefaultSpinner, self).__init__(**kwargs)
        self.color = 'grey'
    def on_text(self, *args):
        # Change text color to black after an option is selected
        self.color = 'black'  # Set the color to black

class DefaultSpinnerOption(SpinnerOption):
    pass
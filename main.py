from kivymd.app import MDApp
from backend.AppDefaults import *
from backend.Screens import *
from backend.UserManagement import *
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy_garden.mapview import MapView
import geocoder
from kivymd.uix.screenmanager import MDScreenManager
from ctypes import windll, c_int64

windll.user32.SetProcessDpiAwarenessContext(c_int64(-4))


Window.size = (310, 580)
Window.clearcolor = (245/255,222/255,179/255,1)



class WindowManager(MDScreenManager):
    pass
       

class manajam(MDApp):
    def build(self):
        # Load the KV file after app initialization
        self.root = Builder.load_file('frontend/ManajamApp.kv')
        return self.root
    
if __name__ == "__main__":
    manajam().run()
    



from kivymd.app import MDApp
from backend.AppDefaults import *
from backend.Screens import *
from backend.UserManagement import *
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy_garden.mapview import MapView
import geocoder
from kivy.uix.screenmanager import FadeTransition
from kivymd.uix.screenmanager import MDScreenManager


Window.size = (310, 580)
Window.clearcolor = (245/255,222/255,179/255,1)



class WindowManager(MDScreenManager):
    def go_to_search_screen(self):
        self.transition = FadeTransition()
        self.transition.duration = 0.1
        self.transition.clearcolor = (245/255,222/255,179/255,1)
        self.current = 'search_screen'
       

class manajam(MDApp):
    def build(self):
        # Load the KV file after app initialization
        self.root = Builder.load_file('frontend/ScreenManager.kv')
        return self.root
    
if __name__ == "__main__":
    manajam().run()
    



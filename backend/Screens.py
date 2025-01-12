from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.animation import Animation
from backend.UserManagement import *
import geocoder


class OpenScreen(MDScreen):
    hint_text_color = ListProperty([0.5, 0.5, 0.5, 1])
    def logIn(self, email, password):
        if checkCredentials(email, password):
            self.manager.transition.direction = 'left'
            self.manager.current = 'main_screen'
        else:
            self.hint_text_color = [1, 0, 0, 1]
            self.ids.email_input.text = ''
            self.ids.password_input.text = ''
            self.ids.email_input.hint_text = 'Invalid credentials'

class MusicianSignup(MDScreen):
    def signUp(self):
        user_info = ()
        for id in self.ids:
            user_info += (self.ids[id].text,)
        insertCredentials(*user_info)
        self.manager.transition.direction = 'right'
        self.manager.current = 'open_screen'

class MainScreen(MDScreen):
    pass

class MapScreen(MDScreen):
    g = geocoder.ip('me')
    if g.ok:
        current_lat = g.latlng[0]
        current_lon = g.latlng[1]
        print("got your location")
    else:
        # Fallback to a default location if current location can't be fetched
        current_lat = 31.0465  # Default latitude (Israel)
        current_lon = 34.8516  # Default longitude (Israel)

class SearchScreen(MDScreen):
    search_result = StringProperty("")

    def search(self):
        search_type = self.ids.type.text.strip()
        search_text = self.ids.search_text.text.strip()
        for index, row in df.iterrows():
            if row[search_type] == search_text:
                self.search_result += f"{row['First']} {row['Last']}"


class BandsScreen(MDScreen):
    pass

class TasksScreen(MDScreen):
    pass

class UserScreen(MDScreen):
    pass
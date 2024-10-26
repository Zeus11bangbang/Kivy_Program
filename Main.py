from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ObjectProperty, StringProperty, ColorProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationrail import MDNavigationRailItem
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText
)

### This is for testing ###
'''class TestScreen(Screen):
    def logout_user(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "screen_login"

    def dashboard_user(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "screen_dashboard"'''

### Login Screen Class and all its functions ####
class LoginScreen(Screen):
    email = ObjectProperty()
    password = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_key_down=self.on_key_down)

    def loggin_user(self):
        print(f"Login button clicked with email: {self.email.text} and password: {self.password.text}")
        if self.email.text == 'admin' and self.password.text == 'admin':
            print('Credentials correct')
            self.manager.transition = SlideTransition(direction='left')
            self.manager.current = "screen_main"
            print("Successfully transitioned to Main Screen")
        else:
            print("Login failed")

    def on_key_down(self, window, key, *args):
        # Tab key is typically key code 9
        if key == 9:
            if self.email.focus:
                self.password.focus = True
                return True  # Stop the event here
            elif self.password.focus:
                self.email.focus = True
                return True  # Stop the event here
        return False

    def clear_button(self):
        self.email.text = ''
        self.password.text = ''

### Main Screen Class and all its Functions ###
class MainScreen(Screen):
    def logout_user(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "screen_login"

    def dashboard_user(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "screen_dashboard"

### Dashboard Class and all its Functions ###
class DashboardScreen(Screen):
    def back_to_main(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "screen_main"

class CommonNavigationRailItem(MDNavigationRailItem):
    text = StringProperty()
    icon = StringProperty()

class DrawerLabel(MDBoxLayout):
    icon = StringProperty()
    text = StringProperty()

class MDFloatLayout(MDLabel):
    font_size = StringProperty()
    font_style = StringProperty()

class DrawerItem(MDNavigationDrawerItem):
    icon = StringProperty()
    text = StringProperty()
    trailing_text = StringProperty()
    trailing_text_color = ColorProperty()

    _trailing_text_obj = None

    def on_trailing_text(self, instance, value):
        self._trailing_text_obj = MDNavigationDrawerItemTrailingText(
            text=value,
            theme_text_color="Custom",
            text_color=self.trailing_text_color,
        )
        self.add_widget(self._trailing_text_obj)

    def on_trailing_text_color(self, instance, value):
        self._trailing_text_obj.text_color = value

class MyApp(MDApp):
    '''def build(self):
        return Builder.load_string(KV)'''

    def build(self):
        self.theme_cls.theme_style = "Dark"
        # Load KV files
        Builder.load_file('LoginScreen.kv')
        #Builder.load_file('testscreen.kv')
        Builder.load_file('MainScreen.kv')
        Builder.load_file('DashboardScreen.kv')

        # Initialize the screen manager
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='screen_login'))
        #sm.add_widget(TestScreen(name='screen_test'))
        sm.add_widget(MainScreen(name='screen_main'))
        sm.add_widget(DashboardScreen(name='screen_dashboard'))

        return sm

if __name__ == "__main__":
    MyApp().run()
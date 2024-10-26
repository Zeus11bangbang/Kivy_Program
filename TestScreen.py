from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationbar.navigationbar import MDNavigationBar

# Kivy code for the UI
KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: "screen_test"

    BoxLayout:
        orientation: "horizontal"
        size_hint: 1, .4
        pos_hint: {"center_x": .5, "center_y": .825}
        spacing: 20
        padding: 10

        canvas.before:
            
            Rectangle:
                size: self.size[0], self.size[1]
                pos: self.pos
                source: "MainScreen.png"
    BoxLayout:
        orientation: "horizontal"
        size_hint: 1, .15
        pos_hint: {"center_x": .5, "center_y": .55}
        spacing: 20
        padding: 10

        CustomNavigationBar:
            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'account-circle'
                    size: 200, 40
                    icon_size:
                    theme_text_color: "Custom"  # Allow custom color
                    text_color: [1, 1, 1, 1]  # Purple color (RGBA)
                MDNavigationItemLabel:
                    text: 'Dashboard'
                    text_color: [1, 1, 1, 1]
                    pos_hint: {"center_x": .5, "center_y": .2}

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'phone-clock'
                    theme_text_color: "Custom"  # Allow custom color
                    text_color: [1, 1, 1, 1]  # Purple color (RGBA)
                MDNavigationItemLabel:
                    text: 'Schedule Jobs'
                    text_color: [1, 1, 1, 1]
                    pos_hint: {"center_x": .5, "center_y": .2}

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'view-list'
                    theme_text_color: "Custom"  # Allow custom color
                    text_color: [1, 1, 1, 1]  # Purple color (RGBA)
                MDNavigationItemLabel:
                    text: 'View Work Orders'
                    text_color: [1, 1, 1, 1]
                    pos_hint: {"center_x": .5, "center_y": .2}

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'account-group'
                    theme_text_color: "Custom"  # Allow custom color
                    text_color: [1, 1, 1, 1]  # Purple color (RGBA)
                MDNavigationItemLabel:
                    text: 'Customer Management'
                    text_color: [1, 1, 1, 1]
                    pos_hint: {"center_x": .5, "center_y": .2}

    BoxLayout:
        orientation: "horizontal"
        size_hint: 1, .15
        pos_hint: {"center_x": .5, "center_y": .435}
        spacing: 20
        padding: 10

        CustomNavigationBar:
            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'cash'
                    size: 200, 40
                    icon_size:
                    theme_text_color: "Custom"  # Allow custom color
                    text_color: [1, 1, 1, 1]  # Purple color (RGBA)
                MDNavigationItemLabel:
                    text: 'Income/Expenses'
                    text_color: [1, 1, 1, 1]
                    pos_hint: {"center_x": .5, "center_y": .2}

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: "account-multiple-check"
                    theme_text_color: "Custom"  # Allow custom color
                    text_color: [1, 1, 1, 1]  # Purple color (RGBA)
                MDNavigationItemLabel:
                    text: 'Employee Management'
                    text_color: [1, 1, 1, 1]
                    pos_hint: {"center_x": .5, "center_y": .2}

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'cogs'
                    theme_text_color: "Custom"  # Allow custom color
                    text_color: [1, 1, 1, 1]  # Purple color (RGBA)
                MDNavigationItemLabel:
                    text: 'Settings'
                    text_color: [1, 1, 1, 1]
                    pos_hint: {"center_x": .5, "center_y": .2}

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'logout'
                    theme_text_color: "Custom"  # Allow custom color
                    text_color: [1, 1, 1, 1]  # Purple color (RGBA)
                MDNavigationItemLabel:
                    text: 'Logout'
                    text_color: [12, 1, 1, 1]
                    pos_hint: {"center_x": .5, "center_y": .2}
'''

class CustomNavigationBar(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.md_bg_color = [0.5, 0.3, 0.6, 1]  # Light grey background

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
class MainScreen(Screen):
    pass
    
if __name__ == '__main__':
    MyApp().run()



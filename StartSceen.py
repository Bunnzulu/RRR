from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

def Navigate_to_Page(Page):
    app = App.get_running_app()
    app.root.clear_widgets()
    app.root.add_widget(Page)

class BrightnessLevel(Widget):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(BrightnessLevel, cls).__new__(cls, *args, **kwargs)
            cls._instance.brightness = NumericProperty(50)
        return cls._instance

    def set_brightness(self, value):
        self.brightness = int(value)
    
    def Get_brightness(self):
        print(self.brightness)
    
class TitleScreenWidget(AnchorLayout):
    Brightness_Manager = BrightnessLevel()
    def Goto_controls_page(self):
        Navigate_to_Page(ControlsWidget())
        self.Brightness_Manager.Get_brightness()
    def Goto_settings_page(self):
        Navigate_to_Page(SettingsWidget())

class ControlsWidget(BoxLayout):
    def Back(self):
        Navigate_to_Page(TitleScreenWidget())

class SettingsWidget(GridLayout):
    Brightness_Manager = BrightnessLevel()
    def Back(self):
        Navigate_to_Page(TitleScreenWidget())
    
    def Change_brightness(self,widget):
        self.Brightness_Manager.set_brightness(int(widget.value))
        self.Brightness_Manager.Get_brightness()


class TitleScreenApp(App):
    def build(self):
        # Initialize brightness manager to ensure it is available
        Brightness_Manager = BrightnessLevel()
        return TitleScreenWidget()






TitleScreenApp().run()

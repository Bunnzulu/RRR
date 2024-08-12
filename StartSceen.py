from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.app import App

def Navigate_to_Page(Page):
    app = App.get_running_app()
    app.root.clear_widgets()
    app.root.add_widget(Page)

class TitleScreenWidget(AnchorLayout):
    def Goto_controls_page(self):
        Navigate_to_Page(ControlsWidget())

class ControlsWidget(BoxLayout):
    def Back(self):
        Navigate_to_Page(TitleScreenWidget())

class TitleScreenApp(App):
    pass






TitleScreenApp().run()
